import openai

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

## Enter your Open API Key here
openai.api_key = "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"
