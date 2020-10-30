# [START app]

from flask import Flask, current_app
from flask_plugins import PluginManager, Plugin

class AppPlugin(Plugin):
    def register_blueprint(self, blueprint, **kwargs):
        """Registers a blueprint."""
        current_app.register_blueprint(blueprint, **kwargs)



app = Flask(__name__, static_url_path='/public', static_folder='public')
plugin_manager = PluginManager()
plugin_manager.init_app(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9060, debug=True)

