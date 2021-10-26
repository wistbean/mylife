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
from flask import render_template, session, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required

from app.auth import auth
from app.auth.forms import SignupForm, LoginForm
from app.models import User


@auth.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data)
        new_user.set_password(form.password.data)
        new_user.add()
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        remember_pwd = login_form.remember_pwd.data

        user = User.query.filter_by(username=username).first()

        if user:
            if username == user.username and user.check_password(password):
                # 登录
                if remember_pwd:
                    login_user(user, remember=True)
                else:
                    login_user(user)
                return render_template('index.html', title='个人管理系统', username=username)
            else:
                # 用户名或密码不正确
                return render_template('login.html', form=login_form, errormsg='用户名或密码不正确')
        else:
            return render_template('login.html', form=login_form, errormsg='用户不存在')

    return render_template('login.html', form=login_form)


@auth.route('logout')
def logout():
    logout_user()
    return redirect('auth.login')
