import { Entity, PrimaryGeneratedColumn, Column, ManyToOne } from 'typeorm';
import { ProgramSession } from './program-session.entity';

@Entity('session_exercises')
export class SessionExercise {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column()
    exercise_name: string;

    @Column()
    sets: number;

    @Column()
    reps: number;

    @Column({ nullable: true })
    rest_seconds: number;

    @Column({ type: 'text', nullable: true })
    notes: string;

    @ManyToOne(() => ProgramSession)
    session: ProgramSession;
}