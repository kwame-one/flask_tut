from flask import Blueprint
from controllers.blog_controller import find_all, store, find, delete, update

blog_bp = Blueprint('blog_bp', __name__)

blog_bp.route('', methods=['GET'])(find_all)
blog_bp.route('/', methods=['POST'])(store)
blog_bp.route('/<string:id>', methods=['GET'])(find)
blog_bp.route('/<string:id>', methods=['DELETE'])(delete)
blog_bp.route('/<string:id>', methods=['PUT'])(update)
