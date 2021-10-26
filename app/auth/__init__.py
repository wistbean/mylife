from flask import Blueprint

# 蓝本创建
auth = Blueprint('auth', __name__)

from . import views


