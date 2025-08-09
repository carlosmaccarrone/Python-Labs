from abc import ABC, abstractmethod
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

class DefaultDataAccess(ABC):
    def __init__(self, engine):
        self.Session = sessionmaker(bind=engine)

    @abstractmethod
    def entityType(self):
        pass

    def generateWhere(self, query, generic):
        # To override children if desired
        return query

    def create(self, generic):
        session = self.Session()
        try:
            session.add(generic)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError("Error occurred during create: {}".format(e))
        finally:
            session.close()

    def update(self, generic):
        session = self.Session()
        try:
            session.merge(generic)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise RuntimeError("Error occurred during update: {}".format(e))
        finally:
            session.close()

    def all_instances(self):
        session = self.Session()
        try:
            query = session.query(self.entityType())
            return query.all()
        finally:
            session.close()

    def search_by_id(self, id_):
        session = self.Session()
        try:
            query = session.query(self.entityType()).filter_by(id=id_)
            return query.one()
        finally:
            session.close()

    def search_by_example(self, generic):
        session = self.Session()
        try:
            query = session.query(self.entityType())
            query = self.generateWhere(query, generic)
            return query.all()
        finally:
            session.close()

