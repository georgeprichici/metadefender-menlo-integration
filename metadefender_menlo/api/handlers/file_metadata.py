from metadefender_menlo.api.handlers.base_handler import BaseHandler
import logging

class InboundMetadataHandler(BaseHandler):
    def post(self):        
        logging.warning("POST /api/v1/submit > Not implemented")        
        self.json_response({"error": "Not implemented"}, 400)