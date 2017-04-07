from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25))
    password = db.Column(db.String(60))
    authenticated = db.Column(db.Boolean, default=False)
    rows = db.relationship('Row', foreign_keys='Row.user_id')

    def get_id(self):
        """Return the id to satisfy Flask-Login's requirements."""
        return self.id

    def is_active(self):
        """True, as all users are active."""
        return True

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False


class Row(db.Model):
    __tablename__ = 'row'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255))
    status = db.Column(db.String(10))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
