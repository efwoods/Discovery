import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

environments = discovery.list_environments()
print(json.dumps(environments, indent=2))

news_environments = [x for x in environments['environments'] if x['name'] == 'Watson Discovery News Environment']
news_environment_id = news_environments[0]['environment_id']
print(json.dumps(news_environment_id, indent=2))

collections = discovery.list_collections(news_environment_id)
news_collections = [x for x in collections['collections']]
print(json.dumps(news_collections, indent=2))
