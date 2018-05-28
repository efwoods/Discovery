import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

with open(os.path.join(os.getcwd(), 'config_update.json')) as config_data:
    data = json.load(config_data)
    updated_config = discovery.update_configuration('{environment_id}', '{configuration_id}', data['name'], data['description'], data['conversions'], data['enrichments'], data['normalizations'])
print(json.dumps(updated_config, indent=2))
