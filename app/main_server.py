from app import app
from app.routes.relation_mgmt_route import rel_var
import logging

logging.basicConfig(level=logging.DEBUG)

if __name__ == '__main__':
    app.register_blueprint(rel_var)
    app.run(host="0.0.0.0")
    logging.info("####################")
    logging.debug("app starts running")
    logging.info("####################")
