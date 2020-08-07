from metadefender_menlo.api.metadefender.metadefender_api import MetaDefenderAPI
from metadefender_menlo.api.responses.base_response import BaseResponse
from metadefender_menlo.api.models.file_analysis_response import FileAnalysisResponse

class FileAnalyis(BaseResponse):

    def __init__(self, allowedResponses=None):

        allowedResponses = [200, 500]
        super().__init__(allowedResponses)

        self._http_responses["200"] = self.__response200
        
    def __response200(self, json_response, status_code):

        if 'data_id' not in json_response:
            return (json_response, 404)
        else:
            model = FileAnalysisResponse()
            model.result = 'pending' if json_response['process_info']['progress_percentage'] < 100 else 'completed'
            if model.result == 'completed':
                model.outcome = 'clean' if json_response['process_info']['result'] == 'Allowed' else 'infected'
            else:
                model.outcome = 'unknown'
            model.report_url = MetaDefenderAPI.get_instance().report_url.format(data_id=json_response['data_id'])
            model.filename = json_response['file_info']['display_name']

            post_process = json_response['process_info']['post_processing']
            if 'sanitization_details' in post_process:
                if 'details' in post_process['sanitization_details']:
                    details = post_process['sanitization_details']['details']
                    modifications = []

                    if (isinstance(details, list)):
                        for item in details:
                            action = item['action'] if 'action' in item else 'Undefined Action'
                            count = item['count'] if 'count' in item else 'All'
                            obj_name = item['object_name'] if 'object_name' in item else 'All'
                            modifications.append("Action: {0} - Count: {1} - Object type: {2}".format(action, count, obj_name))                        
                    else:
                        modifications = [details]
                    
                    model.modifications = modifications
                    
            return (model.to_dict(), 200)