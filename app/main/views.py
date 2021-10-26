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
from flask import render_template
from flask_login import current_user, login_required
from app.main import main
from app.models import Plan


@main.route('/')
@login_required
def index():
    todolist = Plan.query.with_parent(current_user).order_by(
        Plan.create_at.desc()).limit(8)
    return render_template('index.html', todolist=todolist)
