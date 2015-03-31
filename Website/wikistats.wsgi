#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/Website/")

from api import app as application
application.secret_key = 'T@Aq6qmkojqk3h4;khj;qj235k@^124'
