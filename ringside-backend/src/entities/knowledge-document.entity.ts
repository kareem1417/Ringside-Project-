import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn } from 'typeorm';

@Entity('knowledge_documents')
export class KnowledgeDocument {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column()
    sport: string; // e.g., boxing

    @Column()
    topic: string; // e.g., strength, endurance

    @Column({ type: 'text' })
    content: string; // The actual chunk of text from the PDF

    // This is the pgvector column! length 384 matches all-MiniLM-L6-v2 model
    @Column({ type: 'vector', length: 384, nullable: true })
    embedding: string;

    @CreateDateColumn()
    created_at: Date;
}