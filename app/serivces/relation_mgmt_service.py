from app.serivces.factory import ServiceFactory
from app import db_name


class RelationMgmtService():

    def __init__(self):
        # problem:1
        # self.sql_service = SQLService()
        # self.doc_service = DocumentService()

        # problem:2
        # if db_name == 'mysql':
        #     self.service = SQLService()
        # elif db_name == 'mongo':
        #     self.service = DocumentService()

        print("before creating the service.. with db_name", db_name)
        # solution
        self.service = ServiceFactory().create(db_name)
        print("after getting the Servicefactory..", self.service)

    def add_into_db(self, data):
        return self.service.add_into_db(data)

    def get_all_data_from_db(self):
        return self.service.get_all_data_from_db()

    def get_all_data_by_name(self, name):
        return self.service.get_all_data_by_name(name)
