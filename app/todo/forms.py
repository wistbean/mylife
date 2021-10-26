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
from wtforms.validators import DataRequired, Length


class TodoListForm(FlaskForm):
    todo = StringField('todo', validators=[DataRequired()])


class TodoForm(FlaskForm):
    todo = StringField('todo', validators=[DataRequired()])
