# TODO - Candidate to add Site API Tests when working on the assignment.

import logging
import pytest

from libs.api_libs.org_api_libs import OrgAPILibs
from libs.api_libs.site_api_libs import SiteAPILibs


@pytest.mark.site
class TestSiteAPI(object):
    """
    Test class for Site API validations
    """

    @classmethod
    def setup_class(cls):
        """
        Setup runs once before all test cases
        """
        cls.env = "dev"   # change based on env config
        cls.org_api = OrgAPILibs()
        cls.site_api = SiteAPILibs()

        # Create Org (prerequisite for Site)
        org_response = cls.org_api._op_create_org(cls.env)
        cls.org_id = org_response["id"]

        logging.info("Setup completed with Org ID: {}".format(cls.org_id))

    def test_create_site(self):
        """
        Test: Create Site
        """
        site_response = self.site_api._op_create_site(self.env, self.org_id)

        assert site_response is not None
        assert "id" in site_response
        assert "name" in site_response

        self.site_id = site_response["id"]

        logging.info("Site created with ID: {}".format(self.site_id))

    def test_get_site_details(self):
        """
        Test: Get Site Details
        """
        site_response = self.site_api._op_create_site(self.env, self.org_id)
        site_id = site_response["id"]

        site_details = self.site_api._get_site_details(
            self.env, self.org_id, site_id
        )

        assert site_details["id"] == site_id
        assert site_details["name"] == site_response["name"]

    def test_update_site(self):
        """
        Test: Update Site
        """
        site_response = self.site_api._op_create_site(self.env, self.org_id)
        site_id = site_response["id"]

        update_payload = {
            "name": "Updated Automation Site"
        }

        updated_response = self.site_api._op_update_site(
            self.env, self.org_id, site_id, update_payload
        )

        assert updated_response["name"] == update_payload["name"]

    def test_site_presence(self):
        """
        Test: Validate Site Presence
        """
        site_response = self.site_api._op_create_site(self.env, self.org_id)
        site_id = site_response["id"]

        is_present = self.site_api._is_site_present(
            self.env, self.org_id, site_id
        )

        assert is_present is True

    def test_delete_site(self):
        """
        Test: Delete Site
        """
        site_response = self.site_api._op_create_site(self.env, self.org_id)
