<<<<<<< HEAD
# TODO - Candidate to add Site API Libs when working on the assignment.
=======
# TODO - Candidate to add Site API Libs when working on the assignment.
# kib changes

import requests
import random
import string
import time
import os
from dotenv import load_dotenv

class TodoSiteApiLibs:
    """
    Library to automate the Sites API (Create, Update, Delete, Verify)
    """

    def __init__(self):
        # Load credentials from environment or .env file
        load_dotenv()
        self.base_url = os.getenv("MIST_API_BASE_URL", "https://api.mist.com/api/v1")
        self.org_id = os.getenv("MIST_ORG_ID")
        self.api_token = os.getenv("MIST_API_TOKEN")

        if not self.org_id or not self.api_token:
            raise ValueError("Missing MIST_ORG_ID or MIST_API_TOKEN in environment variables or .env file")

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.api_token}"
        }

    # ===== Helper Methods =====
    def _random_name(self, prefix="AutoSite"):
        """Generate a random site name"""
        return f"{prefix}_{''.join(random.choices(string.ascii_uppercase + string.digits, k=6))}"

    # ===== API Methods =====
    def create_site(self):
        """Create a site with random name"""
        url = f"{self.base_url}/orgs/{self.org_id}/sites"
        site_name = self._random_name()
        payload = {
            "name": site_name,
            "country_code": "US",
            "timezone": "America/Los_Angeles"
        }

        print(f"Creating site: {site_name}")
        response = requests.post(url, headers=self.headers, json=payload)
        response.raise_for_status()
        data = response.json()
        print(f"Site created successfully → ID: {data['id']}, Name: {data['name']}")
        return data

    def update_site(self, site_id):
        """Update site name to another random one"""
        new_name = self._random_name("UpdatedSite")
        url = f"{self.base_url}/sites/{site_id}"
        payload = {"name": new_name}

        print(f"Updating site ID {site_id} → {new_name}")
        response = requests.put(url, headers=self.headers, json=payload)
        response.raise_for_status()
        print("Site updated successfully")
        return new_name

    def delete_site(self, site_id):
        """Delete site and verify deletion"""
        url = f"{self.base_url}/sites/{site_id}"
        print(f"Deleting site ID {site_id}")
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        print("Site deleted successfully")

        # Verify deletion
        time.sleep(2)
        verify = requests.get(url, headers=self.headers)
        if verify.status_code == 404:
            print("Verified site deletion")
        else:
            print(f"Deletion verification failed (status {verify.status_code})")

    # ===== Combined Flow =====
    def run_full_site_lifecycle(self):
        """Create, update, and delete a site in one flow"""
        try:
            site = self.create_site()
            site_id = site["id"]
            self.update_site(site_id)
            self.delete_site(site_id)
        except Exception as e:
            print(f"Error during site lifecycle: {e}")

>>>>>>> efa2975 (re creating PR)
