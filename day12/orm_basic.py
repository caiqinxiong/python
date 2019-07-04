# -*- coding:utf-8 -*-
# Author:caiqinxiong
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine = create_engine("mysql+pymysql://root:root@172.16.219.139/cai",
                       encoding='utf-8')#, echo=True)

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (
            self.name, self.password)

Base.metadata.create_all(engine)  # 创建表结构

Session_class = sessionmaker(bind=engine)  # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session = Session_class()  # 生成session实例

# user_obj = User(name="lixiaoxin", password="123")  # 生成你要创建的数据对象
# user_obj2 = User(name="caiqinxiong", password="123")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# Session.add(user_obj2)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建

Session.commit()  # 现此才统一提交，创建数据

# 查询
my_user = Session.query(User).filter_by(name="lixiaoxin").first()
print(my_user) # sqlalchemy帮你把返回的数据映射成一个对象，这样你调用每个字段就可以跟调用对象属性一样
print(my_user.id,my_user.name,my_user.password)

# 修改
# my_user = Session.query(User).filter_by(name="caiqinxiong").first()
#
# my_user.name = "caiqinxiong_cai"
#
# Session.commit()

# 回滚
my_user = Session.query(User).filter_by(id=1).first()
my_user.name = "Jack"

fake_user = User(name='Rain', password='12345')
Session.add(fake_user)

print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 这时看session里有你刚添加和修改的数据

Session.rollback()  # 此时你rollback一下

print(Session.query(User).filter(User.name.in_(['Jack', 'rain'])).all())  # 再查就发现刚才添加的数据没有了。

# Session
# Session.commit()

print(Session.query(User.name,User.id).all() )

# 多条件查询
objs = Session.query(User).filter(User.id>0).filter(User.id<7).all()
# 上面2个filter的关系相当于 user.id >1 AND user.id <7 的效果

# 统计和分组

Session.query(User).filter(User.name.like("Ra%")).count()

# 分组

from sqlalchemy import func
print(Session.query(func.count(User.name),User.name).group_by(User.name).all() )