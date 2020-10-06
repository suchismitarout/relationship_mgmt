from app import db
from app.models.members import Members


class MembersDao():
    def create_one_record(self, record):
        input_data = Members(**record)
        db.session.add(input_data)
        db.session.commit()

    def create_many_records(self, records):
        pass

    def delete_one_record(self, record):
        Members.query.filter_by(Name=record).delete()

    def find_one_by_name(self, data):
        return Members.query.filter_by(Name=data).first()

    def find_all(self):
        return Members.query.all()

    def find_by_id(self,id):
        return Members.query.get(id)
