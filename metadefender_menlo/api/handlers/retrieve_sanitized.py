from metadefender_menlo.api.responses.retrieve_sanitized import RetrieveSanitized
from metadefender_menlo.api.handlers.base_handler import BaseHandler

class RetrieveSanitizedHandler(BaseHandler):
    async def get(self):
        uuid = self.get_argument('uuid')
                
        file, status_code = await self.metaDefenderAPI.retrieve_sanitized_file(uuid)
        
        sanitized_file, status = RetrieveSanitized().handle_response(status_code, file)
        self.stream_response(sanitized_file, status)