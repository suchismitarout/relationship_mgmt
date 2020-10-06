from app import db


class Relationship(db.Model):
    __tablename__ = 'relationship'

    Id1 = db.Column(db.Integer, primary_key=True)
    Id2 = db.Column(db.Integer, primary_key=True)
    Relation = db.Column(db.Text(30))

    def __init__(self, Id1,Id2, Relation):
        self.Id1 = Id1
        self.Id2 = Id2
        self.Relation = Relation

    def __repr__(self):
        return f"Id1: {self.Id1}, Id2: {self.Id2}, Relation: {self.Relation}"
