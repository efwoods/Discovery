import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

environment_info = discovery.list_environment('{environment_id}')
print(json.dumps(environment_info, indent=2))
