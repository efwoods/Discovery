#Finally, use the GET /v1/environments/{environment_id}/collections/{collection_id}/query method to search your collection of documents.

#The following example returns all entities that are called IBM. Replace {username}, {password}, {environment_id} and {configuration_id} with your information:

curl -u "9a07247a-21ec-4aee-a8ed-4bce6ba9e36e":"{password}" 'https://gateway.watsonplatform.net/discovery/api/v1/environments/{environment_id}/collections/{collection_id}/query?version=2017-11-07&query=enriched_text.entities.text:IBM'

"9a07247a-21ec-4aee-a8ed-4bce6ba9e36e",
"BOBOzbwxJyCj"
"622177b8-ffe3-4fdd-b1ab-75d6e46a3d25",
"38938952-3018-4190-9354-6582a0fc7cfe",
