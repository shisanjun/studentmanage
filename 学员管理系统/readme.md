#作业12

##本节作业


###作业：学员管理系统
####要求：
	用户角色，讲师＼学员， 用户登陆后根据角色不同，能做的事情不同，分别如下
	讲师视图
		管理班级，可创建班级，根据学员qq号把学员加入班级
		可创建指定班级的上课纪录，注意一节上课纪录对应多条学员的上课纪录， 即每节课都有整班学员上， 为了纪录每位学员的学习成绩，需在创建每节上课纪录是，同时为这个班的每位学员创建一条上课纪录
		为学员批改成绩， 一条一条的手动修改成绩
	学员视图
		提交作业
		查看作业成绩
		一个学员可以同时属于多个班级，就像报了Linux的同时也可以报名Python一样， 所以提交作业时需先选择班级，再选择具体上课的节数
		附加：学员可以查看自己的班级成绩排名

##博客地址:
	数据库--mysql介绍 http://www.cnblogs.com/lixiang1013/p/7290372.html
	数据库-mysql安装 http://www.cnblogs.com/lixiang1013/p/7290384.html
	数据库-mysql管理 http://www.cnblogs.com/lixiang1013/p/7290403.html
	数据库-mysql数据类型 http://www.cnblogs.com/lixiang1013/p/7290409.html
	数据库-mysql数据库和表操作 http://www.cnblogs.com/lixiang1013/p/7290443.html
	数据库-mysql数据操作 http://www.cnblogs.com/lixiang1013/p/7290794.html
	数据库-mysql数据连接 http://www.cnblogs.com/lixiang1013/p/7291581.html
	数据库-mysql事务 http://www.cnblogs.com/lixiang1013/p/7291661.html
	数据库-mysql索引 http://www.cnblogs.com/lixiang1013/p/7294002.html
	数据库-mysql视图 http://www.cnblogs.com/lixiang1013/p/7294040.html
	数据库-mysql触发器 http://www.cnblogs.com/lixiang1013/p/7294090.html
	数据库-mysql储存过程 http://www.cnblogs.com/lixiang1013/p/7294207.html
	数据库-mysql函数 http://www.cnblogs.com/lixiang1013/p/7294724.html
	数据库-mysql中文显示问题 http://www.cnblogs.com/lixiang1013/p/7294732.html

	数据库-python操作mysql(pymsql) http://www.cnblogs.com/lixiang1013/p/7294730.html

	ORM介绍 http://www.cnblogs.com/lixiang1013/p/7375589.html
	SQLAlchemy-介绍安装 http://www.cnblogs.com/lixiang1013/p/7375796.html
	SQLAlchemy-方言(Dialects) http://www.cnblogs.com/lixiang1013/p/7380251.html
	SQLAlchemy-对象关系教程ORM-create http://www.cnblogs.com/lixiang1013/p/7382215.html
	SQLAlchemy-对象关系教程ORM-query http://www.cnblogs.com/lixiang1013/p/7384126.html
	SQLAlchemy-对象关系教程ORM-一对多（外键)，一对一，多对多 http://www.cnblogs.com/lixiang1013/p/7392109.html
	SQLAlchemy-对象关系教程ORM-连接，子查询 http://www.cnblogs.com/lixiang1013/p/7397878.html

SELECT版FTP

##程序结构
	├── studentmanage          程序目录
	│ ├── bin					运行目录
	│ │ ├── __init__.py
	│ │ └── start.py			运行程序
	│ ├── conf					配置目录
	│ │ ├── __init__.py
	│ │ └── settings.py			配置文件
	│ ├── __init__.py
	│ ├── log					日志目录
	│ │ ├── __init__.py
	│ │ └── studentmanage.log	日志文件
	│ └── src					代码目录
	│     ├── connection.py		连接程序
	│     ├── fomatter.py		格式化程序
	│     ├── function.py		功能程序
	│     ├── __init__.py
	│     ├── init_table_data.py 初始化数据
	│     ├── interactive.py	交互程序
	│     ├── log.py			日志程序
	│     ├── models.py			ORM程序
	│     ├── mysql.txt



