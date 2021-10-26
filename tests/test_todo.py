import unittest

from flask import url_for

from app import create_app, db
from app.models import User, Plan, SubPlan



class TodoTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('testing')
        self.app_context = app.test_request_context()
        self.app_context.push()
        db.create_all()
        self.client = app.test_client()

        test_user = User(username='xsb')
        test_user.set_password('666666')
        
        plan = Plan()
        
        db.session.add(test_user)
        db.session.commit()

        self.client.post(url_for('auth.login'), data={'username':'xsb', 'password':'666666'})

    def tearDown(self):
        db.drop_all()
        self.app_context.pop()

    def test_add_todolist(self):
        response = self.client.post(url_for('todo.add_todolist'), data={'body':'我的第一个大计划'})
        data = response.get_data(as_text=True)
        self.assertIn('人生管理', data)

    def test_add_todo(self):
        response = self.client.post(url_for('todo.add_todo', plan_id=1), data={'body':'我是小计划'})
        data = response.get_data(as_text=True)
        self.assertIn('<div class', data)



