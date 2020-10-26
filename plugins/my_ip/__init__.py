from flask import flash, Blueprint, render_template, render_template_string, jsonify, request
from flask_plugins import connect_event

__plugin__ = "MyIP"
__version__ = "0.1.0"

ip = Blueprint("ip", __name__, template_folder="templates")

@ip.route("/ip")
def index():
    ip = request.headers.get("X-Appengine-User-IP", request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
    if ip:
        return jsonify({"IP": ip})
    return jsonify({'error':'no ip headers'})

class MyIP:
    def setup(self):
        self.register_blueprint(ip, url_prefix="/ip")
        #connect_event("after_navigation", hello_world)
