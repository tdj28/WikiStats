from flask import Blueprint, jsonify
from decorators.secured import secured

authentication = Blueprint('authentication', __name__)


@authentication.route('/', methods=['POST'])
@secured
def authenticate():
    return jsonify({
        'token': 'an-auth-token'
    })
