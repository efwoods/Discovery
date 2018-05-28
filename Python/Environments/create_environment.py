import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

response = discovery.create_environment(
    name="my_environment",
    description="My environment"
)

print(json.dumps(response, indent=2))
