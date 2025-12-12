import pytest
import logging
from libs.api_libs.todo_site_api_libs import *
from libs.api_libs.org_api_libs import *

site_obj = SiteAPILibs()
org_obj = OrgAPILibs()

class TestSiteAPI():

    org_id = ""  # Class variable for Org ID
    site_id = ""  # Class variable for Site ID

    def test_01_create_site(self, env):
        """
        Test to create a site via API and validate the response.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {} ################".format("test_01_create_site"))
        
        # First create an Org to host the Site
        create_org = org_obj._op_create_org(env)
        TestSiteAPI.org_id = create_org['id']
        logging.info("Created Org with ID: {}".format(TestSiteAPI.org_id))

        # Now create a Site within that Org
        create_site = site_obj._op_create_site(env, TestSiteAPI.org_id)

        # Making the Site ID available for other test methods
        TestSiteAPI.site_id = create_site['id']

        assert (site_obj._is_site_present(env, TestSiteAPI.org_id, create_site['id']))

    def test_02_update_site(self, env):
        """
        Test to update an existing site via API and validate the response.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {} ################".format("test_02_update_site"))

        # Generate new Site Name
        site_payload = {"name": site_obj.create_random_site_name()}

        # Update the Site Name
        updated_site = site_obj._op_update_site(env, TestSiteAPI.site_id, site_payload)

        assert (updated_site['name'] == site_payload['name'])

    def test_03_delete_site(self, env):
        """
        Test to delete an existing site via API and validate the response.
        """
        logging.info("*********************************************************************************")
        logging.info("###################   IN TEST METHOD {} ################".format("test_03_delete_site"))

        # Delete the Site
        site_obj._op_delete_site(env, TestSiteAPI.site_id)

        assert (not site_obj._is_site_present(env, TestSiteAPI.org_id, TestSiteAPI.site_id))

        # Clean up: Delete the Org as well
        org_obj._op_delete_org(env, TestSiteAPI.org_id)
        logging.info("Cleaned up Org with ID: {}".format(TestSiteAPI.org_id))
