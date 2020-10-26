# flask-plugins-test

```bash
$ python3 app.py 
```

results in

```
Traceback (most recent call last):
  File "app.py", line 10, in <module>
    plugin_manager.init_app(app)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/flask_plugins/__init__.py", line 245, in init_app
    self.setup_plugins()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/flask_plugins/__init__.py", line 331, in setup_plugins
    for plugin in itervalues(self.plugins):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/flask_plugins/__init__.py", line 259, in plugins
    self.load_plugins()
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/flask_plugins/__init__.py", line 269, in load_plugins
    for plugin_name, plugin_package in iteritems(self.find_plugins()):
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/flask_plugins/__init__.py", line 306, in find_plugins
    tmp = importlib.import_module(plugin)
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 953, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1006, in _gcd_import
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 965, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'flask-plugins-test'
```
