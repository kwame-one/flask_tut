from exceptions.not_found_exception import ResourceNotFoundException
import logging


class BaseService:
    def __init__(self, repository):
        self.repository = repository

    def find_all(self, query=None):
        logging.info('data %s', self.repository.find_all())
        return self.repository.find_all(query)

    def find(self, id):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Item not found')
        return resource

    def update(self, id, data):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Item not found')
        return self.repository.update(id, data)

    def store(self, data):
        return self.repository.store(data)

    def delete(self, id):
        resource = self.repository.find(id)

        if resource is None:
            raise ResourceNotFoundException(description='Item not found')
        self.repository.delete(id)
        return True
