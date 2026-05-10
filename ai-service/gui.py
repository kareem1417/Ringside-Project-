import streamlit as st
import requests
import time

# ==========================================
# ⚙️ Page Configuration
# ==========================================
st.set_page_config(
    page_title="Ringside AI",
    page_icon="🥊",
    layout="wide",
    initial_sidebar_state="expanded"
)

API_URL = "http://localhost:8000"

# ==========================================
# 🎨 Custom CSS — Premium Dark Theme
# ==========================================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;500;600;700;800&display=swap');

    /* ---- Global ---- */
    .stApp {
        background-color: #0a0a0a;
        font-family: 'Urbanist', sans-serif;
    }
    header[data-testid="stHeader"] { background-color: #0a0a0a; }

    /* ---- Sidebar ---- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f0f 0%, #111 100%);
        border-right: 1px solid #1e1e1e;
    }
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3 {
        color: #ffffff;
    }
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown li {
        color: #aaa;
    }

    /* ---- Typography ---- */
    h1, h2, h3, .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 { color: #fff !important; }
    p, li, .stMarkdown p, .stMarkdown li, label, .stTextInput label, span { color: #ccc; }

    /* ---- Accent color override ---- */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: transparent; border-bottom: 1px solid #222; }
    .stTabs [data-baseweb="tab"] {
        background-color: #161616;
        border-radius: 8px 8px 0 0;
        color: #aaa;
        padding: 12px 28px;
        font-weight: 600;
        border: 1px solid #222;
        border-bottom: none;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1a1a1a !important;
        color: #deff9a !important;
        border-color: #deff9a !important;
        border-bottom: 2px solid #0a0a0a !important;
    }

    /* ---- Inputs ---- */
    .stNumberInput input, .stTextInput input, .stSelectbox > div > div {
        background-color: #161616 !important;
        border: 1px solid #2a2a2a !important;
        color: #fff !important;
        border-radius: 8px !important;
    }
    .stNumberInput input:focus, .stTextInput input:focus {
        border-color: #deff9a !important;
        box-shadow: 0 0 0 1px #deff9a33 !important;
    }
    .stSlider > div > div > div > div { background: #deff9a !important; }

    /* ---- Buttons ---- */
    .stFormSubmitButton > button, .stButton > button {
        background: linear-gradient(135deg, #deff9a 0%, #b5d45a 100%) !important;
        color: #0a0a0a !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px 32px !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }
    .stFormSubmitButton > button:hover, .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(222, 255, 154, 0.3) !important;
    }

    /* ---- Chat ---- */
    .stChatMessage { background-color: #131313 !important; border: 1px solid #1e1e1e !important; border-radius: 12px !important; }
    .stChatInputContainer { border-color: #2a2a2a !important; }
    .stChatInputContainer textarea { background-color: #161616 !important; color: #fff !important; }

    /* ---- Cards ---- */
    .metric-card {
        background: linear-gradient(135deg, #161616 0%, #1a1a1a 100%);
        border: 1px solid #2a2a2a;
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric-card:hover { border-color: #deff9a44; transform: translateY(-4px); box-shadow: 0 12px 30px rgba(0,0,0,0.4); }
    .metric-value { font-size: 36px; font-weight: 800; color: #deff9a; margin: 8px 0; }
    .metric-label { font-size: 14px; color: #888; text-transform: uppercase; letter-spacing: 1px; }

    .result-card {
        background: linear-gradient(135deg, #111 0%, #161616 100%);
        border: 1px solid #deff9a33;
        border-left: 4px solid #deff9a;
        border-radius: 16px;
        padding: 32px;
        margin-top: 20px;
    }
    .result-program { font-size: 32px; font-weight: 800; color: #deff9a; margin: 8px 0 16px 0; }
    .result-reason { color: #ccc; font-size: 16px; line-height: 1.7; padding: 16px; background: #0d0d0d; border-radius: 10px; border: 1px solid #1e1e1e; }
    .result-meta { display: flex; gap: 32px; margin-top: 16px; }
    .result-meta-item { color: #888; font-size: 14px; }
    .result-meta-item strong { color: #deff9a; }

    /* ---- BMI Badge ---- */
    .bmi-badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 14px;
        margin-top: 4px;
    }
    .bmi-normal { background: #deff9a22; color: #deff9a; border: 1px solid #deff9a44; }
    .bmi-under { background: #60a5fa22; color: #60a5fa; border: 1px solid #60a5fa44; }
    .bmi-over { background: #fbbf2422; color: #fbbf24; border: 1px solid #fbbf2444; }
    .bmi-obese { background: #ef444422; color: #ef4444; border: 1px solid #ef444444; }

    /* ---- Dividers ---- */
    hr { border-color: #1e1e1e !important; }

    /* ---- Alerts ---- */
    .stSuccess { background-color: #deff9a11 !important; border: 1px solid #deff9a44 !important; color: #deff9a !important; }
    .stInfo { background-color: #161616 !important; border: 1px solid #2a2a2a !important; }

    /* ---- Hero ---- */
    .hero-title { font-size: 42px; font-weight: 800; color: #fff; margin-bottom: 4px; }
    .hero-accent { color: #deff9a; }
    .hero-sub { color: #888; font-size: 18px; margin-top: 0; }

    /* ---- Section Header ---- */
    .section-icon { font-size: 28px; margin-right: 8px; }
    .section-header { font-size: 22px; font-weight: 700; color: #fff; margin-bottom: 16px; border-bottom: 2px solid #deff9a33; padding-bottom: 8px; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 📌 Sidebar
# ==========================================
with st.sidebar:
    st.markdown("# 🥊 RINGSIDE")
    st.markdown('<p style="color:#deff9a; font-size:14px; margin-top:-12px;">AI-Powered Training Intelligence</p>', unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("### 🧭 Navigation")
    st.markdown("""
    - **💬 AI Coach** — Ask anything  
    - **🎯 Recommender** — Get your program  
    """)
    st.markdown("---")

    st.markdown("### 📊 System Status")
    api_ok = False
    try:
        r = requests.get(f"{API_URL}/docs", timeout=3)
        api_ok = r.status_code == 200
    except Exception:
        pass

    if api_ok:
        st.markdown('🟢 &nbsp; API Online', unsafe_allow_html=True)
    else:
        st.markdown('🔴 &nbsp; API Offline', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<p style="color:#555; font-size:12px;">v1.0 · Built by Kareem Yasser</p>', unsafe_allow_html=True)

# ==========================================
# 🏠 Header
# ==========================================
st.markdown("""
<div style="margin-bottom: 24px;">
    <div class="hero-title">RINGSIDE <span class="hero-accent">AI</span></div>
    <p class="hero-sub">Personalized Combat Sports & Fitness Intelligence</p>
</div>
""", unsafe_allow_html=True)

# Dashboard metrics row
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="metric-card"><div class="metric-label">Model Accuracy</div><div class="metric-value">97.9%</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric-card"><div class="metric-label">Vector Retrieval</div><div class="metric-value">&lt;50ms</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-card"><div class="metric-label">Knowledge Base</div><div class="metric-value">15+</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="metric-card"><div class="metric-label">ML Engine</div><div class="metric-value">Descision Tree</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# TABS
# ==========================================
tab_chat, tab_ml = st.tabs(["💬 AI Coach (RAG Chat)", "🎯 Program Recommender (ML)"])

# ==========================================
# 💬 TAB 1: RAG CHAT
# ==========================================
with tab_chat:
    st.markdown('<div class="section-header">🧠 Ask Your AI Coach</div>', unsafe_allow_html=True)

    # Sport selector + Clear button
    col_sport, col_clear = st.columns([3, 1])
    with col_sport:
        sport_context = st.selectbox(
            "Sport Context",
            ["general", "boxing", "strength", "football", "combat_fitness", "nutrition"],
            format_func=lambda x: {
                "general": "🏋️ General Fitness",
                "boxing": "🥊 Boxing",
                "strength": "💪 Strength & Conditioning",
                "football": "⚽ Football",
                "combat_fitness": "🥋 Combat Sports",
                "nutrition": "🍎 Sports Nutrition"
            }.get(x, x),
            key="sport_select"
        )
    with col_clear:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗑️ Clear Chat"):
            st.session_state.messages = []
            st.rerun()

    st.markdown("---")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Ask anything — e.g. 'Best stance for a beginner in boxing?'"):
        st.chat_message("user").markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner("🧠 Coach is analyzing your question..."):
            try:
                # Build history for the API (exclude current question)
                api_history = []
                for msg in st.session_state.messages[:-1]:
                    api_history.append({"role": msg["role"], "content": msg["content"]})

                # Include recommended program as context if available
                current_program = st.session_state.get("last_program", None)
                user_goal = st.session_state.get("last_goal", None)

                payload = {
                    "question": prompt,
                    "sport": sport_context,
                    "history": api_history,
                    "current_program": current_program,
                    "user_goal": user_goal
                }
                response = requests.post(f"{API_URL}/ask", json=payload, timeout=60)

                if response.status_code == 200:
                    result = response.json()
                    answer = result.get("answer", "No answer received.")
                    engine = result.get("engine", "")
                    if engine:
                        answer += f"\n\n---\n*🔬 Engine: {engine}*"
                else:
                    answer = f"⚠️ Backend returned status code {response.status_code}"
            except requests.exceptions.ConnectionError:
                answer = "🔴 **Cannot connect to the API.** Make sure `main.py` is running on port 8000."
            except Exception as e:
                answer = f"⚠️ Error: {str(e)}"

        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})

# ==========================================
# 🎯 TAB 2: ML RECOMMENDER
# ==========================================
with tab_ml:
    st.markdown('<div class="section-header">🎯 Personalized Program Recommendation</div>', unsafe_allow_html=True)
    st.markdown("Fill in your athletic profile below. Our ML model will analyze your data and recommend the optimal training program.")
    st.markdown("")

    with st.form("ml_form"):
        # ---- Section 1: Biometrics ----
        st.markdown("#### 📐 Biometrics")
        bio1, bio2, bio3, bio4 = st.columns(4)
        with bio1:
            age = st.number_input("Age", min_value=14, max_value=80, value=25)
        with bio2:
            height = st.number_input("Height (cm)", min_value=140.0, max_value=220.0, value=175.0, step=0.5)
        with bio3:
            weight = st.number_input("Weight (kg)", min_value=40.0, max_value=200.0, value=75.0, step=0.5)
        with bio4:
            bmi = round(weight / ((height / 100) ** 2), 2)
            st.markdown(f"**BMI**")
            # BMI category badge
            if bmi < 18.5:
                cat, cls = "Underweight", "bmi-under"
            elif bmi < 25:
                cat, cls = "Normal", "bmi-normal"
            elif bmi < 30:
                cat, cls = "Overweight", "bmi-over"
            else:
                cat, cls = "Obese", "bmi-obese"
            st.markdown(f'<span style="font-size:28px; font-weight:800; color:#fff;">{bmi}</span> <span class="bmi-badge {cls}">{cat}</span>', unsafe_allow_html=True)

        st.markdown("---")

        # ---- Section 2: Training Profile ----
        st.markdown("#### 🏋️ Training Profile")
        tp1, tp2, tp3 = st.columns(3)
        with tp1:
            sport_type = st.selectbox("Sport Type", ["Boxing", "MMA", "General Fitness", "Football", "Wrestling"])
            days_per_week = st.slider("Training Days / Week", 1, 7, 4)
        with tp2:
            level = st.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
            years_training = st.number_input("Years of Training", min_value=0.0, max_value=30.0, value=2.0, step=0.5)
        with tp3:
            goal = st.selectbox("Primary Goal", ["Muscle Gain", "Weight Loss", "Endurance", "Strength", "Performance"])
            has_injury = st.selectbox("Injury History?", [0, 1], format_func=lambda x: "✅ Yes" if x == 1 else "❌ No")

        st.markdown("---")

        # ---- Section 3: Performance Scores ----
        st.markdown("#### ⚡ Performance Scores")
        ps1, ps2, ps3 = st.columns(3)
        with ps1:
            endurance = st.slider("🫁 Endurance", 1, 10, 7)
            strength = st.slider("💪 Strength", 1, 10, 8)
        with ps2:
            speed = st.slider("⚡ Speed", 1, 10, 6)
            flexibility = st.slider("🧘 Flexibility", 1, 10, 5)
        with ps3:
            explosiveness = st.slider("💥 Explosiveness", 1, 10, 7)
            recovery = st.slider("🛌 Recovery", 1, 10, 6)

        st.markdown("")
        submitted = st.form_submit_button("⚡ Generate My Program")

    # ---- Results ----
    if submitted:
        with st.spinner("🔬 AI is analyzing your athletic profile..."):
            try:
                payload = {
                    "Age": age, "Height_cm": height, "Weight_kg": weight, "BMI": bmi,
                    "Sport_Type": sport_type, "Level": level, "Goal": goal,
                    "Training_Days_Per_Week": days_per_week, "Years_Training": years_training,
                    "Has_Injury_History": has_injury, "Endurance_Score": endurance,
                    "Strength_Score": strength, "Speed_Score": speed,
                    "Flexibility_Score": flexibility, "Explosiveness_Score": explosiveness,
                    "Recovery_Score": recovery
                }
                response = requests.post(f"{API_URL}/recommend", json=payload, timeout=30)

                if response.status_code == 200:
                    data = response.json()

                    # Store for chat context
                    st.session_state["last_program"] = data.get("recommended_program_id", "")
                    st.session_state["last_goal"] = goal

                    program = data.get("recommended_program_id", "Unknown")
                    confidence = data.get("confidence", "N/A")
                    model_used = data.get("model_used", "N/A")
                    reason = data.get("reason", "No reasoning provided.")

                    st.markdown(f"""
                    <div class="result-card">
                        <div style="color:#888; font-size:14px; text-transform:uppercase; letter-spacing:2px;">Recommended Program</div>
                        <div class="result-program">🏆 {program}</div>
                        <div class="result-reason">{reason}</div>
                        <div class="result-meta">
                            <div class="result-meta-item">🎯 Confidence: <strong>{confidence}</strong></div>
                            <div class="result-meta-item">🤖 Model: <strong>{model_used}</strong></div>
                            <div class="result-meta-item">📊 Features: <strong>16 metrics</strong></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown("")
                    st.info("💡 **Tip:** Switch to the AI Coach tab and ask questions — your recommended program is now used as context for more personalized answers!")

                else:
                    st.error(f"⚠️ Backend returned status code {response.status_code}")
            except requests.exceptions.ConnectionError:
                st.error("🔴 **Cannot connect to the API.** Make sure `main.py` is running on port 8000.")
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)}")