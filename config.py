class Config:
    DEBUG = False
    APP_SECRET = "justine123"

class DevelopmentConfig(Config):
    DEBUG = True
     

class TestingConfig(Config):
    DEBUG = True

  
app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig
}    
db_configs = {
    'dbname': 'maintenence_tracker',
    'user': 'postgres',
    'host': 'localhost',
    'port': 5432
}