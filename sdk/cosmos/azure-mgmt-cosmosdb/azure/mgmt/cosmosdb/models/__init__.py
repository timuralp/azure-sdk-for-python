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

try:
    from ._models_py3 import ARMResourceProperties
    from ._models_py3 import Capability
    from ._models_py3 import CassandraKeyspaceCreateUpdateParameters
    from ._models_py3 import CassandraKeyspaceGetResults
    from ._models_py3 import CassandraKeyspaceResource
    from ._models_py3 import CassandraPartitionKey
    from ._models_py3 import CassandraSchema
    from ._models_py3 import CassandraTableCreateUpdateParameters
    from ._models_py3 import CassandraTableGetResults
    from ._models_py3 import CassandraTableResource
    from ._models_py3 import ClusterKey
    from ._models_py3 import Column
    from ._models_py3 import ConflictResolutionPolicy
    from ._models_py3 import ConsistencyPolicy
    from ._models_py3 import ContainerPartitionKey
    from ._models_py3 import DatabaseAccountConnectionString
    from ._models_py3 import DatabaseAccountCreateUpdateParameters
    from ._models_py3 import DatabaseAccountGetResults
    from ._models_py3 import DatabaseAccountListConnectionStringsResult
    from ._models_py3 import DatabaseAccountListKeysResult
    from ._models_py3 import DatabaseAccountListReadOnlyKeysResult
    from ._models_py3 import DatabaseAccountPatchParameters
    from ._models_py3 import DatabaseAccountRegenerateKeyParameters
    from ._models_py3 import ErrorResponse, ErrorResponseException
    from ._models_py3 import ExcludedPath
    from ._models_py3 import ExtendedResourceProperties
    from ._models_py3 import FailoverPolicies
    from ._models_py3 import FailoverPolicy
    from ._models_py3 import GremlinDatabaseCreateUpdateParameters
    from ._models_py3 import GremlinDatabaseGetResults
    from ._models_py3 import GremlinDatabaseResource
    from ._models_py3 import GremlinGraphCreateUpdateParameters
    from ._models_py3 import GremlinGraphGetResults
    from ._models_py3 import GremlinGraphResource
    from ._models_py3 import IncludedPath
    from ._models_py3 import Indexes
    from ._models_py3 import IndexingPolicy
    from ._models_py3 import Location
    from ._models_py3 import Metric
    from ._models_py3 import MetricAvailability
    from ._models_py3 import MetricDefinition
    from ._models_py3 import MetricName
    from ._models_py3 import MetricValue
    from ._models_py3 import MongoDBCollectionCreateUpdateParameters
    from ._models_py3 import MongoDBCollectionGetResults
    from ._models_py3 import MongoDBCollectionResource
    from ._models_py3 import MongoDBDatabaseCreateUpdateParameters
    from ._models_py3 import MongoDBDatabaseGetResults
    from ._models_py3 import MongoDBDatabaseResource
    from ._models_py3 import MongoIndex
    from ._models_py3 import MongoIndexKeys
    from ._models_py3 import MongoIndexOptions
    from ._models_py3 import Operation
    from ._models_py3 import OperationDisplay
    from ._models_py3 import PartitionMetric
    from ._models_py3 import PartitionUsage
    from ._models_py3 import PercentileMetric
    from ._models_py3 import PercentileMetricValue
    from ._models_py3 import RegionForOnlineOffline
    from ._models_py3 import SqlContainerCreateUpdateParameters
    from ._models_py3 import SqlContainerGetResults
    from ._models_py3 import SqlContainerResource
    from ._models_py3 import SqlDatabaseCreateUpdateParameters
    from ._models_py3 import SqlDatabaseGetResults
    from ._models_py3 import SqlDatabaseResource
    from ._models_py3 import SqlStoredProcedureCreateUpdateParameters
    from ._models_py3 import SqlStoredProcedureGetResults
    from ._models_py3 import SqlStoredProcedureResource
    from ._models_py3 import SqlTriggerCreateUpdateParameters
    from ._models_py3 import SqlTriggerGetResults
    from ._models_py3 import SqlTriggerResource
    from ._models_py3 import SqlUserDefinedFunctionCreateUpdateParameters
    from ._models_py3 import SqlUserDefinedFunctionGetResults
    from ._models_py3 import SqlUserDefinedFunctionResource
    from ._models_py3 import TableCreateUpdateParameters
    from ._models_py3 import TableGetResults
    from ._models_py3 import TableResource
    from ._models_py3 import ThroughputSettingsGetResults
    from ._models_py3 import ThroughputSettingsResource
    from ._models_py3 import ThroughputSettingsUpdateParameters
    from ._models_py3 import UniqueKey
    from ._models_py3 import UniqueKeyPolicy
    from ._models_py3 import Usage
    from ._models_py3 import VirtualNetworkRule
