import { Entity, PrimaryGeneratedColumn, Column, ManyToOne } from 'typeorm';
import { User } from './user.entity';
import { Program } from './program.entity';

@Entity('enrollments')
export class Enrollment {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @ManyToOne(() => User)
    user: User;

    @ManyToOne(() => Program)
    program: Program;

    @Column({ type: 'date' })
    start_date: Date;

    @Column('text', { array: true })
    preferred_days: string[];
}