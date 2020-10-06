from flask import Blueprint, request, jsonify
from app.serivces.relation_mgmt_service import RelationMgmtService
from app.common.constants import *
import logging

rel_var = Blueprint('rel', __name__)

###################
# CREATING OBJECT #
###################
service = RelationMgmtService()
print("loading route....")


@rel_var.route('/', methods=['GET'])
def get_all_members():
    print("to get all data")
    result = service.get_all_data_from_db()
    print("result", result)
    return jsonify(result)


@rel_var.route('/add_member', methods=['POST'])
def add_new_member():
    try:
        logging.info("add new record")
        response = request.get_json()
        logging.debug("response", response)
        service.add_into_db(response)
        return jsonify({STATUS: SUCCESS, MSG: "Record successfully inserted into db"})
    except Exception as e:
        return jsonify({STATUS: FAILED, MSG: "Record insertion failed: {} ".format(e.args)})


@rel_var.route('/getbyname/<name>', methods=['GET'])
def get_all_members_relation_info_by_name(name):
    res = service.get_all_data_by_name(name)
    return jsonify(res)
