from app import db

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    uuid = db.Column(db.Integer)
    users = db.relationship("User", backref="role", lazy="dynamic")
