# import requests
from tornado.httpclient import AsyncHTTPClient
import datetime
import os
import json


class MetaDefenderCoreAPI:
    server_url = "http://localhost:8008"
    apikey = ""
    cert_file = None

    # __http = urllib3.PoolManager(cert_reqs='CERT_NONE')

    api_endpoints = {
        "submit_file": {
            "type": "POST",
            "endpoint": "/file"
        },
        "retrieve_result": {
            "type": "GET",
            "endpoint": "/file/{data_id}"
        },
        "sanitized_file": {
            "type": "GET",
            "endpoint": "/file/converted/{data_id}"
        }, 
        "hash_lookup": {
            "type": "GET", 
            "endpoint": "/hash/{hash}"
        }
    }

    @staticmethod
    def config(url, apikey, crt):
        MetaDefenderCoreAPI.server_url = url
        MetaDefenderCoreAPI.apikey = apikey
        MetaDefenderCoreAPI.cert_file = crt

    def __init__(self):
        pass
    
    @property
    def supports_download_file(self):
        return False

    async def submit_file(self, filename, fp, analysis_callback_url=None, metadata=None):  
        print("Submit file > filename: {0} ".format(filename))   
    
        metadata_str = json.dumps(metadata) if metadata is not None else ""
    
        headers = {
            "filename": filename,             
            "metadata": metadata_str
        }
                
        json_response, http_status = await self.__request_as_json_status("submit_file", body=fp, headers=headers)

        return (json_response, http_status)

    # polling mechanism
    # callbackurl replaced it, however is available starting with Core v4.17.0 
    async def retrieve_result(self, data_id):
        print("MetaDefender > Retrieve result for {0}".format(data_id))
        
        analysis_completed = False
        
        while (not analysis_completed):            
            json_response, http_status = await self.check_result(data_id)
            if ("process_info" in json_response and "progress_percentage" in json_response["process_info"]):
                analysis_completed = json_response["process_info"]["progress_percentage"] == 100
            else:
                print("Unexpected response from MetaDefender: {0}".format(json_response))
        
        return (json_response, http_status)

    async def check_result(self, data_id):
        print("MetaDefender > Check result for {0}".format(data_id))        
        return await self.__request_as_json_status("retrieve_result", fields={"data_id": data_id})
    
    async def hash_lookup(self, sha256):
        print("MetaDefender > Hash Lookup for {0}".format(sha256))    
        return await self.__request_as_json_status("hash_lookup", fields={"hash": sha256})
    
    async def retrieve_sanitized_file(self, data_id):        
        print("MetaDefender > Retrieve Sanitized file for {0}".format(data_id))
        response, http_status = await self.__request_status("sanitized_file", fields={"data_id": data_id})
        
        return (response, http_status)

    async def __request_as_json_status(self, endpoint_id, fields=None, headers=None, body=None):
        response, http_status = await self.__request_status(endpoint_id, fields, headers, body)

        json_resp = json.loads(response)

        return (json_resp, http_status)

    async def __request_status(self, endpoint_id, fields=None, headers=None, body=None):

        print("MetaDefender Request > ({0}) for {1}".format(endpoint_id, fields))   

        endpoint_details = self.api_endpoints[endpoint_id]
        endpoint_path = endpoint_details["endpoint"]
        if fields is not None:
            endpoint_path = endpoint_details["endpoint"].format(**fields)
        metadefender_url = MetaDefenderCoreAPI.server_url + endpoint_path
        
        if MetaDefenderCoreAPI.apikey is not None: 
            headers["apikey"] = MetaDefenderCoreAPI.apikey

        before_submission = datetime.datetime.now()        
        print("Request [{0}]: {1}".format(endpoint_details["type"], metadefender_url))

        http_client = AsyncHTTPClient(None, defaults=dict(user_agent="MenloTornadoIntegration", validate_cert=False))
        response = await http_client.fetch(request=metadefender_url, method=endpoint_details["type"], headers=headers, body=body, )
        
        # response = requests.request(endpoint_details["type"], metadefender_url, headers=headers, data=body, verify=MetaDefenderCoreAPI.cert_file)
        
        http_status = response.code                        
        total_submission_time = datetime.datetime.now() - before_submission

        print("{timestamp} {name} >> time: {total_time}, http status: {status}".format(timestamp=before_submission, name=endpoint_id, total_time=total_submission_time, status=http_status))                

        return (response.body, http_status)