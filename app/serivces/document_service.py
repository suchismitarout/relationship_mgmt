import logging
from app.mongodb_dao.family_dao import FamilyDao
from app.common.constants import *


class DocumentService():

    def __init__(self):
        print("inside document service...")
        self.family = FamilyDao()

    def add_into_db(self, data):
        """
        logic:
            1. first it'll check whether it has any brothers/sisters in the input data.
            2. If any exists then it'll check the values brothers/sisters in the db or not .
            3. If exists then it'll be as it is else it'll delete them from brothers/sisters field in the input data.
            4. finally override/update/insert the input data to db.
        :param data:
        :return:
        """
        logging.info("adding new record into mongo db")
        logging.info("input data", data)
        for doc in data:
            if data[doc] == FATHER or MOTHER:
                record = self.family.find_one_by_name(data[doc])
                if not record:
                    # logic to remove the key from input data
                    del data[doc]

            elif data[doc] == BROTHERS or SISTERS:
                for j in data[doc]:
                    logging.info('j', j)
                    record = self.family.find_one_by_name(j)
                    if not record:
                        del data[doc]
        else:
            self.family.update_and_insert(data)

    def get_all_data_from_db(self):
        """
        It'll get all the data from members table
        :return:
        """

        try:
            result = []
            print("entry for getting the memebers data")
            res = self.family.find_all()
            print("res", res)
            print("type..", type(res))
            for i in res:
                print("record", i)
                print("type of i", type(i))
                i['_id'] = str(i['_id'])
                # rec = {ID: i[ID], NAME: i[NAME], AGE: i[AGE], SEX: i[SEX], FATHER: i[FATHER], MOTHER: i[MOTHER], BROTHERS: i[BROTHERS], SISTERS: i[SISTERS]}
                # print("rec", rec)
                result.append(i)
            print("result", result)
            return result
        except Exception as e:
            print(e.args)
            return "Internal error while connecting to database"

    def get_all_data_by_name(self, name):
        """
        It'll get all data along with their relationship combining members & rel_list table
        :param name:
        :return:
        """

        record = self.family.find_one_by_name(name)
        print("type of record", type(record))
        print("record got by name", record)
        for doc in record:
            doc['_id'] = str(doc['_id'])
            return doc
