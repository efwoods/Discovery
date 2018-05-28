import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

new_collection = discovery.create_collection(environment_id='{environment_id}', configuration_id='{configuration_id}', name='{collection_name}', description='{collection_desc}', language='{collection_lang}')
print(json.dumps(new_collection, indent=2))
