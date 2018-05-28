import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

doc_info = discovery.get_document_status('{environment_id}', '{collection_id}', '{document_id}')
print(json.dumps(doc_info, indent=2))
