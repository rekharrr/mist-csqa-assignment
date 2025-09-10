import pytest
import logging
from libs.api_libs.org_api_libs import OrgAPILibs
from libs.api_libs.site_api_libs import SiteAPILibs

org_obj = OrgAPILibs()
site_obj = SiteAPILibs()


class TestSiteAPI():

    org_id = ""   # Class variable to hold Org ID
    site_id = ""  # Class variable to hold Site ID

    def test_01_create_site(self, env):
        """
        Test to create a Site under an Org via API and validate the response.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {} ################".format("test_01_create_site"))

        # First create an Org (site must belong to an Org)
        created_org = org_obj._op_create_org(env)
        TestSiteAPI.org_id = created_org["id"]

        # Create a Site in that Org
        created_site = site_obj._op_create_site(env, TestSiteAPI.org_id)
        TestSiteAPI.site_id = created_site["id"]

        assert "id" in created_site
        assert created_site["org_id"] == TestSiteAPI.org_id

    def test_02_update_site(self, env):
        """
        Test to update an existing Site and validate the response.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {} ################".format("test_02_update_site"))

        # Generate new Site Name
        site_payload = {"name": site_obj.create_random_site_name()}

        # Update the Site
        updated_site = site_obj._op_update_site(env, TestSiteAPI.site_id, site_payload)

        assert updated_site["id"] == TestSiteAPI.site_id
        assert updated_site["name"] == site_payload["name"]

    def test_03_delete_site(self, env):
        """
        Test to delete an existing Site and validate the response.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {} ################".format("test_03_delete_site"))

        # Delete the Site
        site_obj._op_delete_site(env, TestSiteAPI.site_id)

        # Verify it's gone using the verification method
        assert not site_obj._is_site_present(env, TestSiteAPI.site_id)

        # Cleanup: also delete the org created in test_01
        org_obj._op_delete_org(env, TestSiteAPI.org_id)
