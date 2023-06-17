from flask import request, jsonify
from services.blog_service import BlogService

service = BlogService()


def find_all():
    resources = service.find_all(query=request.args)
    return jsonify(resources)


def find(id):
    resource = service.find(id)
    return jsonify(resource)


def update(id):
    resource = service.update(id, request.get_json(force=True))
    return jsonify(resource)


def store():
    resource = service.store(request.get_json(force=True))
    return jsonify(resource), 201


def delete(id):
    service.delete(id)
    return jsonify({}), 204
