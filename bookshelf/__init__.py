from flask import Flask
from bookshelf.main.main_controllers import main
from bookshelf.admin.admin_controllers import admin

app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')

# enable jinja2 extensions - i.e. continue in for loops
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')