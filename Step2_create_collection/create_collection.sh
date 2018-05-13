#Use the POST /v1/environments/{environment_id}/collections method to create a collection called my-first-collection. Replace {username}, {password}, {environment_id} and {configuration_id} with your information:

curl -X POST -u "9a07247a-21ec-4aee-a8ed-4bce6ba9e36e":"BOBOzbwxJyCj" -H "Content-Type: application/json" -d '{"name": "my-first-collection", "description": "exploring collections", "configuration_id":"42e016bb-e6b6-4c57-9638-766fce8067ba" , "language": "en_us"}' https://gateway.watsonplatform.net/discovery/api/v1/environments/622177b8-ffe3-4fdd-b1ab-75d6e46a3d25/collections?version=2017-11-07

