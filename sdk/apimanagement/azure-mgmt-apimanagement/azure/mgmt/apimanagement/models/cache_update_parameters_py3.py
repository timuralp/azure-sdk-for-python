# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CacheUpdateParameters(Model):
    """Cache update details.

    :param description: Cache description
    :type description: str
    :param connection_string: Runtime connection string to cache
    :type connection_string: str
    :param resource_id: Original uri of entity in external system cache points
     to
    :type resource_id: str
    """

    _validation = {
        'description': {'max_length': 2000},
        'connection_string': {'max_length': 300},
        'resource_id': {'max_length': 2000},
    }

    _attribute_map = {
        'description': {'key': 'properties.description', 'type': 'str'},
        'connection_string': {'key': 'properties.connectionString', 'type': 'str'},
        'resource_id': {'key': 'properties.resourceId', 'type': 'str'},
    }

    def __init__(self, *, description: str=None, connection_string: str=None, resource_id: str=None, **kwargs) -> None:
        super(CacheUpdateParameters, self).__init__(**kwargs)
        self.description = description
        self.connection_string = connection_string
        self.resource_id = resource_id
