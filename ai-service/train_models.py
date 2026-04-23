import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import time

print("🚀 Starting ULTIMATE ML Pipeline (Cross-Validation & Tuning)...\n")

# 1. تحميل وتجهيز الداتا
df = pd.read_csv('fitness_dataset.csv')
X = df.drop('Recommended_Program_ID', axis=1)
y = df['Recommended_Program_ID']

categorical_cols = ['Sport_Type', 'Level', 'Goal']
X_encoded = pd.get_dummies(X, columns=categorical_cols)
expected_features = list(X_encoded.columns)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_encoded)

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# 2. جيش الموديلات
models = {
    "Logistic Regression": LogisticRegression(max_iter=2000, class_weight='balanced', random_state=42),
    "KNN (K-Nearest)": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(class_weight='balanced', random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42)
}

print("-" * 75)
print(f"{'Model Name':<25} | {'Cross-Val Accuracy (5-Fold)':<30} | {'Status'}")
print("-" * 75)

best_model_name = ""
best_model_score = 0
best_model_obj = None

# 3. اختبار قاسي (Cross-Validation) لكل الموديلات
for name, model in models.items():
    # بنمتحن الموديل 5 مرات مختلفة وناخد المتوسط
    cv_scores = cross_val_score(model, X_scaled, y_encoded, cv=5, scoring='accuracy', n_jobs=-1)
    mean_accuracy = np.mean(cv_scores)
    
    print(f"{name:<25} | {mean_accuracy * 100:>15.2f}% (±{np.std(cv_scores)*100:.2f}%)   | Tested")
    
    if mean_accuracy > best_model_score:
        best_model_score = mean_accuracy
        best_model_name = name
        best_model_obj = model

print("-" * 75)
print(f"\n🏆 Initial Champion: ** {best_model_name} ** with {best_model_score * 100:.2f}% accuracy!\n")

# 4. تظبيط الموديل الفائز لأقصى درجة (Hyperparameter Tuning)
# 4. تظبيط الموديل الفائز لأقصى درجة (Hyperparameter Tuning)
print(f"⚙️ Tuning the Champion ({best_model_name}) for MAX performance...")

if best_model_name == "Random Forest":
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }
    grid_search = GridSearchCV(estimator=RandomForestClassifier(class_weight='balanced', random_state=42),
                               param_grid=param_grid, cv=3, n_jobs=-1, verbose=0)
    grid_search.fit(X_scaled, y_encoded)
    final_model = grid_search.best_estimator_

elif best_model_name == "Decision Tree":
    param_grid = {
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'criterion': ['gini', 'entropy']
    }
    grid_search = GridSearchCV(estimator=DecisionTreeClassifier(class_weight='balanced', random_state=42),
                               param_grid=param_grid, cv=3, n_jobs=-1, verbose=0)
    grid_search.fit(X_scaled, y_encoded)
    final_model = grid_search.best_estimator_

else:
    final_model = best_model_obj
    final_model.fit(X_scaled, y_encoded)

# استخراج أهم 5 عوامل بتأثر في القرار (لو الموديل شجرة أو غابة)
if best_model_name in ["Random Forest", "Decision Tree"]:
    print(f"🔥 Tuning Complete! Best Parameters found: {grid_search.best_params_}")
    importances = final_model.feature_importances_
    indices = np.argsort(importances)[::-1]
    print("\n📊 Top 5 Features driving the AI's decisions:")
    for i in range(5):
        print(f"   {i+1}. {expected_features[indices[i]]} ({importances[indices[i]]*100:.1f}%)")
else:
    # لو موديل تاني كسب، هندربه على الداتا كلها عادي
    final_model = best_model_obj
    final_model.fit(X_scaled, y_encoded)

# 5. حفظ الموديل النهائي الجبار
pipeline = {
    'model': final_model,
    'scaler': scaler,
    'label_encoder': label_encoder,
    'features': expected_features
}

joblib.dump(pipeline, 'champion_model.pkl')
print("\n✅ ULTIMATE Champion Pipeline Saved Successfully! The system is now at MAX level. 🚀")