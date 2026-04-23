import { Entity, PrimaryGeneratedColumn, Column, ManyToOne, OneToMany, JoinColumn } from 'typeorm';
import { User } from './user.entity';
import { ProgramBlock } from './program-block.entity';

@Entity('programs')
export class Program {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @ManyToOne(() => User)
    @JoinColumn({ name: 'coach_id' })
    coach: User;

    @Column()
    title: string;

    @Column({ type: 'text' })
    description: string;

    @Column()
    goal_primary: string; // e.g., 'Punch Power', 'Endurance'

    @Column()
    level_target: string; // e.g., 'Novice', 'Pro'

    @Column({ type: 'float', default: 0 })
    rating_avg: number;

    // حلينا مشكلة الـ unknown هنا
    @OneToMany(() => ProgramBlock, (block: ProgramBlock) => block.program)
    blocks: ProgramBlock[];
}