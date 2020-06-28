from metadefender_menlo.api.handlers.base_handler import BaseHandler

class InboundMetadataHandler(BaseHandler):
    def post(self):        
        print("post_inbound_metadata - Not implemented")
        self.json_response({"error": "Not implemented"}, 400)