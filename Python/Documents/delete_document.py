import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

delete_doc = discovery.delete_document('{environment_id}', '{collection_id}', '{document_id}')
print(json.dumps(delete_doc, indent=2))
