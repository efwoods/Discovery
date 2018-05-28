import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

my_query = discovery.query(environment_id='{environment_id}', collection_id='{collection_id}', query='{query}', filter='{filter}', aggregation='{aggregation}', return_fields='{return_fields}' ...)
print(json.dumps(my_query, indent=2))
