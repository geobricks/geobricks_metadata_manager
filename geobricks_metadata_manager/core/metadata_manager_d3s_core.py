import requests
import json
from geobricks_metadata_manager.utils.log import logger

log = logger("geobricks_metadata_manager.metadata_manager_d3s_core")


class MetadataManager():

    config = None
    url_create_metadata = None #"POST"
    url_get_metadata_uid = None #"GET"
    url_get_metadata = None #"POST"

    def __init__(self, config):
        # settings
        self.config = config
        # mapping the urls
        try:
            self.url_create_metadata = config["url_create_metadata"]
            self.url_get_metadata_uid = config["url_get_metadata_uid"]
            self.url_get_metadata = config["url_get_metadata"]
        except Exception, e:
            raise Exception("Not all the urls are mapped: " + e)

    def publish_metadata(self, payload, overwrite=False):
        #TODO: use overwrite
        '''
        Create a new metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.url_create_metadata, data=json.dumps(payload), headers=headers)
        if r.status_code is not 201:
            raise Exception(r.text)
        return json.loads(r.text)

    def delete_metadata(self, uid):
        '''
        Create a new metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.url_create_metadata, data=json.dumps(uid), headers=headers)
        if r.status_code is not 201:
            raise Exception(r.text)
        return json.loads(r.text)

    def get_by_uid(self, uid):
        '''
        Get metadata through his uid
        :param uid: String of the uid
        :return: the json containing the metadata
        '''
        url = self.url_get_metadata_uid.replace("<uid>", uid);
        r = requests.get(url)
        log.info(r.text)
        log.info(r.status_code)
        if r.status_code is not 200:
            raise Exception(r.text)
        return json.loads(r.text)

    def get_all_layers(self):
        q = {
            "meContent.resourceRepresentationType" : {
                "enumeration" : ["geographic"]
            }
        }
        headers = {'Content-Type': 'application/json'}
        r = requests.post(self.url_get_metadata, data=json.dumps(q), headers=headers)
        log.info(r.text)
        log.info(r.status_code)
        if r.status_code is not 200:
            raise Exception(r.text)
        return json.loads(r.text)