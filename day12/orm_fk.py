# -*- coding:utf-8 -*-
# Author:caiqinxiong
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,DATE,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
engine = create_engine("mysql+pymysql://root:root@172.16.219.139/python?charset=utf8",
                       encoding='utf-8', echo=True) #  ?charset=utf8 支持中文

Base = declarative_base()  # 生成orm基类

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)
    name = Column(String(32),nullable=False)
    register_date = Column(DATE,nullable=False)

    def __repr__(self):
        return " < %s name='%s >" % (
            self.id, self.name)

class StudyRecode(Base):
    __tablename__ = "study_recode"
    id = Column(Integer,primary_key=True)
    day = Column(Integer,nullable=False)
    status = Column(String(32),nullable=False)
    stu_id = Column(Integer,ForeignKey('student.id'))
    student = relationship("Student", backref="my_study_recode") #这个nb，允许你在user表里通过backref字段反向查出所有它在addresses表里的关联项

    def __repr__(self):
        return "<%s day: %s status: %s>" % (
            self.student.name, self.day,self.status)

Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
session = Session_class()  # 生成session实例
s1 = Student(name='caiqinxiong',register_date = '2018-08-19')
s2 = Student(name='lixiaoxin',register_date = '2018-08-20')
s3 = Student(name='jack',register_date = '2018-08-21')
s4 = Student(name='蔡亲雄',register_date = '2018-08-22')

study_obj1 = StudyRecode(day = 1,status = 'YES',stu_id = 1)
study_obj2 = StudyRecode(day = 2,status = 'NO',stu_id = 1)
study_obj3 = StudyRecode(day = 3,status = 'YES',stu_id = 1)
study_obj4 = StudyRecode(day = 1,status = 'YES',stu_id = 2)

session.add_all([s1,s2,s3,s4,study_obj1,study_obj2,study_obj3,study_obj4])

stu_obj = session.query(Student).filter(Student.name=='caiqinxiong').first()
print(stu_obj.my_study_recode)
session.commit()













