# coding: utf-8
from datetime import date, datetime  
from typing import List, Dict  

from metadefender_menlo.api.models.base_model import Model
from metadefender_menlo.api import util


class FileSubmitBody(Model):

    def __init__(self, userid=None, srcuri=None, clientip=None, sha256=None, filename=None, file_type=None, filesize=None):  
        """InboundRequestBody - a model defined in OpenAPI

        :param userid: The userid of this InboundRequestBody.  
        :type userid: str
        :param srcuri: The srcuri of this InboundRequestBody.  
        :type srcuri: str
        :param clientip: The clientip of this InboundRequestBody.  
        :type clientip: str
        :param sha256: The sha256 of this InboundRequestBody.  
        :type sha256: str
        :param filename: The filename of this InboundRequestBody.  
        :type filename: str
        :param file_type: The file_type of this InboundRequestBody.  
        :type file_type: str
        :param filesize: The filesize of this InboundRequestBody.  
        :type filesize: int
        """
        self.types = {
            'userid': str,
            'srcuri': str,
            'clientip': str,
            'sha256': str,
            'filename': str,
            'file_type': str,
            'filesize': int
        }

        self.attribute_map = {
            'userid': 'userid',
            'srcuri': 'srcuri',
            'clientip': 'clientip',
            'sha256': 'sha256',
            'filename': 'filename',
            'file_type': 'file_type',
            'filesize': 'filesize'
        }

        self._userid = userid
        self._srcuri = srcuri
        self._clientip = clientip
        self._sha256 = sha256
        self._filename = filename
        self._file_type = file_type
        self._filesize = filesize

    @classmethod
    def from_dict(cls, dikt) -> 'InboundRequestBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InboundRequestBody of this InboundRequestBody.  
        :rtype: InboundRequestBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def userid(self):
        """Gets the userid of this InboundRequestBody.

        The user ID of the user requesting the file  

        :return: The userid of this InboundRequestBody.
        :rtype: str
        """
        return self._userid

    @userid.setter
    def userid(self, userid):
        """Sets the userid of this InboundRequestBody.

        The user ID of the user requesting the file  

        :param userid: The userid of this InboundRequestBody.
        :type userid: str
        """

        self._userid = userid

    @property
    def srcuri(self):
        """Gets the srcuri of this InboundRequestBody.

        The URI of the original request for the file  

        :return: The srcuri of this InboundRequestBody.
        :rtype: str
        """
        return self._srcuri

    @srcuri.setter
    def srcuri(self, srcuri):
        """Sets the srcuri of this InboundRequestBody.

        The URI of the original request for the file  

        :param srcuri: The srcuri of this InboundRequestBody.
        :type srcuri: str
        """

        self._srcuri = srcuri

    @property
    def clientip(self):
        """Gets the clientip of this InboundRequestBody.

        The detected IP of the client requesting the file.  

        :return: The clientip of this InboundRequestBody.
        :rtype: str
        """
        return self._clientip

    @clientip.setter
    def clientip(self, clientip):
        """Sets the clientip of this InboundRequestBody.

        The detected IP of the client requesting the file.  

        :param clientip: The clientip of this InboundRequestBody.
        :type clientip: str
        """

        self._clientip = clientip

    @property
    def sha256(self):
        """Gets the sha256 of this InboundRequestBody.

        The sha256 of the requested file  

        :return: The sha256 of this InboundRequestBody.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        """Sets the sha256 of this InboundRequestBody.

        The sha256 of the requested file  

        :param sha256: The sha256 of this InboundRequestBody.
        :type sha256: str
        """

        self._sha256 = sha256

    @property
    def filename(self):
        """Gets the filename of this InboundRequestBody.

        The filename of the requested file  

        :return: The filename of this InboundRequestBody.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this InboundRequestBody.

        The filename of the requested file  

        :param filename: The filename of this InboundRequestBody.
        :type filename: str
        """

        self._filename = filename

    @property
    def file_type(self):
        """Gets the file_type of this InboundRequestBody.

        The file type as determined by MSIP  

        :return: The file_type of this InboundRequestBody.
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this InboundRequestBody.

        The file type as determined by MSIP  

        :param file_type: The file_type of this InboundRequestBody.
        :type file_type: str
        """

        self._file_type = file_type

    @property
    def filesize(self):
        """Gets the filesize of this InboundRequestBody.

        The file size  

        :return: The filesize of this InboundRequestBody.
        :rtype: int
        """
        return self._filesize

    @filesize.setter
    def filesize(self, filesize):
        """Sets the filesize of this InboundRequestBody.

        The file size  

        :param filesize: The filesize of this InboundRequestBody.
        :type filesize: int
        """

        self._filesize = filesize
