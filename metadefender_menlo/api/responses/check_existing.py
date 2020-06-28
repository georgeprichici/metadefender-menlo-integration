
from metadefender_menlo.api.responses.base_response import BaseResponse


class CheckExisting(BaseResponse):
    
    def __init__(self, allowedResponses=None):
        
        allowedResponses = [200, 500]
        super().__init__(allowedResponses)

        self._http_responses["200"] = self.__response200

    def __response200(self, response, status_code):
        translation = {
            'uuid': '{0}',
            'result': '{0}'
        }

        if 'data_id' in response: 
            
            self._translate('uuid', translation, response['data_id'])
            self._translate('result', translation, 'found')

            return (translation, status_code)
        else:
            return (response, 404)

