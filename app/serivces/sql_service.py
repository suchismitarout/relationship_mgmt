from app.common.constants import *
import logging
from app.mysql_dao.members_dao import MembersDao
from app.mysql_dao.relationship_dao import RelationshipDao


class SQLService():
    def __init__(self):
        self.membersdao = MembersDao()
        self.relationshipdao = RelationshipDao()
        self.rel_list = [FATHER, MOTHER, BROTHERS, SISTERS]

    def add_into_db(self, data):
        """
        logic:
            1. First it'll check the name given in input present in members table or not.
            2. If exists then it'll check in rel_list table.
            3. It'll check the values in brothers/sisters present in memebers or not.
            4. If present then it'll add therir id along with id of input in rel_list table
        :param data:
        :return:
        """
        logging.info("adding new record into mysql db")
        check_record = self.membersdao.find_one_by_name(data[NAME])
        if check_record:
            value_to_add = {}
            for i in self.rel_list:
                if i in data:
                    if data[i] == FATHER or MOTHER:
                        record = self.membersdao.find_one_by_name(data[i])
                        if record:
                            logging.debug("got record", record)
                            value_to_add[ID1] = data[ID]
                            value_to_add[ID2] = record.Id
                            value_to_add[RELATION] = i
                            self.relationshipdao.create_one_record(value_to_add)
                    else:
                        for j in data[i]:
                            print('j', j)
                            record = self.membersdao.find_one_by_name(j)
                            if record:
                                logging.debug("got record", record)
                                value_to_add[ID1] = data[ID]
                                value_to_add[ID2] = record.Id
                                value_to_add[RELATION] = i
                                self.relationshipdao.create_one_record(value_to_add)
        else:
            self.membersdao.create_one_record(
                {ID: data[ID], NAME: data[NAME], AGE: data[AGE], SEX: data[SEX]})

    def get_all_data_from_db(self):
        """
        It'll get all the data from members table
        :return:
        """
        try:
            result = []
            print("entry for getting the memebers data")
            res = self.membersdao.find_all()
            # print("res", res)
            # print("type..", type(res))
            for i in res:
                # print("record", i)
                # print("type of i", type(i))
                rec = {ID: i.Id, NAME: i.Name, AGE: i.Age, SEX: i.Sex}
                # print("rec", rec)
                result.append(rec)
            # print("result", result)
            return result
        except Exception as e:
            # print(e.args)
            return "There is no data in database. Please add few"

    def get_all_data_by_name(self, name):
        """
        It'll get all data along with their relationship combining members & rel_list table
        :param name:
        :return:
        """
        member_rel_info = {}
        member = self.membersdao.find_one_by_name(name)
        logging.debug(member.Id)
        member_rel_info[ID] = member.Id
        member_rel_info[NAME] = member.Name
        member_rel_info[AGE] = member.Age
        member_rel_info[SEX] = member.Sex
        member_rel_info[BROTHERS] = []
        member_rel_info[SISTERS] = []
        if member:
            rel = self.relationshipdao.find_many_by_Id1(member.Id)
            for i in rel:
                r = {ID1: i.Id1, ID2: i.Id2, RELATION: i.Relation}
                logging.debug(r)
                if r[RELATION] == FATHER:
                    mem = self.membersdao.find_by_id(r[ID2])
                    logging.debug(mem)
                    member_rel_info[FATHER] = mem.Name
                if r[RELATION] == MOTHER:
                    mem = self.membersdao.find_by_id(r[ID2])
                    member_rel_info[MOTHER] = mem.Name
                if r[RELATION] == BROTHERS:
                    mem = self.membersdao.find_by_id(r[ID2])
                    member_rel_info[BROTHERS].append(mem.Name)
                if r[RELATION] == SISTERS:
                    mem = self.membersdao.find_by_id(r[ID2])
                    member_rel_info[SISTERS].append(mem.Name)
        return member_rel_info
