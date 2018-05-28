import os
import json
from watson_developer_cloud import DiscoveryV1

discovery = DiscoveryV1(
    version="2018-03-05",
    username="{username}",
    password="{password}"
)

with open(os.path.join(os.getcwd(), '{path_element}', '{filename}')) as fileinfo:
    add_doc = discovery.add_document('{environment_id}', '{collection_id}', file=fileinfo)
print(json.dumps(add_doc, indent=2))
