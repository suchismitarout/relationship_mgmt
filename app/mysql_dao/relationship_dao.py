from app import db
from app.models.relationship import Relationship


class RelationshipDao():
    def create_one_record(self, record):
        input_data = Relationship(**record)
        db.session.add(input_data)
        db.session.commit()

    def create_many_records(self, records):
        pass

    def delete_one_record(self, record):
        Relationship.query.filter_by(Name=record).delete()

    def find_one_by_name(self, name):
        return Relationship.query.filter_by(Name=name).first()

    def find_many_by_Id1(self, id1):
        return Relationship.query.filter_by(Id1=id1).all()



