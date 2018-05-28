import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

with open(os.path.join(os.getcwd(), 'config.json')) as config_data:
    data = json.load(config_data)
    new_config = discovery.create_configuration('{environment_id}', data['name'], data['description'], data['conversions'], data['enrichments'], data['normalizations'])
print(json.dumps(new_config, indent=2))
