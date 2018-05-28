import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

del_env = discovery.delete_environment('{environment_id}')
print(json.dumps(del_env, indent=2))
