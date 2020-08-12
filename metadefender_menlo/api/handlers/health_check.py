from metadefender_menlo.api.handlers.base_handler import BaseHandler
import logging

class HealthCheckHandler(BaseHandler):
    def get(self):        
        logging.warning("GET /health > OK!")        
        self.json_response({"status": "Ready"}, 200)