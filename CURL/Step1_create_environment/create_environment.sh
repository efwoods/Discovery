#Issue the following command to create an environment that is called my-first-environment. Replace {username} and {password} with the service credentials you copied earlier:

curl -X POST -u "9a07247a-21ec-4aee-a8ed-4bce6ba9e36e":"BOBOzbwxJyCj" -H "Content-Type: application/json" -d '{ "name":"my-first-environment", "description":"exploring environments"}' "https://gateway.watsonplatform.net/discovery/api/v1/environments?version=2017-11-07"

