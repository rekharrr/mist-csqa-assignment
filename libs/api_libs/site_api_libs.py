import logging
from datetime import datetime
from libs.api_libs.constants import api_constants
from utils.api_utils.api_utils import CommonAPIUtils
import os
import json


class GenericSiteLibs(object):
    """
        Class that holds the Generic Functions for Site Set Up.
    """

    def create_random_site_name(self):
        """
        Create a random Site name with timestamp.
        """
        return "Automation Site " + str(datetime.now())[0:16]

    def get_sample_site_config(self):
        """
        Load the default Site payload JSON.
        """
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
        SiteAPILibs():: Having __init__ method in here for initializing any attributes if needed
        """

    def _op_create_site(self, env, org_id, site_payload=None):
        logging.info("{} :: {} :: Trying to create a Site".format(
            self.__class__.__name__,
            self.__class__._op_create_site.__name__))

        create_site_url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SITES.format(org_id)
        create_site_data = super(SiteAPILibs, self).get_sample_site_config()

        if site_payload is not None:
            create_site_data.update(site_payload)
        else:
            create_site_data['name'] = super(SiteAPILibs, self).create_random_site_name()

        logging.info("{} :: {} :: Site name is set as {} ".format(
            self.__class__.__name__,
            self.__class__._op_create_site.__name__,
            create_site_data['name']))

        response = CommonAPIUtils().post_request_with_status_code_validation(create_site_url, create_site_data, 200)
        logging.info("{} :: {} :: Site has been created Successfully".format(
            self.__class__.__name__,
            self.__class__._op_create_site.__name__))
        return response

    def _get_site_details(self, env, site_id):
        logging.info("{} :: {} :: Trying to GET the Site details for Site ID {}".format(
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

    def _is_site_present(self, env, site_id):
        """
        Check if a site exists by trying to get its details.
        
        Args:
            env: Environment (production, etc.)
            site_id: Site ID to check
            
        Returns:
            bool: True if site exists, False otherwise
        """
        logging.info("{} :: {} :: Trying to check if site {} exists".format(
            self.__class__.__name__,
            self.__class__._is_site_present.__name__,
            site_id))
        
        try:
            site_details = self._get_site_details(env, site_id)
            if site_details and site_details.get("id") == site_id:
                logging.info("{} :: {} :: Site {} exists".format(
                    self.__class__.__name__,
                    self.__class__._is_site_present.__name__,
                    site_id))
                return True
            else:
                logging.info("{} :: {} :: Site {} does not exist".format(
                    self.__class__.__name__,
                    self.__class__._is_site_present.__name__,
                    site_id))
                return False
        except Exception as e:
            logging.info("{} :: {} :: Site {} does not exist (exception: {})".format(
                self.__class__.__name__,
                self.__class__._is_site_present.__name__,
                site_id,
                str(e)))
            return False
