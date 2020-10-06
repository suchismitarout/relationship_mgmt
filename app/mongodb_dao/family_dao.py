from app import db
from app.common.constants import *


class FamilyDao():
    def create_one(self, record):
        db.family.insertOne(record)

    def update_and_insert(self, record):
        db.family.update({NAME: record[NAME]},
                         record,
                         upsert=True)

    def find_one_by_name(self, data):
        return db.family.find({NAME: data})

    def delete_one_by_name(self, data):
        db.family.deleteOne({NAME: data})

    def find_all(self):
        print("find all records")
        return db.family.find()
