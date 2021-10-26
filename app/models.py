# -*- coding: utf-8 -*-
################################################################
# 作者：小帅b                                                  #
#                                                              #
# 网站 : https://vip.fxxkpython.com                            #
#                                                              #
# 公众号：fxxkpython                                           #
#                                                              #
#                                                              #
# 声明:                                                        #
# 本项目为小帅b的VIP教程之一，仅供学员学习，禁止商用           #
#                                                              #
################################################################
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from app import db, whooshee, login_manager


class BaseModel:
    def commit(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()

    def add(self):
        db.session.add(self)
        self.commit()
        return self.id

    def delete(self):
        db.session.delete(self)
        self.commit()


class User(db.Model, UserMixin, BaseModel):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    hash_password = db.Column(db.String(120), nullable=False)

    plans = db.relationship("Plan", backref="user", lazy="dynamic")

    def set_password(self, password):
        self.hash_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash_password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@whooshee.register_model('body')
class Plan(db.Model, BaseModel):
    __tablename__ = 'plan'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    create_at = db.Column(db.DateTime, index=True, default=datetime.now)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    sub_plans = db.relationship("SubPlan", lazy="dynamic")

    @property
    def get_subplan_done_count(self):
        return self.sub_plans.filter_by(is_done=True).count()

    @property
    def get_all_subplan_count(self):
        return self.sub_plans.count()

    @property
    def get_done_percent(self):
        try:
            return round((self.get_subplan_done_count/self.get_all_subplan_count), 2) * 100
        except:
            return 0


class SubPlan(db.Model, BaseModel):
    __tablename__ = 'sub_plan'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default=datetime.now)
    finish_time = db.Column(db.DateTime)
    is_done = db.Column(db.Boolean, default=False)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    plan_id = db.Column(db.Integer, db.ForeignKey("plan.id"))

    # 关联删除
    plan = db.relationship('Plan', cascade='delete', overlaps="sub_plans")

    def change_status(self):
        if self.is_done is True:
            self.is_done = False
        else:
            self.is_done = True
            self.finish_time = datetime.now()

        self.add()
