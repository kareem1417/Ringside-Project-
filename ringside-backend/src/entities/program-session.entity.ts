import { Entity, PrimaryGeneratedColumn, Column, ManyToOne, JoinColumn } from 'typeorm';
import { ProgramBlock } from './program-block.entity';

@Entity('program_sessions')
export class ProgramSession {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column()
    name: string; // e.g., 'Lower Body Power'

    @Column()
    day_offset: number; // Day 1, Day 3, etc.

    // السيشن بتنتمي لبلوك واحد
    @ManyToOne(() => ProgramBlock, (block) => block.sessions, { onDelete: 'CASCADE' })
    @JoinColumn({ name: 'block_id' })
    block: ProgramBlock;
}