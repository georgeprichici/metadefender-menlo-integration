# coding: utf-8
from datetime import date, datetime  
from typing import List, Dict  

from metadefender_menlo.api.models.base_model import Model
from metadefender_menlo.api import util



class FileResponse(Model):

    def __init__(self, result=None, outcome=None, report_url=None, filename=None):  
        """FileResponse - a model defined in OpenAPI

        :param result: The result of this FileResponse.  
        :type result: str
        :param outcome: The outcome of this FileResponse.  
        :type outcome: str
        :param report_url: The report_url of this FileResponse.  
        :type report_url: str
        :param filename: The filename of this FileResponse.  
        :type filename: str
        """
        self.types = {
            'result': str,
            'outcome': str,
            'report_url': str,
            'filename': str
        }

        self.attribute_map = {
            'result': 'result',
            'outcome': 'outcome',
            'report_url': 'report_url',
            'filename': 'filename'
        }

        self._result = result
        self._outcome = outcome
        self._report_url = report_url
        self._filename = filename

    @classmethod
    def from_dict(cls, dikt) -> 'FileResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileResponse of this FileResponse.  
        :rtype: FileResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this FileResponse.

        The current status of the analysis  

        :return: The result of this FileResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this FileResponse.

        The current status of the analysis  

        :param result: The result of this FileResponse.
        :type result: str
        """
        allowed_values = ["pending", "completed"]  
        if result not in allowed_values:
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}"
                .format(result, allowed_values)
            )

        self._result = result

    @property
    def outcome(self):
        """Gets the outcome of this FileResponse.

        The overall analysis result.  

        :return: The outcome of this FileResponse.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this FileResponse.

        The overall analysis result.  

        :param outcome: The outcome of this FileResponse.
        :type outcome: str
        """
        allowed_values = ["clean", "infected", "unknown", "error"]  
        if outcome not in allowed_values:
            raise ValueError(
                "Invalid value for `outcome` ({0}), must be one of {1}"
                .format(outcome, allowed_values)
            )

        self._outcome = outcome

    @property
    def report_url(self):
        """Gets the report_url of this FileResponse.

        A full URL to retrieve the report  

        :return: The report_url of this FileResponse.
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this FileResponse.

        A full URL to retrieve the report  

        :param report_url: The report_url of this FileResponse.
        :type report_url: str
        """
        if report_url is None:
            raise ValueError("Invalid value for `report_url`, must not be `None`")  

        self._report_url = report_url

    @property
    def filename(self):
        """Gets the filename of this FileResponse.

        Optional string of new filename. If not given, will use original  

        :return: The filename of this FileResponse.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this FileResponse.

        Optional string of new filename. If not given, will use original  

        :param filename: The filename of this FileResponse.
        :type filename: str
        """

        self._filename = filename
