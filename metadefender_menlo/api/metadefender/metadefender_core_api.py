# import requests
from tornado.httpclient import AsyncHTTPClient
from metadefender_menlo.api.metadefender.metadefender_api import MetaDefenderAPI
import datetime
import os
import json


class MetaDefenderCoreAPI(MetaDefenderAPI):
   
    def __init__(self, url, apikey):
        self.server_url = url
        self.apikey = apikey
        self.report_url = self.server_url + "/#/public/process/dataId/{data_id}"
    
    def _get_submit_file_headers(self, filename, metadata):    
        metadata_str = json.dumps(metadata) if metadata is not None else ""
    
        headers = {
            "filename": filename,             
            "metadata": metadata_str
        }
        return headers
    
    async def retrieve_sanitized_file(self, data_id):        
        print("MetaDefender > Retrieve Sanitized file for {0}".format(data_id))
        response, http_status = await self._request_status("sanitized_file", fields={"data_id": data_id})
        
        return (response, http_status)