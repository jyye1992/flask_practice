from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Machines(db.Model):
    __tablename__ = 'machines'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    factoryId = db.Column(db.String, db.ForeignKey('factories.id'))


    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'factoryId': self.factoryId,
        }