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
    # The following example shows how to set the request URL and parameters.
    # Set request Endpoint.
    # Specify a request method, such as GET, PUT, POST, DELETE, HEAD, and PATCH.
    # Set request URI.
    # Set parameters for the request URL.
    user_url = "https://iam.ru-moscow-1.hc.sbercloud.ru/v3/users"
    api_url = signer.HttpRequest("GET", user_url)
    # Add header parameters, for example, x-domain-id for invoking a global service and x-project-id for invoking a project-level service.
    api_url.headers = {"Content-Type":"application/json;charset=utf8", "X-Domain-Id":account_id}
    # Sign 
    sig.Sign(api_url)
    # Form request to API
    response = requests.request(api_url.method, api_url.scheme + "://" + api_url.host + api_url.uri, headers=api_url.headers)
    # Json to string for parsing
    data = json.loads(response.text)
    # Json array
    user_data = data['users']
    # Query iser ID in JSON Array
    for users in user_data:
        #Set iser ID variable
        user_id=users['id']
        # Set request URI.
        # Set parameters for the request URL.
        detail_url = f"https://iam.ru-moscow-1.hc.sbercloud.ru/v3.0/OS-USER/users/{user_id}"
        detail_api_url = signer.HttpRequest("GET", detail_url)
        detail_api_url.headers = {"Content-Type":"application/json;charset=utf8", "X-Domain-Id":account_id}
        # Sign 
        sig.Sign(detail_api_url)
        # Form request to API
        response = requests.request(detail_api_url.method, detail_api_url.scheme + "://" + detail_api_url.host + detail_api_url.uri, headers=detail_api_url.headers)
        # Json to string for parsing
        detail_data = json.loads(response.text)
        # Query user details
        name = detail_data["user"]["name"]
        email = detail_data["user"]["email"]
        phone = detail_data["user"]["phone"]
        print("name:",name,"| email:",email,"| phone:",phone)   

    return True
