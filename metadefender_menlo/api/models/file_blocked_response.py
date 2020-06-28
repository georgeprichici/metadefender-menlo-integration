# coding: utf-8
from datetime import date, datetime  
from typing import List, Dict  

from metadefender_menlo.api.models.base_model import Model
from metadefender_menlo.api import util


class FileBlockedResponse(Model):


    def __init__(self, result=None, outcome=None, report_url=None, filename=None, modifications=None, outcome_categorization=None, observed_type=None, observed_specifics=None):  
        """FileBlockedResponse - a model defined in OpenAPI

        :param result: The result of this FileBlockedResponse.  
        :type result: str
        :param outcome: The outcome of this FileBlockedResponse.  
        :type outcome: str
        :param report_url: The report_url of this FileBlockedResponse.  
        :type report_url: str
        :param filename: The filename of this FileBlockedResponse.  
        :type filename: str
        :param modifications: The modifications of this FileBlockedResponse.  
        :type modifications: List[str]
        :param outcome_categorization: The outcome_categorization of this FileBlockedResponse.  
        :type outcome_categorization: str
        :param observed_type: The observed_type of this FileBlockedResponse.  
        :type observed_type: List[str]
        :param observed_specifics: The observed_specifics of this FileBlockedResponse.  
        :type observed_specifics: List[str]
        """
        self.types = {
            'result': str,
            'outcome': str,
            'report_url': str,
            'filename': str,
            'modifications': List[str],
            'outcome_categorization': str,
            'observed_type': List[str],
            'observed_specifics': List[str]
        }

        self.attribute_map = {
            'result': 'result',
            'outcome': 'outcome',
            'report_url': 'report_url',
            'filename': 'filename',
            'modifications': 'modifications',
            'outcome_categorization': 'outcome_categorization',
            'observed_type': 'observed_type',
            'observed_specifics': 'observed_specifics'
        }

        self._result = result
        self._outcome = outcome
        self._report_url = report_url
        self._filename = filename
        self._modifications = modifications
        self._outcome_categorization = outcome_categorization
        self._observed_type = observed_type
        self._observed_specifics = observed_specifics

    @classmethod
    def from_dict(cls, dikt) -> 'FileBlockedResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileBlockedResponse of this FileBlockedResponse.  
        :rtype: FileBlockedResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result(self):
        """Gets the result of this FileBlockedResponse.

        The current status of the analysis  

        :return: The result of this FileBlockedResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this FileBlockedResponse.

        The current status of the analysis  

        :param result: The result of this FileBlockedResponse.
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
        """Gets the outcome of this FileBlockedResponse.

        The overall analysis result.  

        :return: The outcome of this FileBlockedResponse.
        :rtype: str
        """
        return self._outcome

    @outcome.setter
    def outcome(self, outcome):
        """Sets the outcome of this FileBlockedResponse.

        The overall analysis result.  

        :param outcome: The outcome of this FileBlockedResponse.
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
        """Gets the report_url of this FileBlockedResponse.

        A full URL to retrieve the report  

        :return: The report_url of this FileBlockedResponse.
        :rtype: str
        """
        return self._report_url

    @report_url.setter
    def report_url(self, report_url):
        """Sets the report_url of this FileBlockedResponse.

        A full URL to retrieve the report  

        :param report_url: The report_url of this FileBlockedResponse.
        :type report_url: str
        """
        if report_url is None:
            raise ValueError("Invalid value for `report_url`, must not be `None`")  

        self._report_url = report_url

    @property
    def filename(self):
        """Gets the filename of this FileBlockedResponse.

        Optional string of new filename. If not given, will use original  

        :return: The filename of this FileBlockedResponse.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this FileBlockedResponse.

        Optional string of new filename. If not given, will use original  

        :param filename: The filename of this FileBlockedResponse.
        :type filename: str
        """

        self._filename = filename

    @property
    def modifications(self):
        """Gets the modifications of this FileBlockedResponse.

        Array of up to 5 strings of modifications performed on the file by CDR.    

        :return: The modifications of this FileBlockedResponse.
        :rtype: List[str]
        """
        return self._modifications

    @modifications.setter
    def modifications(self, modifications):
        """Sets the modifications of this FileBlockedResponse.

        Array of up to 5 strings of modifications performed on the file by CDR.    

        :param modifications: The modifications of this FileBlockedResponse.
        :type modifications: List[str]
        """

        self._modifications = modifications

    @property
    def outcome_categorization(self):
        """Gets the outcome_categorization of this FileBlockedResponse.

        Threat category (e.g. malware, adware, ...).  

        :return: The outcome_categorization of this FileBlockedResponse.
        :rtype: str
        """
        return self._outcome_categorization

    @outcome_categorization.setter
    def outcome_categorization(self, outcome_categorization):
        """Sets the outcome_categorization of this FileBlockedResponse.

        Threat category (e.g. malware, adware, ...).  

        :param outcome_categorization: The outcome_categorization of this FileBlockedResponse.
        :type outcome_categorization: str
        """

        self._outcome_categorization = outcome_categorization

    @property
    def observed_type(self):
        """Gets the observed_type of this FileBlockedResponse.

        Array of up to 5 strings of observed types or details, such as virus type  

        :return: The observed_type of this FileBlockedResponse.
        :rtype: List[str]
        """
        return self._observed_type

    @observed_type.setter
    def observed_type(self, observed_type):
        """Sets the observed_type of this FileBlockedResponse.

        Array of up to 5 strings of observed types or details, such as virus type  

        :param observed_type: The observed_type of this FileBlockedResponse.
        :type observed_type: List[str]
        """

        self._observed_type = observed_type

    @property
    def observed_specifics(self):
        """Gets the observed_specifics of this FileBlockedResponse.

        array of up to 5 strings of observed specifics, such as activities.  

        :return: The observed_specifics of this FileBlockedResponse.
        :rtype: List[str]
        """
        return self._observed_specifics

    @observed_specifics.setter
    def observed_specifics(self, observed_specifics):
        """Sets the observed_specifics of this FileBlockedResponse.

        array of up to 5 strings of observed specifics, such as activities.  

        :param observed_specifics: The observed_specifics of this FileBlockedResponse.
        :type observed_specifics: List[str]
        """

        self._observed_specifics = observed_specifics
