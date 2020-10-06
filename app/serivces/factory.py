from app.common.constants import MONGODB, MYSQL


class ServiceFactory():

    def create(self, db_name):
        print("inside service factory... getting db name as ", db_name)
        if db_name == MYSQL:
            from app.serivces.sql_service import SQLService
            return SQLService()
        elif db_name == MONGODB:
            from app.serivces.document_service import DocumentService
            return DocumentService()
