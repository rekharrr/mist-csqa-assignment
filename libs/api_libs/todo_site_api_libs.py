import logging
from datetime import datetime
from libs.api_libs.constants import api_constants
from utils.api_utils.api_utils import CommonAPIUtils
import os
import json

class GenericSiteLibs(object):
    """
        Class that holds the Generic Functions for the Site Set Up.
    """

    def create_random_site_name(self):
        """
        Creating the Site Name.
        :return: The Site Name.
        """
        return "Automation Site " + str(datetime.now())[0:16]

    def get_sample_site_config(self):
        site_config_file = os.path.abspath(__file__ + "/../") + "/configs/sample_site_config.json"
        with open(site_config_file) as site_default_payload:
            data = json.load(site_default_payload)
        return data


class SiteAPILibs(GenericSiteLibs):
    """
      Class that holds the Generic Site Setup Related functionalities.
      This class inherits the GenericSiteLibs.
    """

    def __init__(self):
        """
        SiteAPILibs():: Having __init__ method in here for initializing any attributes if needed"
        """

    def _op_create_site(self, env, org_id, site_payload=None):
        logging.info("{} :: {} :: Trying to create a Site".format(self.__class__.__name__,
                                                                   self.__class__._op_create_site.__name__))
        create_site_url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITES.format(org_id)
        create_site_data = super(SiteAPILibs, self).get_sample_site_config()
        if site_payload is not None:
            create_site_data.update(site_payload)
        else:
            create_site_data['name'] = super(SiteAPILibs, self).create_random_site_name()

        logging.info("{} :: {} :: Site name is set as {} ".format(self.__class__.__name__,
                                                                   self.__class__._op_create_site.__name__,
                                                                   create_site_data['name']))
        response = CommonAPIUtils().post_request_with_status_code_validation(create_site_url, create_site_data, 200)
        logging.info("{} :: {} :: Site has been created Successfully".format(self.__class__.__name__,
                                                                             self.__class__._op_create_site.__name__))
        return response

    def _get_site_details(self, env, site_id):
        logging.info("{} :: {} :: Trying to GET the site details for Site with ID {}".format(
            self.__class__.__name__,
            self.__class__._get_site_details.__name__,
            site_id))
        site_details_url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITE_DETAILS.format(site_id)
        site_details = CommonAPIUtils().get_request_with_status_code_validation(site_details_url, 200)
        return site_details

    def _op_update_site(self, env, site_id, site_payload):
        logging.info("{} :: {} :: Trying to Update a Site".format(
            self.__class__.__name__,
            self.__class__._op_update_site.__name__))
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITE_DETAILS.format(site_id)
        response = CommonAPIUtils().put_request_with_status_code_validation(url, site_payload, 200)
        logging.info("{} :: {} :: Site was updated successfully".format(
            self.__class__.__name__,
            self.__class__._op_update_site.__name__))
        return response

    def _op_delete_site(self, env, site_id):
        logging.info("{} :: {} :: Trying to delete a Site by its ID".format(
            self.__class__.__name__,
            self.__class__._op_delete_site.__name__))
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITE_DETAILS.format(site_id)
        CommonAPIUtils().delete_request_with_status_code_validation(url, 200)
        logging.info("{} :: {} :: Site was deleted successfully".format(
            self.__class__.__name__,
            self.__class__._op_delete_site.__name__))

    def get_list_of_site_ids_for_org(self, env, org_id):
        logging.info("{} :: {} :: Trying to GET the list of Site IDs for the Org".format(
            self.__class__.__name__,
            self.__class__.get_list_of_site_ids_for_org.__name__))
        site_ids = []
        sites_url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITES.format(org_id)
        sites_list = CommonAPIUtils().get_request_with_status_code_validation(sites_url, 200)
        
        # The response is a list of sites
        for site in sites_list:
            site_ids.append(site['id'])
        return site_ids

    def _is_site_present(self, env, org_id, site_id):
        logging.info(
            "{} :: {} :: Trying to check if the given site_id is present in the list of sites for the org.".format(
                self.__class__.__name__, self.__class__._is_site_present.__name__))
        site_ids = self.get_list_of_site_ids_for_org(env, org_id)
        if site_id in site_ids:
            logging.info(
                "{} :: {} :: Given site exists in the list of sites for the org".format(
                    self.__class__.__name__, self.__class__._is_site_present.__name__))
            return True
        else:
            logging.info(
                "{} :: {} :: Given site doesnt exist in the list of sites for the org.".format(
                    self.__class__.__name__, self.__class__._is_site_present.__name__))
            return False
