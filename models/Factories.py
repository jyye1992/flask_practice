from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Factories(db.Model):
    '''
    # whereIn
    # doc: sqlalchemy.sql.expression.ColumnOperators.in_(others)
    
    # insert
    # doc: sqlalchemy.orm.Session.add

    # update
    # doc: 

    # delete
    # doc: sqlalchemy.orm.query.Query.delete(synchronize_session='evaluate')
    '''

    __tablename__ = 'factories'
    
    
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String)
    isSend = db.Column(db.String)

    def __init__(self, **kwargs):
        self.db = db
        super().__init__(**kwargs)

    def __getitem__(self, field):
        return self.__dict__[field]

    @property
    def serialize(self):
        return {
            'id': self.id,
            'region': self.region,
            'isSend': self.isSend,
        }

    

