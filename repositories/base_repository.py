from sqlalchemy import select, desc, update, delete

from database import db_session


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def find_all(self, query=None):
        resources = db_session.scalars(select(self.model).order_by(desc(self.model.id))).all()
        return list(map(lambda item: item.to_json(), resources))

    def find(self, id):
        resource = db_session.scalars(select(self.model).where(self.model.id == id)).first()
        db_session.commit()
        if resource is None:
            return None
        return resource.to_json()

    def update(self, id, data):
        db_session.execute(update(self.model).where(self.model.id == id).values(**data))
        db_session.commit()
        return self.find(id)

    def store(self, data):
        resource = self.model(**data)
        db_session.add(resource)
        db_session.commit()
        return resource.to_json()

    def delete(self, id):
        db_session.execute(delete(self.model).where(self.model.id == id))
        db_session.commit()
