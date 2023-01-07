import openai
import os

class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

openai.api_key = os.getenv('OPEN_AI_KEY')
openai_key = openai.api_key