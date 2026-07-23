import os
import requests

hubspot_key = os.getenv('HUBSPOT_API_KEY')
request_headers = {
    "Authorization": f"Bearer {hubspot_key}",
    "Content-Type": "application/json"
}

# --- TASK 1: Update Alex Rivera's title to CEO ---
alex_email = "alex.rivera@example.com"
search_url = f"https://api.hubapi.com/crm/v3/objects/contacts/{alex_email}?idProperty=email"
check_response = requests.get(search_url, headers=request_headers)

alex_data = {
    "properties": {
        "firstname": "Alex",
        "lastname": "Rivera",
        "jobtitle": "CEO"
    }
}

if check_response.status_code == 200:
    contact_id = check_response.json()['id']
    update_url = f"https://api.hubapi.com/crm/v3/objects/contacts/{contact_id}"
    update_res = requests.patch(update_url, headers=request_headers, json=alex_data)
    print(f"Updated Alex Rivera ({contact_id}) to CEO: {update_res.status_code}")
else:
    print("Alex Rivera not found for update.")

# --- TASK 2: Create a Brand New Contact ---
new_contact_data = {
    "properties": {
        "email": "sarah.jenkins@example.com",
        "firstname": "Sarah",
        "lastname": "Jenkins",
        "company": "Apex Global",
        "jobtitle": "CTO"
    }
}

create_url = "https://api.hubapi.com/crm/v3/objects/contacts"
create_res = requests.post(create_url, headers=request_headers, json=new_contact_data)
print(f"Created New Contact Status: {create_res.status_code}")
print(create_res.json())
