import os

def create_Mysql_uri(usernmae, password, host, port, database):
    db_url = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        usernmae, password, host, port, database)
    return db_url

class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'zheshimiyao')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    WTF_I18n_ENABLED = False
    # 全文搜索
    WHOOSHEE_MIN_STRING_LEN = 0

class DevConfig(BaseConfig):
    DEBUG = True
    DEBUG_TB_PROFILER_ENABLED = True
    # 数据库链接 URI
    DB_URI = create_Mysql_uri('root', 'wistbean', '127.0.0.1', 3306, 'my_system_dev')
    SQLALCHEMY_DATABASE_URI = DB_URI

class ProConfig(BaseConfig):
    # 数据库链接 URI
    DB_URI = create_Mysql_uri('root', 'root', '127.0.0.1', 3306, 'my_system_pro')
    SQLALCHEMY_DATABASE_URI = DB_URI


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

config = {
    "development": DevConfig,
    "testing": TestConfig,
    "production": ProConfig,
    "default": DevConfig,
}





