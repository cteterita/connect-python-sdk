# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class V1Employee(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, first_name=None, last_name=None, role_ids=None, authorized_location_ids=None, email=None, status=None, external_id=None, created_at=None, updated_at=None):
        """
        V1Employee - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'role_ids': 'list[str]',
            'authorized_location_ids': 'list[str]',
            'email': 'str',
            'status': 'str',
            'external_id': 'str',
            'created_at': 'str',
            'updated_at': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'role_ids': 'role_ids',
            'authorized_location_ids': 'authorized_location_ids',
            'email': 'email',
            'status': 'status',
            'external_id': 'external_id',
            'created_at': 'created_at',
            'updated_at': 'updated_at'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._role_ids = role_ids
        self._authorized_location_ids = authorized_location_ids
        self._email = email
        self._status = status
        self._external_id = external_id
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self):
        """
        Gets the id of this V1Employee.
        The employee's unique ID.

        :return: The id of this V1Employee.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this V1Employee.
        The employee's unique ID.

        :param id: The id of this V1Employee.
        :type: str
        """

        self._id = id

    @property
    def first_name(self):
        """
        Gets the first_name of this V1Employee.
        The employee's first name.

        :return: The first_name of this V1Employee.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this V1Employee.
        The employee's first name.

        :param first_name: The first_name of this V1Employee.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this V1Employee.
        The employee's last name.

        :return: The last_name of this V1Employee.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this V1Employee.
        The employee's last name.

        :param last_name: The last_name of this V1Employee.
        :type: str
        """

        self._last_name = last_name

    @property
    def role_ids(self):
        """
        Gets the role_ids of this V1Employee.
        The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.

        :return: The role_ids of this V1Employee.
        :rtype: list[str]
        """
        return self._role_ids

    @role_ids.setter
    def role_ids(self, role_ids):
        """
        Sets the role_ids of this V1Employee.
        The ids of the employee's associated roles. Currently, you can specify only one or zero roles per employee.

        :param role_ids: The role_ids of this V1Employee.
        :type: list[str]
        """

        self._role_ids = role_ids

    @property
    def authorized_location_ids(self):
        """
        Gets the authorized_location_ids of this V1Employee.
        The IDs of the locations the employee is allowed to clock in at.

        :return: The authorized_location_ids of this V1Employee.
        :rtype: list[str]
        """
        return self._authorized_location_ids

    @authorized_location_ids.setter
    def authorized_location_ids(self, authorized_location_ids):
        """
        Sets the authorized_location_ids of this V1Employee.
        The IDs of the locations the employee is allowed to clock in at.

        :param authorized_location_ids: The authorized_location_ids of this V1Employee.
        :type: list[str]
        """

        self._authorized_location_ids = authorized_location_ids

    @property
    def email(self):
        """
        Gets the email of this V1Employee.
        The employee's email address.

        :return: The email of this V1Employee.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this V1Employee.
        The employee's email address.

        :param email: The email of this V1Employee.
        :type: str
        """

        self._email = email

    @property
    def status(self):
        """
        Gets the status of this V1Employee.
        CWhether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard. 

        :return: The status of this V1Employee.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this V1Employee.
        CWhether the employee is ACTIVE or INACTIVE. Inactive employees cannot sign in to Square Register.Merchants update this field from the Square Dashboard. 

        :param status: The status of this V1Employee.
        :type: str
        """

        self._status = status

    @property
    def external_id(self):
        """
        Gets the external_id of this V1Employee.
        An ID the merchant can set to associate the employee with an entity in another system.

        :return: The external_id of this V1Employee.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this V1Employee.
        An ID the merchant can set to associate the employee with an entity in another system.

        :param external_id: The external_id of this V1Employee.
        :type: str
        """

        self._external_id = external_id

    @property
    def created_at(self):
        """
        Gets the created_at of this V1Employee.
        The time when the employee entity was created, in ISO 8601 format.

        :return: The created_at of this V1Employee.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this V1Employee.
        The time when the employee entity was created, in ISO 8601 format.

        :param created_at: The created_at of this V1Employee.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this V1Employee.
        The time when the employee entity was most recently updated, in ISO 8601 format.

        :return: The updated_at of this V1Employee.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this V1Employee.
        The time when the employee entity was most recently updated, in ISO 8601 format.

        :param updated_at: The updated_at of this V1Employee.
        :type: str
        """

        self._updated_at = updated_at

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other