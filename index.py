# -*- coding:utf-8 -*-
import json
import requests
from apig_sdk import signer

def handler (event, context):
    sig = signer.Signer()
    # Set the AK/SK to sign and authenticate the request.
    sig.Key = context.getAccessKey()
    sig.Secret = context.getSecretKey()
    # Set root account id
    account_id = context.getUserData('account_id')
    # The following example shows how to set the request URL and parameters to query a VPC list.
    # Set request Endpoint.
    # Specify a request method, such as GET, PUT, POST, DELETE, HEAD, and PATCH.
    # Set request URI.
    # Set parameters for the request URL.
    api_url = signer.HttpRequest("GET", "https://iam.ru-moscow-1.hc.sbercloud.ru/v3/users")
    # Add header parameters, for example, x-domain-id for invoking a global service and x-project-id for invoking a project-level service.
    api_url.headers = {"Content-Type":"application/json;charset=utf8", "X-Domain-Id":account_id}
    # Add a body if you have specified the PUT or POST method. Special characters, such as the double quotation mark ("), contained in the body must be escaped.
    sig.Sign(api_url)
    response = requests.request(api_url.method, api_url.scheme + "://" + api_url.host + api_url.uri, headers=api_url.headers)
    # Json to string for parsing
    data = json.loads(response.text)
    # Json array
    user_data = data['users']
    #print(data)
    # comment 
    for users in user_data:
        #Query EIP id
        name=users['name']
        email=users['email']
        print("name:",name,"| email:",email)   

    return True