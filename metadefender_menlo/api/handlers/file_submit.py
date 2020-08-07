import tornado
from tornado.web import HTTPError

from metadefender_menlo.api.responses.file_submit import FileSubmit
from metadefender_menlo.api.handlers.base_handler import BaseHandler

class FileSubmitHandler(BaseHandler):

    async def post(self):   

        if len(self.request.files) < 1:
            raise HTTPError(400, 'No file uploaded')
        elif len(self.request.files) > 1:
            raise HTTPError(400, 'Too many files uploaded')
        
        field_name = list(self.request.files.keys())[0]
        info = self.request.files[field_name][0]
        filename, content_type = info["filename"], info["content_type"]
        fp = info["body"]
        print('Submit "%s" "%s" %d bytes', filename, content_type, len(fp))

        metadata = {}
        for arg in self.request.arguments.keys():
            print("{0}: {1}".format(arg, self.get_argument(arg)))
            metadata[arg] = str(self.request.arguments[arg])


        # make request to MetaDefender         
        json_response, http_status = await self.metaDefenderAPI.submit_file(filename, fp, metadata=metadata)    
        json_response, http_status = FileSubmit().handle_response(http_status, json_response)
        self.json_response(json_response, http_status)