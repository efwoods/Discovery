import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

collection = discovery.get_collection('{environment_id}', '{collection_id}')
print(json.dumps(collection, indent=2))
