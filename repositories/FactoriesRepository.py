from models.Factories import Factories

class FactoriesRepository:
    def __init__(self):
        self.model = Factories
        self.db = Factories().db

    def insert(self, data):
        self.db.session.add(Factories(**data))
        self.db.session.commit()

    def update_with_region_like(self, like_statment, data):
        self.db.session.query(self.model) \
            .filter(self.model.region.like(like_statment)) \
            .update(data, synchronize_session='fetch',)        
                # synchronize_session=False,
        self.db.session.commit()

    def delete_by_ids(self, ids):
        self.db.session.query(self.model).filter(self.model.id.in_(ids)).delete()
        self.db.session.commit()

    def get(self):
        return [f.serialize for f in self.model.query.all()]
    

    # def where(self):
    # '''
    #     query with where
    # '''
    #     pass

    def first(self):
        return self.model.query.first().serialize