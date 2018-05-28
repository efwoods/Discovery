import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

fields = discovery.list_fields('{environment_id}', ['{collection_id1}','{collection_id2}'])
print(json.dumps(fields, indent=2))
