import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

config = discovery.get_configuration('{environment_id}', '{configuration_id}')
print(json.dumps(config, indent=2))
