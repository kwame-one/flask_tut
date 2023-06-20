from flask_injector import FlaskInjector
from .modules.blog_module import BlogModule


def init_container(app):
    FlaskInjector(app=app, modules=[BlogModule])
