import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn, ManyToOne } from 'typeorm';
import { User } from './user.entity';

@Entity('posts')
export class Post {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @ManyToOne(() => User)
    user: User;

    @Column({ type: 'text' })
    content: string;

    @Column({ nullable: true })
    image_path: string;

    @Column({ default: false })
    is_system_generated: boolean;

    @CreateDateColumn()
    created_at: Date;
}