from flask import jsonify
from api import app, r

from decorators.secured import secured
import redis
r = redis.Redis('localhost')


@app.route('/hits/', methods=['POST'])
@secured
def hitme():
    r.incr('counter')
    count = r.get('counter')
    return jsonify({
        'token': 'an-auth-token-hit',
        'count': count
    })


