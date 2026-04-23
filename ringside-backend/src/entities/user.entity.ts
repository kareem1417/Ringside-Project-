import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, OneToMany } from 'typeorm';
import { PhysicalSnapshot } from './physical-snapshot.entity';

@Entity('users')
export class User {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column({ unique: true })
    username: string;

    @Column({ unique: true })
    email: string;

    @Column()
    password_hash: string;

    @Column({ type: 'enum', enum: ['athlete', 'coach'], default: 'athlete' })
    role: string;

    @Column({ nullable: true })
    sport_type: string; // e.g., boxing, football

    @Column({ nullable: true })
    weight_class: string;

    @Column({ type: 'enum', enum: ['novice', 'amateur', 'pro'], default: 'novice' })
    level: string;

    @OneToMany(() => PhysicalSnapshot, snapshot => snapshot.user)
    snapshots: PhysicalSnapshot[];

    @CreateDateColumn()
    created_at: Date;
}