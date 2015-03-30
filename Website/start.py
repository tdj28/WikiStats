from api import app
from api.views import login
from api.views import hits
from api.views import authentication


app.run(host='0.0.0.0', port=8080)

