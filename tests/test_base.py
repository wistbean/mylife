from flask import url_for, current_app
import unittest
from app import create_app, db
from app.models import User


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        # 获取测试 app 对象
        app = create_app('testing')
        # 获取上下文环境
        self.context = app.test_request_context()
        self.context.push()
        # 获取测试用户
        self.client = app.test_client()
        # 创建数据库
        db.create_all()


    def tearDown(self):
        # 清除测试数据库
        db.drop_all()
        # 移除上下文
        self.context.pop()

    def post_data(self, url_point, **data):
        response = self.client.post(
            url_for(url_point),
            data=data
        )
        return response


    def test_app_exists(self):
        self.assertTrue(current_app is not None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
