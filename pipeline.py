import os
import requests

# Pull the API key from GitHub's secret environment
hubspot_key = os.getenv('HUBSPOT_API_KEY')
email = "alex.rivera@example.com"
search_url = f"https://api.hubapi.com/crm/v3/objects/contacts/{email}?idProperty=email"

request_headers = {
    "Authorization": f"Bearer {hubspot_key}",
    "Content-Type": "application/json"
}

contact_data = {
    "properties": {
        "firstname": "Alex",
        "lastname": "Rivera",
        "jobtitle": "VP of Operations" 
    }
}

# 1. Check if contact exists
check_response = requests.get(search_url, headers=request_headers)

if check_response.status_code == 200:
    # 2. Update if they exist
    contact_id = check_response.json()['id']
    update_url = f"https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}"
    requests.patch(update_url, headers=request_headers, json=contact_data)
    print(f"Updated Contact: {contact_id}")
else:
    # 3. Create if they do not exist
    create_url = "https://api.hubapi.com/crm/v3/objects/contacts"
    contact_data["properties"]["email"] = email
    requests.post(create_url, headers=request_headers, json=contact_data)
    print("Created New Contact")