###1. 程序说明
	用户角色，讲师＼学员， 用户登陆后根据角色不同，能做的事情不同，分别如下
	讲师视图
		管理班级，可创建班级，根据学员qq号把学员加入班级
		可创建指定班级的上课纪录，注意一节上课纪录对应多条学员的上课纪录，
		即每节课都有整班学员上， 为了纪录每位学员的学习成绩，需在创建每节上课纪录是，
		同时为这个班的每位学员创建一条上课纪录
		为学员批改成绩， 一条一条的手动修改成绩
	学员视图
		提交作业
		查看作业成绩
		一个学员可以同时属于多个班级，就像报了Linux的同时也可以报名Python一样， 
		所以提交作业时需先选择班级，再选择具体上课的节数
		附加：学员可以查看自己的班级成绩排名

###2. 测试用例

        账号1：admin 密码:123456
        账号2：teacher 密码:123456
		账号2：shisanjun 密码:123456

###3. 程序测试

		1) 在mysql数据库服务器上创建数据库
			create database studentmanage charset=utf8;
			commit;
		2）初始表结构
			python DAY12-李祥-学员管理系统/bin/studentmanage/src/models.py
		3) 初始用户数据
			python DAY12-李祥-学员管理系统/bin/studentmanage/src/init_table_data.py
		4) 系统使用
			python DAY12-李祥-学员管理系统/bin/studentmanage/bin/start.py

###4. 测试结果

####1）管理员测试
	请输入用户名>>admin
	请输入密码>>123456
	
	        --------------------管理员界面-----------------------------
	        0:退出                        1.增加班级
	        2.查看班级                     3.增加学员
	        4.查看学员                     5.学员分配班级
	        6.增加课程                     7.查看课程
	        8.增加课程记录                 9.查看课程记录
	        10.增加学员上课记录和作业       11.查看学员上课程记录和作业
	        12.审批学员成绩                13.查看学员成绩
	        14.增加角色                    15.查看角色
	        
	请选择功能>>15
	序号	角色名
	1	admin
	2	teacher
	3	student
	请选择功能>>4
	序号	姓名	qq号	角色
	1	admin	1		admin
	2	teacher	2		teacher
	3	shisanjun	3		student
	4	tianshi	4		student
***

