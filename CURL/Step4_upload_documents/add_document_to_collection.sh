#Now, add the example documents to your collection. This example uploads the document test-doc1.html to your collection. Replace {username}, {password}, {environment_id} and {configuration_id} with your information. Modify the location of the sample document to point to where you saved the test-doc1.html file.

#Use the POST /v1/environments/{environment_id}/collections/{collection_id}/documents method:

curl -X POST -u "9a07247a-21ec-4aee-a8ed-4bce6ba9e36e":"BOBOzbwxJyCj" -F "file=@test-doc4.html" https://gateway.watsonplatform.net/discovery/api/v1/environments/622177b8-ffe3-4fdd-b1ab-75d6e46a3d25/collections/38938952-3018-4190-9354-6582a0fc7cfe/documents?version=2017-11-07
