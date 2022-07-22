# -*- coding:utf-8 -*-
import json
import requests
from datetime import datetime, date

def handler (event, context):
    #Get Token
    token = context.getToken()
    #Set Retention days
    retention_days = 15
    #Set minimum images count
    images_count = 2
    #Set Organization Name
    Org_name = "dimal"
    #Set Image Name
    Image_Name = "mern-front"
    #Form URL endpoint - image info
    get_image_info_url = f"https://swr-api.ru-moscow-1.hc.sbercloud.ru/v2/manage/namespaces/{Org_name}/repos/{Image_Name}/tags"
    #Form URL endpoint - image count
    get_image_num_url = f"https://swr-api.ru-moscow-1.hc.sbercloud.ru/v2/manage/repos?filter=center::self|namespace::{Org_name}|name::{Image_Name}"
    #Set Headers with fetched token
    headers =  {"Content-Type":"application/json", "X-Auth-Token":token}
    #Form API requests
    get_image_info_req = requests.get(get_image_info_url, headers=headers)
    get_image_num_req = requests.get(get_image_num_url, headers=headers)
    #Json to string for parsing
    get_image_num_data = json.loads(get_image_num_req.text)
    #Get current image count
    for images_num in get_image_num_data:
        current_images_count = images_num['num_images']
        print(f"current images count:{current_images_count}")
    #Json to string for parsing
    get_image_info_data = json.loads(get_image_info_req.text)
    #Get current date
    current_date = datetime.now().date()
    i=1
    #Get updated data information and delete images accroding to images_count and retention_days variables
    for images in get_image_info_data:
        if i > images_count:
            updated_datetime = images['updated']
            updated_datetime = datetime.strptime(updated_datetime, "%Y-%m-%dT%H:%M:%S.%fZ")
            created_date = updated_datetime.date()
            delta = current_date - created_date
            delta = delta.days
            if delta > retention_days:
                image_tag = images['Tag']
                delete_image_url = f"https://swr-api.ru-moscow-1.hc.sbercloud.ru/v2/manage/namespaces/{Org_name}/repos/{Image_Name}/tags/{image_tag}"
                delete_request = requests.delete(delete_image_url, headers=headers)
                print(f"image {Image_Name}:{image_tag} was deleted, delta days:{delta}")
        i+=1

    return True
