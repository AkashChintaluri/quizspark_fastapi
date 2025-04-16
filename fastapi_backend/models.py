from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, TIMESTAMP, JSON, DateTime
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

class StudentLogin(Base):
    __tablename__ = "student_login"
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

class TeacherLogin(Base):
    __tablename__ = "teacher_login"
    
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

class Quizzes(Base):
    __tablename__ = "quizzes"
    
    quiz_id = Column(Integer, primary_key=True, nullable=False)
    quiz_name = Column(String(255), nullable=False)
    quiz_code = Column(String(50), nullable=False)
    created_by = Column(Integer, ForeignKey("teacher_login.id"), nullable=False)
    questions = Column(JSON, nullable=False)
    due_date = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, nullable=False, server_default=text('now()'))

class QuizAttempts(Base):
    __tablename__ = "quiz_attempts"
    
    attempt_id = Column(Integer, primary_key=True, nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.quiz_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("student_login.id"), nullable=False)
    attempt_date = Column(TIMESTAMP, server_default=text('now()'))
    score = Column(Integer)
    total_questions = Column(Integer)
    time_taken = Column(Integer)
    is_completed = Column(Boolean, default=False)
    answers = Column(JSON)

class Subscriptions(Base):
    __tablename__ = "subscriptions"
    
    student_id = Column(Integer, ForeignKey("student_login.id"), primary_key=True)
    teacher_id = Column(Integer, ForeignKey("teacher_login.id"), primary_key=True)
    subscribed_at = Column(TIMESTAMP, server_default=text('now()'))

class RetestRequests(Base):
    __tablename__ = "retest_requests"
    
    request_id = Column(Integer, primary_key=True, nullable=False)
    student_id = Column(Integer, ForeignKey("student_login.id"), nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.quiz_id"), nullable=False)
    attempt_id = Column(Integer, ForeignKey("quiz_attempts.attempt_id"), nullable=False)
    request_date = Column(TIMESTAMP, server_default=text('now()'))
    status = Column(String(20), default='pending')
    updated_at = Column(DateTime(timezone=True)) 