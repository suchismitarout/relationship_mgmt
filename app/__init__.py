from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser
import sys
from pymongo import MongoClient

db = None
db_name = sys.argv[1]
print("db_name", db_name)
app = Flask(__name__)

if db_name == 'mysql':
    print("inside mysql config...")
    ########################
    # To read config file  #
    # ########################

    config = configparser.ConfigParser()
    config.read('C:/Users/Suchismita/PycharmProjects/relationship_mgmt/app/resources/config.ini')
    config.sections()
    user = config['mysql']['user']
    pwd = config['mysql']['pwd']
    host = config['mysql']['host']
    db = config['mysql']['db']

    ##############################
    # MYSQL DATABASE CONNECTION  #
    ##############################

    app.config['SECRET_KEY'] = 'my_sec_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{pwd}@{host}/{db}'.format(user=user, pwd=pwd,
                                                                                              host=host,
                                                                                              db=db)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db = SQLAlchemy(app)


elif db_name == 'mongodb':
    print("inside mongodb config..")

    ###############################
    # MONGODB DATABASE CONNECTION #
    ###############################
    conn = MongoClient('localhost', 27017)
    db = conn['user_profile']
    print("after mongodb loading finished...")
