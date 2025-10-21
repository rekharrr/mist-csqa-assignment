# TODO - Candidate to add Site API Tests when working on the assignment.
import requests
import random
import string
import time

# ===== Configuration =====
API_BASE_URL = "https://api.mist.com/api/v1"
ORG_ID = "000000ab-00ab-00ab-00ab-0000000000ab"
API_TOKEN = "api_toke" # i tried to get auth token and getting 401 error

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Token {API_TOKEN}"
}

# ===== Helper Functions =====
def random_site_name(prefix="TestSite"):
    """Generate a random site name."""
    return f"{prefix}_{''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}"

def create_site():
    """Create a site with random name."""
    url = f"{API_BASE_URL}/orgs/{ORG_ID}/sites"
    site_name = random_site_name()
    payload = {
        "name": site_name,
        "country_code": "US",
        "timezone": "America/Los_Angeles"
    }

    print(f"Creating site: {site_name}")
    response = requests.post(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    site_data = response.json()
    print(f"Created site ID: {site_data['id']}")
    return site_data

def update_site(site_id):
    """Update the site name to a new random name."""
    new_name = random_site_name("UpdatedSite")
    url = f"{API_BASE_URL}/sites/{site_id}"
    payload = {"name": new_name}

    print(f"Updating site ID {site_id} → {new_name}")
    response = requests.put(url, headers=HEADERS, json=payload)
    response.raise_for_status()
    print(f"Site updated successfully")
    return new_name

def delete_site(site_id):
    """Delete the site and verify deletion."""
    url = f"{API_BASE_URL}/sites/{site_id}"
    print(f"Deleting site ID {site_id}")
    response = requests.delete(url, headers=HEADERS)
    response.raise_for_status()
    print("Site deleted")

    # Verify deletion
    time.sleep(2)  # small delay before verify
    verify_response = requests.get(url, headers=HEADERS)
    if verify_response.status_code == 404:
        print("Verified site deletion")
    else:
        print(f" Deletion verification failed. Status: {verify_response.status_code}")

# ===== Main Flow =====
if __name__ == "__main__":
    try:
        created_site = create_site()
        site_id = created_site["id"]

        updated_name = update_site(site_id)
        print(f"Updated site name: {updated_name}")

        delete_site(site_id)
    except Exception as e:
        print(f"Error: {e}")
