from app import db


class Members(db.Model):
    __tablename__ = 'members'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.Text(30))
    Age = db.Column(db.Integer)
    Sex = db.Column(db.Text(20))

    def __init__(self, Id, Name, Age, Sex):
        self.Id = Id
        self.Name = Name
        self.Age = Age
        self.Sex = Sex

    def __repr__(self):
        return f"Id:{self.Id}, Name:{self.Name}, Age:{self.Age}, Sex:{self.Sex}"
