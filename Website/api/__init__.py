from flask import Flask
from flaskext.mysql import MySQL
import redis
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

app.secret_key = 'hswPYkqVrneEBRDy9s2xX3RgH7jcHfab'
#handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
#handler.setLevel(logging.INFO)
#app.logger.addHandler(handler)
app.debug = True

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'wikiview'
app.config['MYSQL_DATABASE_PASSWORD'] = '%jswP^YkqV#rne'
app.config['MYSQL_DATABASE_DB'] = 'wikistats'
app.config['MYSQL_DTABASE_HOST'] = 'localhost'
mysql.init_app(app)


r = redis.Redis('localhost')
r.set('counter', 0)

from api.views.authentication import authentication
app.register_blueprint(authentication, url_prefix='/auth')

from api.views.welcome import welcome
from api.views.hits import hitme
from api.views.apiaccess import apiaccess
from api.views.login import login
from api.views.logout import logout