####2）讲师测试
	请输入用户名>>teacher
	请输入密码>>123456

        --------------------讲师界面-----------------------------
        0:退出                        1.增加班级
        2.查看班级                     3.增加学员
        4.查看学员                     5.学员分配班级
        6.增加课程                     7.查看课程
        8.增加课程记录                 9.查看课程记录
        10.增加学员上课记录和作业       11.查看学员上课程记录和作业
        12.审批学员成绩                13.查看学员成绩
        
	请选择功能>>1
	请输入班级名>>linux学习班
	请选择功能>>1
	请输入班级名>>python学习班
	请选择功能>>1
	请输入班级名>>go学习班
	请选择功能>>2
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请选择功能>>4
	序号	姓名	qq号	角色
	3	shisanjun	3		student
	请选择功能>>3
	请输入用户名>>tianshi
	请输入密码>>123456
	请输入QQ号>>4
	请选择功能>>4
	序号	姓名	qq号	角色
	3	shisanjun	3		student
	4	tianshi	4		student
	请选择功能>>5
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>1
	序号	姓名	qq号	角色
	1	admin	1		admin
	2	teacher	2		teacher
	3	shisanjun	3		student
	4	tianshi	4		student
	请输入学号QQ号>>3
	请选择功能>>5
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>1
	序号	姓名	qq号	角色
	1	admin	1		admin
	2	teacher	2		teacher
	3	shisanjun	3		student
	4	tianshi	4		student
	请输入学号QQ号>>4
	请选择功能>>5
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>2
	序号	姓名	qq号	角色
	1	admin	1		admin
	2	teacher	2		teacher
	3	shisanjun	3		student
	4	tianshi	4		student
	请输入学号QQ号>>3
	请选择功能>>5
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>2
	序号	姓名	qq号	角色
	1	admin	1		admin
	2	teacher	2		teacher
	3	shisanjun	3		student
	4	tianshi	4		student
	请输入学号QQ号>>4
	请选择功能>>4
	序号	姓名	qq号	角色
	3	shisanjun	3		student
	4	tianshi	4		student
	请选择功能>>6
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>1
	请输入课程名>>linux基础课
	请选择功能>>6
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>1
	请输入课程名>>linux高级课
	请选择功能>>6
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>2
	请输入课程名>>python基础课
	请选择功能>>6
	序号	班级名
	1	linux学习班
	2	python学习班
	3	go学习班
	请输入班级ID号>>2
	请输入课程名>>python高级课
	请选择功能>>7
	序号	课程名	班级名
	1	linux基础课	linux学习班
	2	linux高级课	linux学习班
	3	python基础课	python学习班
	4	python高级课	python学习班
	请选择功能>>8
	序号	课程名	班级名
	1	linux基础课	linux学习班
	2	linux高级课	linux学习班
	3	python基础课	python学习班
	4	python高级课	python学习班
	请输入课程ID号>>1
	请输入上课记录名>>第一天
	请输入上课作业要求>>用户作业
	请选择功能>>8
	序号	课程名	班级名
	1	linux基础课	linux学习班
	2	linux高级课	linux学习班
	3	python基础课	python学习班
	4	python高级课	python学习班
	请输入课程ID号>>1
	请输入上课记录名>>第二天
	请输入上课作业要求>>用户组作业
	请选择功能>>8
	序号	课程名	班级名
	1	linux基础课	linux学习班
	2	linux高级课	linux学习班
	3	python基础课	python学习班
	4	python高级课	python学习班
	请输入课程ID号>>3
	请输入上课记录名>>第一天
	请输入上课作业要求>>python语法
	请选择功能>>8
	序号	课程名	班级名
	1	linux基础课	linux学习班
	2	linux高级课	linux学习班
	3	python基础课	python学习班
	4	python高级课	python学习班
	请输入课程ID号>>3
	请输入上课记录名>>第二天
	请输入上课作业要求>>python判断作业
	请选择功能>>10
	序号		上课记录		上课作业	课程名		班级名
	1	第一天	用户作业	linux基础课	linux学习班
	2	第二天	用户组作业	linux基础课	linux学习班
	3	第一天	python语法	python基础课	python学习班
	4	第二天	python判断作业	python基础课	python学习班
	请选择功能>>13
	班级	学员	课程名	上课记录	作业名	成绩
	python学习班	shisanjun	linux基础课	第一天	用户作业	90
	python学习班	tianshi	linux基础课	第一天	用户作业	85
	python学习班	shisanjun	linux基础课	第二天	用户组作业	90
	python学习班	tianshi	linux基础课	第二天	用户组作业	85
	python学习班	shisanjun	python基础课	第一天	python语法	90
	python学习班	tianshi	python基础课	第一天	python语法	85
	python学习班	shisanjun	python基础课	第二天	python判断作业	90
	python学习班	tianshi	python基础课	第二天	python判断作业	85
	

####3)学员测试
	请输入用户名>>shisanjun
	请输入密码>>123456
	
	        --------------------学生界面-----------------------------
	        0:退出 　　　　1.提交作业　　　　　2.查看成绩　　　3.班级成绩总分排名
	        
	请选择功能>>1
	请选择功能>>2017-08-22 15:47:35,636 ERROR function.py 用户没有需要上交的作业
	2
	2017-08-22 15:47:37,878 ERROR function.py 用户成绩不存在!
	请选择功能>>3
	班级	用户	总成绩	排名
	python学习班	tianshi	0	1
	python学习班	shisanjun	0	2
***
	请输入用户名>>shisanjun
	请输入密码>>123456
	
	        --------------------学生界面-----------------------------
	        0:退出 　　　　1.提交作业　　　　　2.查看成绩　　　3.班级成绩总分排名
	        
	请选择功能>>1
	请选择功能>>2017-08-22 15:51:55,317 ERROR function.py 用户没有需要上交的作业
	2
	1	linux学习班	linux基础课	第一天	用户作业	90
	3	linux学习班	linux基础课	第二天	用户组作业	90
	5	python学习班	python基础课	第一天	python语法	90
	7	python学习班	python基础课	第二天	python判断作业	90
	请选择功能>>3
	班级	用户	总成绩	排名
	python学习班	shisanjun	360	1
	python学习班	tianshi	340	2