except (SyntaxError, ImportError):
    from ._models import ARMResourceProperties
    from ._models import Capability
    from ._models import CassandraKeyspaceCreateUpdateParameters
    from ._models import CassandraKeyspaceGetResults
    from ._models import CassandraKeyspaceResource
    from ._models import CassandraPartitionKey
    from ._models import CassandraSchema
    from ._models import CassandraTableCreateUpdateParameters
    from ._models import CassandraTableGetResults
    from ._models import CassandraTableResource
    from ._models import ClusterKey
    from ._models import Column
    from ._models import ConflictResolutionPolicy
    from ._models import ConsistencyPolicy
    from ._models import ContainerPartitionKey
    from ._models import DatabaseAccountConnectionString
    from ._models import DatabaseAccountCreateUpdateParameters
    from ._models import DatabaseAccountGetResults
    from ._models import DatabaseAccountListConnectionStringsResult
    from ._models import DatabaseAccountListKeysResult
    from ._models import DatabaseAccountListReadOnlyKeysResult
    from ._models import DatabaseAccountPatchParameters
    from ._models import DatabaseAccountRegenerateKeyParameters
    from ._models import ErrorResponse, ErrorResponseException
    from ._models import ExcludedPath
    from ._models import ExtendedResourceProperties
    from ._models import FailoverPolicies
    from ._models import FailoverPolicy
    from ._models import GremlinDatabaseCreateUpdateParameters
    from ._models import GremlinDatabaseGetResults
    from ._models import GremlinDatabaseResource
    from ._models import GremlinGraphCreateUpdateParameters
    from ._models import GremlinGraphGetResults
    from ._models import GremlinGraphResource
    from ._models import IncludedPath
    from ._models import Indexes
    from ._models import IndexingPolicy
    from ._models import Location
    from ._models import Metric
    from ._models import MetricAvailability
    from ._models import MetricDefinition
    from ._models import MetricName
    from ._models import MetricValue
    from ._models import MongoDBCollectionCreateUpdateParameters
    from ._models import MongoDBCollectionGetResults
    from ._models import MongoDBCollectionResource
    from ._models import MongoDBDatabaseCreateUpdateParameters
    from ._models import MongoDBDatabaseGetResults
    from ._models import MongoDBDatabaseResource
    from ._models import MongoIndex
    from ._models import MongoIndexKeys
    from ._models import MongoIndexOptions
    from ._models import Operation
    from ._models import OperationDisplay
    from ._models import PartitionMetric
    from ._models import PartitionUsage
    from ._models import PercentileMetric
    from ._models import PercentileMetricValue
    from ._models import RegionForOnlineOffline
    from ._models import SqlContainerCreateUpdateParameters
    from ._models import SqlContainerGetResults
    from ._models import SqlContainerResource
    from ._models import SqlDatabaseCreateUpdateParameters
    from ._models import SqlDatabaseGetResults
    from ._models import SqlDatabaseResource
    from ._models import SqlStoredProcedureCreateUpdateParameters
    from ._models import SqlStoredProcedureGetResults
    from ._models import SqlStoredProcedureResource
    from ._models import SqlTriggerCreateUpdateParameters
    from ._models import SqlTriggerGetResults
    from ._models import SqlTriggerResource
    from ._models import SqlUserDefinedFunctionCreateUpdateParameters
    from ._models import SqlUserDefinedFunctionGetResults
    from ._models import SqlUserDefinedFunctionResource
    from ._models import TableCreateUpdateParameters
    from ._models import TableGetResults
    from ._models import TableResource
    from ._models import ThroughputSettingsGetResults
    from ._models import ThroughputSettingsResource
    from ._models import ThroughputSettingsUpdateParameters
    from ._models import UniqueKey
    from ._models import UniqueKeyPolicy
    from ._models import Usage
    from ._models import VirtualNetworkRule
from ._paged_models import CassandraKeyspaceGetResultsPaged
from ._paged_models import CassandraTableGetResultsPaged
from ._paged_models import DatabaseAccountGetResultsPaged
from ._paged_models import GremlinDatabaseGetResultsPaged
from ._paged_models import GremlinGraphGetResultsPaged
from ._paged_models import MetricDefinitionPaged
from ._paged_models import MetricPaged
from ._paged_models import MongoDBCollectionGetResultsPaged
from ._paged_models import MongoDBDatabaseGetResultsPaged
from ._paged_models import OperationPaged
from ._paged_models import PartitionMetricPaged
from ._paged_models import PartitionUsagePaged
from ._paged_models import PercentileMetricPaged
from ._paged_models import SqlContainerGetResultsPaged
from ._paged_models import SqlDatabaseGetResultsPaged
from ._paged_models import SqlStoredProcedureGetResultsPaged
from ._paged_models import SqlTriggerGetResultsPaged
from ._paged_models import SqlUserDefinedFunctionGetResultsPaged
from ._paged_models import TableGetResultsPaged
from ._paged_models import UsagePaged
from ._cosmos_db_enums import (
    DatabaseAccountKind,
    DatabaseAccountOfferType,
    DefaultConsistencyLevel,
    ConnectorOffer,
    IndexingMode,
    DataType,
    IndexKind,
    PartitionKind,
    ConflictResolutionMode,
    TriggerType,
    TriggerOperation,
    KeyKind,
    UnitType,
    PrimaryAggregationType,
)

