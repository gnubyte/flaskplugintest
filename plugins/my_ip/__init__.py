from flask import flash, Blueprint, render_template, render_template_string, jsonify, request
from flask_plugins import connect_event

# FROM <PROJECT_DIRECTORY_NAME>.app import AppPlugin
# An AppPlugin class must also be available from either the app or another python file

from flaskplugintest.app import AppPlugin # have to get the app plugin from the flask app
# the from here is going to reference the root level project folder
# in my case... flaskpluginstest
# app will reference the app.py file at the root of the directory


__plugin__ = "MyIP"
__version__ = "0.1.0"

ipbp = Blueprint("ip", __name__, template_folder="templates")

@ipbp.route("/ip")
def index():
    ip = request.headers.get("X-Appengine-User-IP", request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    if ip:
        return jsonify({"IP": ip})
    return jsonify({'error':'no ip headers'})

class MyIP(AppPlugin):
    def setup(self):
        self.register_blueprint(ipbp, url_prefix="/ip")
        #connect_event("after_navigation", hello_world)
