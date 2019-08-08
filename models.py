from extensions import db


class Model(db.Model):
    """
    Basic model class that define common attributes
    """
    __abstract__ = True

    pk = db.Column('id', db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated = db.Column(db.DateTime, default=db.func.current_timestamp(),
                        onupdate=db.func.current_timestamp())


class HotDog(Model):
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(240), unique=True)
