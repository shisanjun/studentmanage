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

class Function(object):
    logger=Log().logger()
    conn=Connection().create_connection()
    engine=sqlalchemy.create_engine(conn,encoding="utf-8",echo=False)
    auth_dict={}
    def __init__(self):

        session_class=sessionmaker(bind=self.engine)
        self.session=session_class()
        self.format=Fomatter()


    def auth(self):
        """
        用户认证
        :return:
        """
        username=self.format.input_str_format("请输入用户名")
        password=self.format.input_str_format("请输入密码")
        user_obj=self.session.query(User).filter(User.name==username,User.password==password).first()
        if user_obj is None:
            self.auth_dict["username"]=username
            self.auth_dict["is_auth"]=False
            self.auth_dict["role"]=None
            self.auth_dict["user_id"]=None
            self.logger.debug("用户认证失败")
        else:
            self.auth_dict["username"]=username
            self.auth_dict["is_auth"]=True
            self.auth_dict["role"]=user_obj.role.name
            self.auth_dict["user_id"]=user_obj.id
            self.logger.debug("用户认证成功")
        return self.auth_dict


    def role_add(self,*args):
        """
        增加角色
        :param args:
        :return:
        """
        name=self.format.input_str_format("请输入角色名")
        role_obj=Role(name=name)
        try:
            self.session_add(role_obj)
            self.logger.debug("角色[%s]添加成功" %name)
        except:
            self.session.rollback()
            self.logger.error("角色[%s]已存在" %name)

    def role_update(self,*args):
        """
        角色更新
        :param args:
        :return:
        """
        name_old=self.format.input_str_format("请输入需要修改的角色名")
        role_obj=self.session.query(Role).filter_by(name=name_old).first()
        if role_obj is None:
            self.logger.info("角色名[%s]不存在！" %name_old)
        else:
            name_new=self.format.input_str_format("请输入需要修改新的角色名")
            role_obj.name=name_new
            self.session.commit()

    def role_list(self,*args):
        """
        所有角色列表
        :param args:
        :return:
        """
        role_objs=self.session.query(Role).all()
        if len(role_objs)==0:
             self.logger.info("角色表为空")
             return None
        else:
            self.format.show_color("序号\t角色名")
            for role_obj in role_objs:
                self.format.show_color("%s\t%s" %(role_obj.id,role_obj.name))
        return True

    def role_query(self,*args):
        """
        角色更新
        :param args:
        :return:
        """
        name=self.format.input_str_format("请输入查询角色名")
        role_objs=self.session.query(Role).filter(Role.name.like("%"+"%s"%name+"%")).all()
        if len(role_objs)==0:
             self.logger.info("角色表为空")
        else:
            self.format.show_color("序号\t角色名")
            for role_obj in role_objs:
                self.format.show_color("%s\t%s" %(role_obj.id,role_obj.name))


    def classes_add(self,*args):
        """
        增加班级
        :param args:
        :return:
        """
        name=self.format.input_str_format("请输入班级名")
        role_obj=Classes(name=name)
        try:
            self.session_add(role_obj)
            self.logger.debug("班级[%s]添加成功" %name)
        except:
            self.session.rollback()
            self.logger.error("班级[%s]已存在" %name)

    def classes_list(self,*args):
        """
        班级列表
        :param args:
        :return:
        """
        classes_objs=self.session.query(Classes).all()
        if len(classes_objs)==0:
             self.logger.info("班级表为空")
             return None
        else:
            self.format.show_color("序号\t班级名")
            for classes_obj in classes_objs:
                self.format.show_color("%s\t%s" %(classes_obj.id,classes_obj.name))
        return True

    def user_add(self,*args):
        """
        增加用户
        :param args:
        :return:
        """
        name=self.format.input_str_format("请输入用户名")
        password=self.format.input_str_format("请输入密码")
        qq=self.format.input_str_format("请输入QQ号")
        if self.role_list():
            role_id=self.format.input_str_format("请输入角色ID号")
            user_obj=User(name=name,password=password,qq=qq,role_id=role_id)
            try:
                self.session_add(user_obj)
                self.logger.debug("用户[%s]添加成功" %name)
            except:
                self.session.rollback()
                self.logger.error("用户名或者QQ已存在")

    def user_add_teacher(self,*args):
        """
        增加学员
        :param args:
        :return:
        """
        name=self.format.input_str_format("请输入用户名")
        password=self.format.input_str_format("请输入密码")
        qq=self.format.input_str_format("请输入QQ号")
        role_obj=self.session.query(Role).filter_by(name="student").first()

        user_obj=User(name=name,password=password,qq=qq,role_id=role_obj.id)
        try:
            self.session_add(user_obj)
            self.logger.debug("学员[%s]添加成功" %name)
        except:
            self.session.rollback()
            self.logger.error("学员名或者QQ已存在")

    def user_list(self,*args):
        """
        查看所有用户
        :param args:
        :return:
        """
        user_objs=self.session.query(User).all()
        if len(user_objs)==0:
             self.logger.info("用户表为空")
             return None
        else:
            self.format.show_color("序号\t姓名\tqq号\t角色")
            for user_obj in user_objs:
                self.format.show_color("%s\t%s\t%s\t\t%s" %(user_obj.id,user_obj.name,user_obj.qq,user_obj.role.name))
            return True

    def user_student_list(self,*args):
        """
        查看所有学员
        :param args:
        :return:
        """
        user_objs=self.session.query(User).filter(User.role_id.in_(self.session.query(Role.id).filter_by(name="student").first())).all()
        if len(user_objs)==0:
             self.logger.info("用户表为空")
             return None
        else:
            self.format.show_color("序号\t姓名\tqq号\t角色")
            for user_obj in user_objs:
                self.format.show_color("%s\t%s\t%s\t\t%s" %(user_obj.id,user_obj.name,user_obj.qq,user_obj.role.name))
            return True

    def class_user(self,*args):
        """
        学员分配班级
        :param args:
        :return:
        """
        if self.classes_list():
            class_id=self.format.input_str_format("请输入班级ID号")
            class_obj=self.session.query(Classes).filter_by(id=class_id).first()
            if self.user_list():
                qq=self.format.input_str_format("请输入学号QQ号")
                user_obj=self.session.query(User).filter_by(qq=qq).first()
                user_obj.classes=[class_obj]
                try:
                    self.session.commit()
                    self.logger.debug("学员QQ[%s]分配班级成功" %qq)
                except:
                    self.logger.error("学员已分配到此班级")

    def course_add(self,*args):
        """
        增加课程
        :param args:
        :return:
        """

        if self.classes_list():
            class_id=self.format.input_str_format("请输入班级ID号")
            try:
                name=self.format.input_str_format("请输入课程名")
                course_oj=Course(name=name,classes_id=class_id)

                self.session_add(course_oj)
                self.logger.debug("课程[%s]增加成功" %name)
            except:
                self.logger.error("你输入的班级号不存在!")

    def course_list(self,*args):
        """
        查看所有课程
        :param args:
        :return:
        """
        course_objs=self.session.query(Course).all()
        if len(course_objs)==0:
             self.logger.info("课程表为空")
             return None
        else:
            self.format.show_color("序号\t课程名\t班级名")
            for course_obj in course_objs:
                self.format.show_color("%s\t%s\t%s" %(course_obj.id,course_obj.name,course_obj.classes.name))
        return True

    def record_add(self,*args):
        """
        增加上课记录
        :param args:
        :return:
        """

        if self.course_list():
            course_id=self.format.input_str_format("请输入课程ID号")
            try:
                name=self.format.input_str_format("请输入上课记录名")
                taskname=self.format.input_str_format("请输入上课作业要求")
                record_oj=Record(name=name,task=taskname,course_id=course_id)
                self.session_add(record_oj)
                self.logger.debug("上课记录[%s]增加成功" %name)
            except:
                self.logger.error("你输入的课程号不存在!")

    def record_list(self,*args):
        """
        所有课程记录
        :param args:
        :return:
        """
        record_objs=self.session.query(Record).all()
        if len(record_objs)==0:
             self.logger.info("上课记录表为空")
             return None
        else:
            self.format.show_color("序号\t\t上课记录\t\t上课作业\t课程名\t\t班级名")
            for record_obj in record_objs:
                self.format.show_color("%s\t%s\t%s\t%s\t%s" \
                %(record_obj.id,record_obj.name,record_obj.task,record_obj.course.name,record_obj.course.classes.name))
        return True

    def record_user_add(self,*args):
        """
        学员上课记录
        :param args:
        :return:
        """
        if self.record_list():
            record_id=self.format.input_str_format("请输入上课程记录ID号")
            record_obj=self.session.query(Record).filter_by(id=record_id).first()
            if self.user_list():
                user_id=self.format.input_str_format("请输入学员ID号")
                user_obj=self.session.query(User).filter_by(id=user_id).first()
                record_user_obj=RecordUser(user_id=user_id,record_id=record_id)
                self.session_add(record_user_obj)

    def record_user_list(self,*args):
        """
        查看所有学员上课记录
        :param args:
        :return:
        """
        record_user_objs=self.session.query(RecordUser).all()
        if len(record_user_objs)==0:
             self.logger.info("上课记录和用户关系表为空")
             return None
        else:
            self.format.show_color("序号\t课程\t上课记录\t作业\t上课学员")
            for record_user_obj in record_user_objs:
                user_obj=self.session.query(User).filter_by(id=record_user_obj.user_id).first()
                record_obj=self.session.query(Record).filter_by(id=record_user_obj.record_id).first()
                self.format.show_color("%s\t%s\t%s\t%s\t%s" \
                %(record_user_obj.id,record_obj.course.name,record_obj.name,record_obj.task,user_obj.name))
            return True

    def sumbit_user_record(self,*args):
        """
        提交作业
        :param args:
        :return:
        """
        userid=args[0]
        record_user_objs=self.session.query(RecordUser).filter(RecordUser.user_id==userid,RecordUser.record_id.in_(self.session.query(Record.id).filter_by(task_status=0))).all()
        if len(record_user_objs)==0:
            self.logger.error("用户没有需要上交的作业")
            return

        record_user_ids=[]
        for record_user_obj in record_user_objs:
            record_user_ids.append("%s"%record_user_obj.id)
            self.format.show_color("%s\t%s\t%s\t%s\t%s" \
             %(record_user_obj.id,record_user_obj.record.course.classes.name,\
               record_user_obj.record.course.name,record_user_obj.record.name,
               record_user_obj.record.task ))

        while True:
            record_user_id=self.format.input_str_format("请输入作业ID号")
            if record_user_id not in record_user_ids:
                continue
            else:break

        is_ok=self.format.input_str_format("是否提交作业Y/N")
        if is_ok=="Y":
            record_obj=self.session.query(Record).filter(Record.id==self.session.query(RecordUser.record_id).filter(RecordUser.id==record_user_id)).first()
            record_obj.task_status=1
            self.logger.debug("[%s]提交作业成功" %userid)


    def score_add(self,*args):
        """
        审批作业
        :param args:
        :return:
        """
        if self.record_user_list():
            record_user_id=self.format.input_str_format("请输入作业ID号")
            score_num=self.format.input_str_format("请输入成绩")
            try:
                score_obj=Score(number=score_num,record_user_id=record_user_id)
                self.session_add(score_obj)
                self.logger.debug("审批作业成功")
            except:
                self.logger.error("你输入的作业号不存在!")

    def score_query(self,*args):
        """
        查询成绩
        :param args:
        :return:
        """
        userid=args[0]
        score_objs=self.session.query(RecordUser).filter_by(user_id=userid).all()
        if len(score_objs)==0:
            self.logger.error("用户成绩不存在!")
            return
        try:
            for score_obj  in score_objs:
                 self.format.show_color("%s\t%s\t%s\t%s\t%s\t%s" \
                 %(score_obj.id,score_obj.record.course.classes.name,\
                   score_obj.record.course.name,score_obj.record.name,
                   score_obj.record.task,score_obj.score[0].number ))
        except:
            self.logger.error("用户成绩不存在!")

    def score_list(self,*args):
        """
        所有成绩列表
        :param args:
        :return:
        """
        score_objs=self.session.query(RecordUser).all()
        if len(score_objs)==0:
            self.logger.error("用户[%s]成绩不存在!" %(score_objs.user.name))
            return
        self.format.show_color("班级\t学员\t课程名\t上课记录\t作业名\t成绩")
        for score_obj  in score_objs:
            self.format.show_color("%s\t%s\t%s\t%s\t%s\t%s" \
            %(score_obj.user.classes[0].name,score_obj.user.name,score_obj.record.course.name,score_obj.record.name,score_obj.record.task,score_obj.score[0].number))


    def sum_score_list(self,*args):
        """
        成绩排名
        :param args:
        :return:
        """
        userid=args[0]
        user_objs=(self.session.query(User).filter_by(id=userid).first())
        self.format.show_color("班级\t用户\t总成绩\t排名")
        for class_obj in user_objs.classes:
            user_objs=self.session.query(Classes).filter(Classes.id==class_obj.id).first()
            if len(user_objs.user)==0:
                return
            score_sorted=[]
            for user_obj in user_objs.user:
                record_user_objs=self.session.query(RecordUser).filter(RecordUser.user_id==user_obj.id).all()
                nums=[]
                for record_user_obj in record_user_objs:
                    for score_obj in record_user_obj.score:
                        nums.append(copy.deepcopy(score_obj.number))
                score_sorted.append((user_obj.name,sum(nums)))

            new_scored=sorted(score_sorted,key=lambda score:score[1])

            new_scored.reverse()
            for score_tmp in range(len(new_scored)):
                self.format.show_color("%s\t%s\t%s\t%s" %(class_obj.name,new_scored[score_tmp][0],new_scored[score_tmp][1],score_tmp+1))


    def session_add(self,data):
        if type(data)=="list":
            self.session.add_all(data)
        else:
            self.session.add(data)
        self.session.commit()

