# -*- coding:utf-8 -*-
__author__ = 'shisanjun'

import os,sys
import sqlalchemy
from  sqlalchemy  import Table,Column,String,Integer,Date,ForeignKey,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,mapper
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)
from src.connection import Connection


conn=Connection().create_connection()
engine=sqlalchemy.create_engine(conn,encoding="utf-8",echo=False)

BASE=declarative_base()

#班级和用户多对多关系　
classes_user=Table(
    "classes_user",
    BASE.metadata,
    Column("user_qq",String(32),ForeignKey("user.qq")),
    Column("classes_id",Integer,ForeignKey("classes.id"))
)

#上课记录和用户多对多关系
# record_user=Table(
#     "record_user",
#     BASE.metadata,
#     Column("id",Integer,primary_key=True),
#     Column("record_id",Integer,ForeignKey("record.id")),
#     Column("user_id",Integer,ForeignKey("user.id"))
# )

class Role(BASE):
    """
    角色表
    """
    __tablename__="role"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False,unique=True)

    def __repr__(self):
        return self.name

class RecordUser(BASE):
    __tablename__="record_user"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("user.id"))
    record_id=Column(Integer,ForeignKey("record.id"))

    user=relationship("User",backref="recorduser")
    record=relationship("Record",backref="recorduser")


class User(BASE):
    """
    用户表
    """
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False,unique=True)
    password=Column(String(32),nullable=False)
    qq=Column(String(32),nullable=False,unique=True)
    role_id=Column(Integer,ForeignKey("role.id"))

    role=relationship("Role",backref="user")
    classes=relationship("Classes",secondary=classes_user,backref="user")
    record=relationship("Record",secondary=RecordUser.__tablename__,backref="user")

    def __repr__(self):
        return "%s:%s" %(self.name,self.qq)

class Classes(BASE):
    """
    班级表
    """
    __tablename__="classes"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False,unique=True)

    def __repr__(self):
        return self.name

class Course(BASE):
    """
    课程表
    """
    __tablename__="course"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    classes_id=Column(Integer,ForeignKey("classes.id"))

    classes=relationship("Classes",backref="course")

    def __repr__(self):
        return self.name

class Record(BASE):
    """
    记录表
    """
    __tablename__="record"
    id=Column(Integer,primary_key=True)
    name=Column(String(32),nullable=False)
    task=Column(String(32))
    task_status=Column(Boolean,default=False)
    course_id=Column(Integer,ForeignKey("course.id"))

    course=relationship("Course",backref="record")

    def __repr__(self):
        return "record:%s task:%s" %(self.name,self.task)

class Score(BASE):
    """
    成绩表
    """
    __tablename__="score"
    id=Column(Integer,primary_key=True)
    number=Column(Integer,nullable=False)
    record_user_id=Column(Integer,ForeignKey("record_user.id"))

    record_user=relationship("RecordUser",backref="score")

    def __repr__(self):
        return self.number


BASE.metadata.create_all(engine)



