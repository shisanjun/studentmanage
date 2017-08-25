# -*- coding:utf-8 -*-
__author__ = 'shisanjun'

import os,sys
#获取父级目录
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#父级目录加入系统环境
sys.path.append(BASE_DIR)

from src.interactive import Interactive

if __name__=="__main__":
    Interactive()
