import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { User } from './entities/user.entity';
import { PhysicalSnapshot } from './entities/physical-snapshot.entity';
import { KnowledgeDocument } from './entities/knowledge-document.entity';
import { Program } from './entities/program.entity';
import { ProgramBlock } from './entities/program-block.entity';
import { ProgramSession } from './entities/program-session.entity';
import { SessionExercise } from './entities/session-exercise.entity';
import { Enrollment } from './entities/enrollment.entity';
import { Post } from './entities/post.entity';
import { Follow } from './entities/follow.entity';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'postgres',
      password: 'rootpassword',
      database: 'ringside',
      // هنا بنرص كل الجداول عشان TypeORM يشوفها ويكريتها في الداتابيز
      entities: [
        User,
        PhysicalSnapshot,
        KnowledgeDocument,
        Program,
        ProgramBlock,
        ProgramSession,
        SessionExercise,
        Enrollment,
        Post,
        Follow
      ],
      synchronize: true, // هتكريت الجداول أوتوماتيك
    }),
  ],
  controllers: [],
  providers: [],
})
export class AppModule { }