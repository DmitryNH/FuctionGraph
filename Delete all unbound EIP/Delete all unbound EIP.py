# -*- coding:utf-8 -*-
import json
import requests

def handler (event, context):
    #Get Token
    token = context.getToken()
    #Get ProjectID
    projectid = context.getProjectID()
    #Form URL endpoint with fetched project ID
    api_url = f"https://vpc.ru-moscow-1.hc.sbercloud.ru/v1/{projectid}/publicips"
    #Set Headers with fetched token
    headers =  {"Content-Type":"application/json", "X-Auth-Token":token}
    #Form API request 
    response = requests.get(api_url, headers=headers)
    #Json to string for parsing
    data = json.loads(response.text)
    #Json array
    eip_data = data['publicips']
    #Check all entries in array with status DOWN(Unbound)
    for publicips in eip_data:
        if publicips['status'] == "DOWN":
            #Query EIP id
            eip_id=publicips['id']
            eip_ip=publicips['public_ip_address']
            #Form URL endpoint with fetched project ID and EIP id
            api_url = f"https://vpc.ru-moscow-1.hc.sbercloud.ru/v1/{projectid}/publicips/{eip_id}"
            #Form API request 
            delete_eip = requests.delete(api_url, headers=headers)
            print("EIP",eip_ip,"id:",eip_id,"was successfully released")

    return True
