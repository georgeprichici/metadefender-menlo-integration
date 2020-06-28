# coding: utf-8
from datetime import date, datetime  
from typing import List, Dict  

from metadefender_menlo.api.models.base_model import Model
from metadefender_menlo.api import util


class FileBlockedError(Model):

    def __init__(self, result=None, outcome=None, report_url=None, filename=None, error_message=None):  
        """FileBlockedError - a model defined in OpenAPI

        :param result: The result of this FileBlockedError.  
        :type result: str
        :param outcome: The outcome of this FileBlockedError.  
        :type outcome: str
        :param report_url: The report_url of this FileBlockedError.  
        :type report_url: str
        :param filename: The filename of this FileBlockedError.  
        :type filename: str
        :param error_message: The error_message of this FileBlockedError.  
        :type error_message: str
        """
        self.types = {
            'result': str,
            'outcome': str,
            'report_url': str,
            'filename': str,
            'error_message': str
        }

        self.attribute_map = {
            'result': 'result',
            'outcome': 'outcome',
            'report_url': 'report_url',
            'filename': 'filename',
            'error_message': 'error_message'
        }

        self._result = result
        self._outcome = outcome
        self._report_url = report_url
        self._filename = filename
        self._error_message = error_message

    @classmethod
    def from_dict(cls, dikt) -> 'FileBlockedError':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileBlockedError of this FileBlockedError.  
        :rtype: FileBlockedError
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this FileBlockedError.

        The current status of the analysis  

        :return: The result of this FileBlockedError.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this FileBlockedError.

        The current status of the analysis  

        :param result: The result of this FileBlockedError.
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
        """Gets the outcome of this FileBlockedError.

        The overall analysis result.  

        :return: The outcome of this FileBlockedError.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this FileBlockedError.

        The overall analysis result.  

        :param outcome: The outcome of this FileBlockedError.
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
        """Gets the report_url of this FileBlockedError.

        A full URL to retrieve the report  

        :return: The report_url of this FileBlockedError.
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this FileBlockedError.

        A full URL to retrieve the report  

        :param report_url: The report_url of this FileBlockedError.
        :type report_url: str
        """
        if report_url is None:
            raise ValueError("Invalid value for `report_url`, must not be `None`")  

        self._report_url = report_url

    @property
    def filename(self):
        """Gets the filename of this FileBlockedError.

        Optional string of new filename. If not given, will use original  

        :return: The filename of this FileBlockedError.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this FileBlockedError.

        Optional string of new filename. If not given, will use original  

        :param filename: The filename of this FileBlockedError.
        :type filename: str
        """

        self._filename = filename

    @property
    def error_message(self):
        """Gets the error_message of this FileBlockedError.

        Only if outcome is error (string to report in the UI)  

        :return: The error_message of this FileBlockedError.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this FileBlockedError.

        Only if outcome is error (string to report in the UI)  

        :param error_message: The error_message of this FileBlockedError.
        :type error_message: str
        """

        self._error_message = error_message
