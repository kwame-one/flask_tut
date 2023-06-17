from flask import Flask, jsonify

from database import db_session, init_db
from routes.blog_route import blog_bp
from exceptions.not_found_exception import ResourceNotFoundException
import logging

app = Flask(__name__)
app.config.from_object('config')

init_db()

# logging.basicConfig(filename='logs/flask.log', level=logging.DEBUG,
#                     format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

app.register_blueprint(blog_bp, url_prefix='/blogs')

app.register_error_handler(ResourceNotFoundException, lambda e: (jsonify({'message': e.description}), 404))


@app.route('/')
def index():
    return 'welcome'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
