
# Extracting Custom Attributes from ACC/BIM 360 Docs

This Python script demonstrates how to interact with Autodesk Construction Cloud (ACC) / BIM 360 Docs APIs to extract custom attributes from project documents.

## 📋 Prerequisites

- Autodesk Developer Account
- OAuth Access Token with appropriate scopes
- Python 3.x

## ⚙️ Setup

1. Clone this repository or copy the script.
2. Replace the placeholders for `hub_id`, `project_id`, `access_token`, `folder_id`, and `item_ids` with actual values.

## 🚀 Usage

The script includes three main functions:

### 1. `get_top_folders(hub_id, project_id, access_token)`
Retrieves the top-level folders of a project.

### 2. `get_folder_contents(project_id, folder_id, access_token)`
Fetches the contents (items and subfolders) of a specified folder.

### 3. `batch_get_custom_attributes(project_id, access_token, item_or_version_ids)`
Extracts custom attributes for a list of item or version URNs.

## 🔄 API Flow

1. **Get Top Folders**: Identify root folders in the project.
2. **Get Folder Contents**: Drill down into folders to find items.
3. **Get Custom Attributes**: Retrieve metadata for selected items.

## 📎 Example
```python
hub_id = "your_hub_id"
project_id = "your_project_id"
access_token = "your_access_token"
folder_id = "your_folder_id"
item_ids = ["item_urn_1", "item_urn_2"]

# Step 1: Get top folders
top_folders = get_top_folders(hub_id, project_id, access_token)

# Step 2: Get folder contents
contents = get_folder_contents(project_id, folder_id, access_token)

# Step 3: Get custom attributes
attributes = batch_get_custom_attributes(project_id, access_token, item_ids)
```
