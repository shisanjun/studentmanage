# -*- coding:utf-8 -*-
__author__ = 'shisanjun'

import os,sys
import sqlalchemy
from  sqlalchemy.orm import sessionmaker
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)

from src.function import Function
from src.fomatter import Fomatter
class Interactive(object):

    def __init__(self):
        self.func_obj=Function()
        self.fomatter_obj=Fomatter
        self.interaction()

    def interaction(self):
        teacher_print="""
        --------------------讲师界面-----------------------------
        0:退出                        1.增加班级
        2.查看班级                     3.增加学员
        4.查看学员                     5.学员分配班级
        6.增加课程                     7.查看课程
        8.增加课程记录                 9.查看课程记录
        10.增加学员上课记录和作业       11.查看学员上课程记录和作业
        12.审批学员成绩                13.查看学员成绩
        """

        admin_print="""
        --------------------管理员界面-----------------------------
        0:退出                        1.增加班级
        2.查看班级                     3.增加学员
        4.查看学员                     5.学员分配班级
        6.增加课程                     7.查看课程
        8.增加课程记录                 9.查看课程记录
        10.增加学员上课记录和作业       11.查看学员上课程记录和作业
        12.审批学员成绩                13.查看学员成绩
        14.增加角色                    15.查看角色
        """

        student_print="""
        --------------------学生界面-----------------------------
        0:退出 　　　　1.提交作业　　　　　2.查看成绩　　　3.班级成绩总分排名
        """

        teacher_menu={
            "0":exit,
            "1":self.func_obj.classes_add,
            "2":self.func_obj.classes_list,
            "3":self.func_obj.user_add_teacher,
            "4":self.func_obj.user_student_list,
            "5":self.func_obj.class_user,
            "6":self.func_obj.course_add,
            "7":self.func_obj.course_list,
            "8":self.func_obj.record_add,
            "9":self.func_obj.record_list,
            "10":self.func_obj.record_user_add,
            "11":self.func_obj.record_user_list,
            "12":self.func_obj.score_add,
            "13":self.func_obj.score_list,
        }
        admin_menu={
            "0":exit,
            "1":self.func_obj.classes_add,
            "2":self.func_obj.classes_list,
            "3":self.func_obj.user_add,
            "4":self.func_obj.user_list,
            "5":self.func_obj.class_user,
            "6":self.func_obj.course_add,
            "7":self.func_obj.course_list,
            "8":self.func_obj.record_add,
            "9":self.func_obj.record_list,
            "10":self.func_obj.record_user_add,
            "11":self.func_obj.record_user_list,
            "12":self.func_obj.score_add,
            "13":self.func_obj.score_list,
            "14":self.func_obj.role_add,
            "15":self.func_obj.role_list,
        }

        student_menu={
            "0":exit,
            "1":self.func_obj.sumbit_user_record,
            "2":self.func_obj.score_query,
            "3":self.func_obj.sum_score_list
        }

        is_login=self.func_obj.auth()
        if is_login.get("is_auth"):
            if is_login.get("role")=="admin":
                print_str=admin_print
                menu_func=admin_menu
            elif is_login.get("role")=="teacher":
                print_str=teacher_print
                menu_func=teacher_menu
            elif is_login.get("role")=="student":
                print_str=student_print
                menu_func=student_menu
            else:
                return

            print(print_str)
            while True:
                num=input("请选择功能>>")
                if len(num)==0 or num not in menu_func:
                     continue
                else:
                    menu_func[num](is_login.get("user_id"))


Interactive()