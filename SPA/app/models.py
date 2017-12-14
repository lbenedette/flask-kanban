from app import db


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    status = db.Column(db.String(10))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'text': self.text,
            'status': self.status
        }
