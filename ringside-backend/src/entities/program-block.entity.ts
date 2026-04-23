import { Entity, PrimaryGeneratedColumn, Column, ManyToOne, OneToMany, JoinColumn } from 'typeorm';
import { Program } from './program.entity';
import { ProgramSession } from './program-session.entity';

@Entity('program_blocks')
export class ProgramBlock {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @Column()
    name: string; // e.g., 'Accumulation Phase'

    @Column()
    order_index: number;

    // البلوك بينتمي لبرنامج واحد
    @ManyToOne(() => Program, (program) => program.blocks, { onDelete: 'CASCADE' })
    @JoinColumn({ name: 'program_id' })
    program: Program;

    // البلوك الواحد جواه كذا سيشن
    @OneToMany(() => ProgramSession, (session) => session.block)
    sessions: ProgramSession[];
}