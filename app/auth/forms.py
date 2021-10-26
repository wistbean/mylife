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
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, \
    BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class SignupForm(FlaskForm):
    """注册验证表单"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[
        DataRequired(),
        Length(6, 100),
        EqualTo('password_confirm', message='密码必须一致')])
    password_confirm = PasswordField(
        'password_confirm', validators=[DataRequired()])
    submit = SubmitField('注册一波')


class LoginForm(FlaskForm):
    """登录验证表单"""

    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_pwd = BooleanField('要记住密码不？')
    login = SubmitField('登录')
