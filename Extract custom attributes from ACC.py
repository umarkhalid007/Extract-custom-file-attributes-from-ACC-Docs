# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 10:33:12 2025

@author: Umar Khalid

"""
import requests

def get_top_folders(hub_id, project_id, access_token):
    """
    Retrieves the top-level folders for a given Autodesk project.

    Args:
        hub_id (str): The hub ID
        project_id (str): The project ID
        access_token (str): OAuth access token.

    Returns:
        dict: JSON response from the API.
    """
    url = f"https://developer.api.autodesk.com/project/v1/hubs/{hub_id}/projects/{project_id}/topFolders"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")


hub_id = ""         # Provide your Hub ID
project_id = ""     # Provide your Project ID
access_token = ""   # Replace with your actual OAuth token


try:
    top_folders = get_top_folders(hub_id, project_id, access_token)
    print(top_folders)
except Exception as e:
    print(e)

def get_folder_contents(project_id, folder_id, access_token):
    """
    Retrieves the contents of a folder in an Autodesk BIM 360 or ACC project.

    Args:
        project_id (str): The project ID.
        folder_id (str): The folder ID (URL-encoded URN).
        access_token (str): OAuth access token.

    Returns:
        dict: JSON response from the API.
    """
    url = f"https://developer.api.autodesk.com/data/v1/projects/{project_id}/folders/{folder_id}/contents"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")
        

folder_id = ""  # Provide the folder (URL-encoded URN) extract from "get_top_folders" function


try:
    contents = get_folder_contents(project_id, folder_id, access_token)
    print(contents)
except Exception as e:
    print(e)
    
    

def batch_get_custom_attributes(project_id, access_token, item_or_version_ids=None):
    """
    Retrieves custom attribute values for multiple documents using item IDs or version IDs.

    Args:
        project_id (str): The UUID of the project (without the 'b.' prefix).
        access_token (str): OAuth access token.
        item_or_version_ids (list): List of item IDs or version IDs.

    Returns:
        dict: JSON response from the API.
    """
    url = f"https://developer.api.autodesk.com/bim360/docs/v1/projects/{project_id}/versions:batch-get"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }


    payload = {}

    payload["urns"] = item_or_version_ids

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")


item_ids = [] # Provide the list of item_ids extracted from "get_folder_contents" function

try:
    result = batch_get_custom_attributes(project_id, access_token, item_ids=item_ids)
    print(result)
except Exception as e:
    print(e)