__all__ = [
    'ARMResourceProperties',
    'Capability',
    'CassandraKeyspaceCreateUpdateParameters',
    'CassandraKeyspaceGetResults',
    'CassandraKeyspaceResource',
    'CassandraPartitionKey',
    'CassandraSchema',
    'CassandraTableCreateUpdateParameters',
    'CassandraTableGetResults',
    'CassandraTableResource',
    'ClusterKey',
    'Column',
    'ConflictResolutionPolicy',
    'ConsistencyPolicy',
    'ContainerPartitionKey',
    'DatabaseAccountConnectionString',
    'DatabaseAccountCreateUpdateParameters',
    'DatabaseAccountGetResults',
    'DatabaseAccountListConnectionStringsResult',
    'DatabaseAccountListKeysResult',
    'DatabaseAccountListReadOnlyKeysResult',
    'DatabaseAccountPatchParameters',
    'DatabaseAccountRegenerateKeyParameters',
    'ErrorResponse', 'ErrorResponseException',
    'ExcludedPath',
    'ExtendedResourceProperties',
    'FailoverPolicies',
    'FailoverPolicy',
    'GremlinDatabaseCreateUpdateParameters',
    'GremlinDatabaseGetResults',
    'GremlinDatabaseResource',
    'GremlinGraphCreateUpdateParameters',
    'GremlinGraphGetResults',
    'GremlinGraphResource',
    'IncludedPath',
    'Indexes',
    'IndexingPolicy',
    'Location',
    'Metric',
    'MetricAvailability',
    'MetricDefinition',
    'MetricName',
    'MetricValue',
    'MongoDBCollectionCreateUpdateParameters',
    'MongoDBCollectionGetResults',
    'MongoDBCollectionResource',
    'MongoDBDatabaseCreateUpdateParameters',
    'MongoDBDatabaseGetResults',
    'MongoDBDatabaseResource',
    'MongoIndex',
    'MongoIndexKeys',
    'MongoIndexOptions',
    'Operation',
    'OperationDisplay',
    'PartitionMetric',
    'PartitionUsage',
    'PercentileMetric',
    'PercentileMetricValue',
    'RegionForOnlineOffline',
    'SqlContainerCreateUpdateParameters',
    'SqlContainerGetResults',
    'SqlContainerResource',
    'SqlDatabaseCreateUpdateParameters',
    'SqlDatabaseGetResults',
    'SqlDatabaseResource',
    'SqlStoredProcedureCreateUpdateParameters',
    'SqlStoredProcedureGetResults',
    'SqlStoredProcedureResource',
    'SqlTriggerCreateUpdateParameters',
    'SqlTriggerGetResults',
    'SqlTriggerResource',
    'SqlUserDefinedFunctionCreateUpdateParameters',
    'SqlUserDefinedFunctionGetResults',
    'SqlUserDefinedFunctionResource',
    'TableCreateUpdateParameters',
    'TableGetResults',
    'TableResource',
    'ThroughputSettingsGetResults',
    'ThroughputSettingsResource',
    'ThroughputSettingsUpdateParameters',
    'UniqueKey',
    'UniqueKeyPolicy',
    'Usage',
    'VirtualNetworkRule',
    'DatabaseAccountGetResultsPaged',
    'MetricPaged',
    'UsagePaged',
    'MetricDefinitionPaged',
    'OperationPaged',
    'PercentileMetricPaged',
    'PartitionMetricPaged',
    'PartitionUsagePaged',
    'SqlDatabaseGetResultsPaged',
    'SqlContainerGetResultsPaged',
    'SqlStoredProcedureGetResultsPaged',
    'SqlUserDefinedFunctionGetResultsPaged',
    'SqlTriggerGetResultsPaged',
    'MongoDBDatabaseGetResultsPaged',
    'MongoDBCollectionGetResultsPaged',
    'TableGetResultsPaged',
    'CassandraKeyspaceGetResultsPaged',
    'CassandraTableGetResultsPaged',
    'GremlinDatabaseGetResultsPaged',
    'GremlinGraphGetResultsPaged',
    'DatabaseAccountKind',
    'DatabaseAccountOfferType',
    'DefaultConsistencyLevel',
    'ConnectorOffer',
    'IndexingMode',
    'DataType',
    'IndexKind',
    'PartitionKind',
    'ConflictResolutionMode',
    'TriggerType',
    'TriggerOperation',
    'KeyKind',
    'UnitType',
    'PrimaryAggregationType',
]
