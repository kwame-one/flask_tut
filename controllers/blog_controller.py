from flask import request, jsonify, Blueprint
from flask_pydantic import validate

from services.blog_service import BlogService
from requests.blog_request import BlogRequest

blog_bp = Blueprint('blog_bp', __name__)


@blog_bp.get('/')
def find_all(service: BlogService):
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@blog_bp.get('/<int:id>')
def find(id, service: BlogService):
    resource = service.find(id)
    return jsonify(resource)


@blog_bp.put('/<int:id>')
def update(id, service: BlogService):
    body = BlogRequest(**request.get_json())
    resource = service.update(id, body.dict())
    return jsonify(resource)


@blog_bp.post('/')
def store(service: BlogService):
    body = BlogRequest(**request.get_json())
    return jsonify(service.store(body.dict())), 201


@blog_bp.delete('/<int:id>')
def delete(id, service: BlogService):
    service.delete(id)
    return jsonify({}), 204
