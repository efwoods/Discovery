import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

configs = discovery.list_configurations('{environment_id}')
print(json.dumps(configs, indent=2))
