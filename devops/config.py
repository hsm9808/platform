import redis
class Config(object):
    """配置信息"""
    SECRET_KEY = "abcdefg"
    #数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:Hsm2020!@123.56.80.143:3306/devops"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #redis
    REDIS_HOST = "123.56.80.143"
    REDIS_PORT = 6379
    REDIS_PASSWORD = "hsm123"
    #flask-session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT,password=REDIS_PASSWORD)
    SESSION_USER_SIGNER = True #对cookie中的session_id进行隐藏处理
    PERMANENT_SESSION_LIFETIME = 7200 #session数据的有效期

class DevelopConfig(Config):
    """开发配置信息"""
    DEBUG = True

class ProdConfig(Config):
    """线上配置信息"""
    pass


config_map={
    "develop":DevelopConfig,
    "prod":ProdConfig
}