import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, ManyToOne, JoinColumn } from 'typeorm';
import { User } from './user.entity';

@Entity('physical_snapshots')
export class PhysicalSnapshot {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @ManyToOne(() => User, user => user.snapshots, { onDelete: 'CASCADE' })
    @JoinColumn({ name: 'user_id' })
    user: User;

    @Column({ type: 'int', nullable: true })
    trap_bar_deadlift: number; // in kg

    @Column({ type: 'int', nullable: true })
    power_clean: number;

    @Column({ type: 'int', nullable: true })
    mile_time: number; // in seconds

    @Column({ type: 'int', nullable: true })
    burpee_reps: number;

    @CreateDateColumn()
    created_at: Date;
}