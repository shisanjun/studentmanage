# -*- coding:utf-8 -*-
__author__ = 'shisanjun'

import os,sys
import copy
import sqlalchemy
from  sqlalchemy.orm import sessionmaker
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)


from src.connection import Connection
from src.log import Log
from src.models import Role,User,Classes,Course,Record,Score,RecordUser
from src.fomatter import Fomatter

conn=Connection().create_connection()
engine=sqlalchemy.create_engine(conn,encoding="utf-8",echo=False)



session_class=sessionmaker(bind=engine)
session=session_class()
r1=Role(name="admin")
r2=Role(name="teacher")
r3=Role(name="student")

session.add_all([r1,r2,r3])
u1=User(name="admin",password="123456",qq="1",role_id=1)

u2=User(name="teacher",password="123456",qq="2",role_id=2)

u3=User(name="shisanjun",password="123456",qq="3",role_id=3)

session.add_all([u1,u2,u3])

session.commit()