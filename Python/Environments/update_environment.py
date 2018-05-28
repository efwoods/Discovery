import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

new_name = discovery.update_environment('{environment_id}', 'Updated name', 'Updated description')

print(json.dumps(new_name, indent=2))
