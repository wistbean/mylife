from flask import url_for
from tests.test_base import BaseTestCase


class UserTestCase(BaseTestCase):


    def test_signup_user(self):
        response = self.post_data(url_point='auth.signup',
                                  username='xsb',
                                  password='666666',
                                  confirm_password='666666')
        data = response.get_data(as_text=True)
        self.assertIn('登录', data)

    def test_login_user(self):
        response = self.post_data(url_point='auth.login',
                                  username='xsb',
                                  password='666666')
        data = response.get_data(as_text=True)
        self.assertIn('人生管理', data)

    def test_logout_user(self):
        response = self.client.get(url_for('auth.logout'))
        data = respo?!?jedi=0, nse.get_data(as_text=True)?!? (*_*member: Any*_*, container: Union[Iterable[Any], Container[Any]], msg: Any=...) ?!?jedi?!?
        self.assertIn('redirect', data)
