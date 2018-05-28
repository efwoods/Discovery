import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

collections = discovery.list_collections('{environment_id}')
print(json.dumps(collections, indent=2))
