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
import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_whooshee import Whooshee
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

from config import config


db = SQLAlchemy()
whooshee = Whooshee()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


migrate = Migrate()


# 工厂方法创建实例
def create_app(config_name='development'):
    # 加载配置
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # 注册插件
    register_extentions(app)
    # 注册蓝本
    register_blueprints(app)
    # 注册命令
    register_commands(app)
    return app


def register_extentions(app):
    db.init_app(app)
    whooshee.init_app(app)
    login_manager.init_app(app)
   # toolbar.init_app(app)
    migrate.init_app(app, db=db)



def register_blueprints(app):
    from .main import main
    app.register_blueprint(main)

    from .todo import todo
    app.register_blueprint(todo, url_prefix='/todo')

    from .auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

def register_commands(app):
    @app.cli.command()
    def initdb():
        db.drop_all()
        db.create_all()

    @app.cli.command()
    @click.option('--count', default=10, help='创建计划条目数量')
    def plan(count):
        from app.fakers import gen_faker_plan
        click.echo('正在生成中.....')
        gen_faker_plan(count)
        click.echo('生成完毕！')
