from exceptions.not_found_exception import ResourceNotFoundException
import logging


class BaseService:
    def __init__(self, repository, dto):
        self.repository = repository
        self.dto = dto

    def find_all(self, query=None):
        resources = self.repository.find_all(query)
        return list(map(lambda x: self.dto.from_orm(x).dict(), resources))

    def find(self, id):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Item not found')
        return self.dto.from_orm(resource).dict()

    def update(self, id, data):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Item not found')
        return self.dto.from_orm(self.repository.update(id, data)).dict()

    def store(self, data):
        resource = self.repository.store(data)
        return self.dto.from_orm(resource).dict()

    def delete(self, id):
        resource = self.repository.find(id)
        if resource is None:
            raise ResourceNotFoundException(description='Item not found')
        self.repository.delete(id)
        return True
