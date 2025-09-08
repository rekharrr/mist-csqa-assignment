import logging
from datetime import datetime
from libs.api_libs.constants import api_constants
from utils.api_utils.api_utils import CommonAPIUtils
import os
import json

class GenericOrgLibs(object):
    """
        Class that holds the Generic Functions for the Site Set Up.
    """

    def create_random_org_name(self):
        """
        Creating the Org Name.
        :return: The Org Name.
        """
        return "Automation Org " + str(datetime.now())[0:16]

    def get_sample_org_config(self):
        org_config_file = os.path.abspath(__file__ + "/../") + "/configs/sample_org_config.json"
        with open(org_config_file)  as org_default_payload:
            data = json.load(org_default_payload)
        return data


class OrgAPILibs(GenericOrgLibs):
    """
      Class that holds the Generic Org Setup Related functionalities.
      This class inherits the GenericOrgLibs.
    """

    def __init__(self):
        """
        OrgAPILibs():: Having __init__ method in here for initializing any attributes if needed"
        """

    def _op_create_org(self, env, org_payload=None):
        logging.info("{} :: {} :: Trying to create a Organization".format(self.__class__.__name__,
                                                                          self.__class__._op_create_org.__name__))
        create_org_url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_ORGS
        create_org_data = super(OrgAPILibs, self).get_sample_org_config()
        if org_payload is not None:
            create_org_data.update(org_payload)
        else:
            create_org_data['name'] = super(OrgAPILibs, self).create_random_org_name()

        logging.info("{} :: {} :: Org name is set as {} ".format(self.__class__.__name__,
                                                                 self.__class__._op_create_org.__name__,
                                                                 create_org_data['name']))
        response = CommonAPIUtils().post_request_with_status_code_validation(create_org_url, create_org_data, 200)
        logging.info("{} :: {} :: Org has been created Successfully".format(self.__class__.__name__,
                                                                            self.__class__._op_create_org.__name__))
        return response

    def _get_org_details(self, env, org_id):
        logging.info("{} :: {} :: Trying to GET the org details for Org with ID {}".format(self.__class__.__name__,
                                                                                           self.__class__._get_org_details.__name__,
                                                                                           org_id))
        org_details_url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_ORG_DETAILS.format(org_id)
        org_details = CommonAPIUtils().get_request_with_status_code_validation(org_details_url, 200)
        return org_details

    def _op_update_org(self, env, org_id, org_payload):
        logging.info("{} :: {} :: Trying to Update a Org".format(
            self.__class__.__name__,
            self.__class__._op_update_org.__name__))
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_ORG_DETAILS.format(org_id)
        response = CommonAPIUtils().put_request_with_status_code_validation(url, org_payload, 200)
        logging.info("{} :: {} :: Org was updated successfully".format(
            self.__class__.__name__,
            self.__class__._op_update_org.__name__))
        return response

    def _op_delete_org(self, env, org_id):
        logging.info("{} :: {} :: Trying to delete a Org by its ID".format(
            self.__class__.__name__,
            self.__class__._op_delete_org.__name__))
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_ORG_DETAILS.format(org_id)
        CommonAPIUtils().delete_request_with_status_code_validation(url, 200)
        logging.info("{} :: {} :: Org was deleted successfully".format(
            self.__class__.__name__,
            self.__class__._op_delete_org.__name__))

    def _op_get_self(self, env, api_token=None):
        url = api_constants.CONST_EXT_API_URLs[env] + api_constants.CONST_API_SELF
        return CommonAPIUtils().get_request_with_status_code_validation(url, 200)

    def get_list_of_org_ids_for_user(self, env):
        logging.info("{} :: {} :: Trying to GET the list of ORG IDs that the account has access".format(
            self.__class__.__name__,
            self.__class__._op_update_org.__name__))
        org_ids = []
        self_api = self._op_get_self(env)
        for org_count in range(0, len(self_api["privileges"])):
            if self_api["privileges"][org_count]["scope"] == "org":
                current_org_id = self_api['privileges'][org_count]['org_id']
                org_ids.append(current_org_id)
        return org_ids

    def _is_org_present(self, env, org_id):
        logging.info(
            "{} :: {} :: Trying to check if the given org_id is present in the list of orgs that the user has access to.".format(
                self.__class__.__name__, self.__class__._is_org_present.__name__))
        org_ids = self.get_list_of_org_ids_for_user(env)
        if org_id in org_ids:
            logging.info(
                "{} :: {} :: Given org exists in the list of orgs that user has access to".format(
                    self.__class__.__name__, self.__class__._is_org_present.__name__))
            return True
        else:
            logging.info(
                "{} :: {} :: Given org doesnt exist in the list of orgs that user has access to.".format(
                    self.__class__.__name__, self.__class__._is_org_present.__name__))
            return False