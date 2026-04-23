import { Entity, PrimaryGeneratedColumn, ManyToOne, JoinColumn } from 'typeorm';
import { User } from './user.entity';

@Entity('follows')
export class Follow {
    @PrimaryGeneratedColumn('uuid')
    id: string;

    @ManyToOne(() => User)
    @JoinColumn({ name: 'follower_id' })
    follower: User;

    @ManyToOne(() => User)
    @JoinColumn({ name: 'followee_id' })
    followee: User;
}