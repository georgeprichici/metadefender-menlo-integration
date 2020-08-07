import yaml
import os

import tornado.ioloop
import tornado.web

from metadefender_menlo.api.handlers.analysis_result import AnalysisResultHandler
from metadefender_menlo.api.handlers.file_metadata import InboundMetadataHandler
from metadefender_menlo.api.handlers.file_submit import FileSubmitHandler
from metadefender_menlo.api.handlers.retrieve_sanitized import RetrieveSanitizedHandler
from metadefender_menlo.api.handlers.check_existing import CheckExistingHandler

from metadefender_menlo.api.models.file_submit_body import FileSubmitBody
from metadefender_menlo.api.metadefender.metadefender_api import MetaDefenderAPI
from metadefender_menlo.api.metadefender.metadefender_core_api import MetaDefenderCoreAPI
from metadefender_menlo.api.metadefender.metadefender_cloud_api import MetaDefenderCloudAPI

SERVER_PORT = 3000
HOST = "0.0.0.0"
API_VERSION = "/api/v1"

settings = dict(
    ssl_options = {
        "certfile": os.path.join("certs/server.crt"),
        "keyfile": os.path.join("certs/server.key"),
    }
)

def initial_config():
    
    with open("config.yml", 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            api = config["api"]
            md_type = api["type"]
            url = api["url"][md_type] if "url" in api and md_type in api["url"] else "http://localhost:8008"
            apikey = api["params"]["apikey"] if "params" in api and "apikey" in api["params"] else None
            
            md_cls = MetaDefenderCoreAPI if md_type == "core" else MetaDefenderCloudAPI
            MetaDefenderAPI.config(url, apikey, md_cls)
            
            if "server" in config:
                server_details = config["server"]
                SERVER_PORT = server_details["port"] if "port" in server_details else SERVER_PORT
                HOST = server_details["host"] if "host" in server_details else HOST
                API_VERSION = server_details["api_version"] if "api_version" in server_details else HOST
            
        except yaml.YAMLError as exc:
            print(exc)

def make_app():
    endpoints_list = [
        (API_VERSION + '/check', CheckExistingHandler),
        (API_VERSION + '/inbound', InboundMetadataHandler),
        (API_VERSION + '/submit', FileSubmitHandler),
        (API_VERSION + '/result', AnalysisResultHandler),
        (API_VERSION + '/file', RetrieveSanitizedHandler)
    ]
    return tornado.web.Application(endpoints_list)

def main():    
    initial_config()
    
    app = make_app()
    # http_server = tornado.httpserver.HTTPServer(app, **settings)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(SERVER_PORT, HOST)
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()