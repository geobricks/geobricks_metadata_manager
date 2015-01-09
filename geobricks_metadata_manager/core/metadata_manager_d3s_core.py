import requests
import json
from geobricks_common.core.log import logger

log = logger(__file__)


class MetadataManager():

    config = None
    url_create_metadata = None #"POST"
    url_create_coding_system = None #"POST"
    url_get_metadata_uid = None #"GET"
    url_get_metadata = None #"POST"
    url_delete_metadata= None #"DELETE"

    def __init__(self, config):
        # getting the settings
        config = config["settings"]
        self.config = config
        # mapping the urls
        try:
            self.url_create_metadata = config["metadata"]["url_create_metadata"]
            self.url_create_coding_system = config["metadata"]["url_create_coding_system"]
            self.url_get_metadata_uid = config["metadata"]["url_get_metadata_uid"]
            self.url_get_metadata = config["metadata"]["url_get_metadata"]
            self.url_delete_metadata = config["metadata"]["url_delete_metadata"]
            self.url_overwrite_dsd_rid = config["metadata"]["url_overwrite_dsd_rid"]


        except Exception, e:
            log.error(e)
            raise Exception("Not all the urls are mapped: " + str(e))

        # setting logging properties
        if "logger" in config:
            if "level" in config["logger"]:
                log.setLevel(config["logger"]["level"])

    def publish_metadata(self, payload, overwrite=False):
        #TODO: use overwrite
        '''
        Create a new metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        log.info(json.dumps(payload))
        log.info(overwrite)
        if overwrite:
            r = requests.put(self.url_create_metadata, data=json.dumps(payload), headers=headers)
            if r.status_code is not 200:
                raise Exception(r)
        else:
            r = requests.post(self.url_create_metadata, data=json.dumps(payload), headers=headers)
            if r.status_code is not 201:
                raise Exception(r)
        return json.loads(r.text)

    def update_metadata(self, payload, overwrite=False):
        #TODO: use overwrite
        '''
        Update a metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        if overwrite:
            r = requests.put(self.url_create_metadata, data=json.dumps(payload), headers=headers)
            if r.status_code is not 200:
                raise Exception(r)
        else:
            r = requests.patch(self.url_create_metadata, data=json.dumps(payload), headers=headers)
            if r.status_code is not 200:
                raise Exception(r)
        return json.loads(r.text)

    def overwrite_dsd_rid(self, payload):
        '''
        Overwrite a dsd using its rid
        :param payload: json string containing the metadata information to overwrite the rid
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        r = requests.put(self.url_overwrite_dsd_rid, data=json.dumps(payload), headers=headers)
        if r.status_code is not 200:
            raise Exception(r)
        return json.loads(r.text)

    def publish_coding_system(self, payload, overwrite=False):
        '''
        Create a new metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        if overwrite:
            r = requests.put(self.url_create_coding_system, data=json.dumps(payload), headers=headers)
            if r.status_code is not 200:
                raise Exception(r)
        else:
            r = requests.post(self.url_create_coding_system, data=json.dumps(payload), headers=headers)
            if r.status_code is not 201:
                raise Exception(r)
        return json.loads(r.text)

    def update_coding_system(self, payload, overwrite=False):
        '''
        Create a new metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        if overwrite:
            r = requests.put(self.url_create_coding_system, data=json.dumps(payload), headers=headers)
            if r.status_code is not 200:
                raise Exception(r)
        else:
            r = requests.patch(self.url_create_coding_system, data=json.dumps(payload), headers=headers)
            if r.status_code is not 201:
                raise Exception(r)
        return json.loads(r.text)

    def delete_metadata(self, uid):
        '''
        Create a new metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        log.info("delete_metadata")
        url = self.url_delete_metadata.replace("<uid>", uid)
        r = requests.delete(url)
        if r.status_code is not 200:
            raise Exception(r)
        return True #There is no r.text in that case

    def get_by_uid(self, uid, full=True, dsd=True):
        '''
        Get metadata through his uid (proxy to D3S)
        :param uid: String of the uid
        :return: the json containing the metadata
        '''
        url = self.url_get_metadata_uid.replace("<uid>", uid)
        url += "?full=" + str(full) + "&dsd=" + str(dsd)
        r = requests.get(url)
        log.info(r.text)
        log.info(r.status_code)
        if r.status_code is not 200:
            raise Exception(r.text)
        return json.loads(r.text)

    def get_all_layers(self, full=True, dsd=True):
        q = {
            "meContent.resourceRepresentationType": {
                "enumeration": ["geographic"]
            }
        }
        headers = {'Content-Type': 'application/json'}
        url = self.url_get_metadata
        url += "?full=" + str(full) + "&dsd=" + str(dsd)

        r = requests.post(url, data=json.dumps(q), headers=headers)
        if r.status_code is not 201: # TODO: why 201?
            raise Exception(r.text)
        return json.loads(r.text)