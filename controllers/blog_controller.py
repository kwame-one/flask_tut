from flask import request, jsonify, Blueprint
from flask_pydantic import validate

from services.blog_service import BlogService
from requests.blog_request import BlogRequest

service = BlogService()
blog_bp = Blueprint('blog_bp', __name__)


@blog_bp.get('/')
def find_all():
    resources = service.find_all(query=request.args)
    return jsonify(resources)


@blog_bp.get('/<int:id>')
def find(id):
    resource = service.find(id)
    return jsonify(resource)


@blog_bp.put('/<int:id>')
@validate()
def update(id, body: BlogRequest):
    resource = service.update(id, body.dict())
    return jsonify(resource)


@blog_bp.post('/')
@validate()
def store(body: BlogRequest):
    resource = service.store(body.dict())
    return jsonify(resource), 201


@blog_bp.delete('/<int:id>')
def delete(id):
    service.delete(id)
    return jsonify({}), 204
