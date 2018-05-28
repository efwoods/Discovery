import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

updated_collection = discovery.update_collection(environment_id='{environment_id}', collection_id='{collection_id}', configuration_id='{configuration_id}', name='{collection_name}', description='{collection_desc}',)
print(json.dumps(updated_collection, indent=2))
