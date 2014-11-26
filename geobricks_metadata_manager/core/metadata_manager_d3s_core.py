import requests
import json
from geobricks_metadata_manager.utils.log import logger

log = logger("geobricks_metadata_manager.metadata_manager_d3s_core")


class MetadataManager():

    config = None
    #config.url_create_metadata = None #"POST"
    #config.url_get_metadata_uid = None #"GET"

    def __init__(self, config):
        # settings
        self.config = config
        log.info(self.config)

    def publish_metadata(self, payload):
        '''
        Create a new metadata
        :param payload: json string containing the metadata information
        :return: the result json with basic metadata
        '''
        headers = {'Content-Type': 'application/json'}
        print self.config['url_create_metadata']
        r = requests.post(self.config['url_create_metadata'], data=json.dumps(payload), headers=headers)
        if r.status_code is not 201:
            raise Exception(r.text, r.status_code)
        return json.loads(r.text)

    def get_metadata_uid(self, uid):
        '''
        Get metadata through his uid
        :param uid: String of the uid
        :return: the json containing the metadata
        '''
        url = self.config['url_get_metadata_uid'].replace("<uid>", uid);
        r = requests.get(url)
        log.info(r.text)
        log.info(r.status_code)
        if r.status_code is not 200:
            raise Exception(r.text, r.status_code)
        return json.loads(r.text)


#
# config = {
#     "url_create_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata",
#     "url_get_metadata_uid": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>",
# }
#
# metadata_manager = MetadataManager(config)
#
# metadata = {
#     "uid": "fenix|gaul0_2",
#     "creationDate": 1416221596000,
#     "meContent": {
#         "resourceRepresentationType": "geographic",
#         "seCoverage": {
#             "coverageSectors": {
#                 "idCodeList": "FENIX_GeographicalSectors",
#                 "version" : "1.0",
#                 "codes": [{"code": "MODIS_LAND_COVER"}]
#             },
#             "coverageTime": {
#                 "to": 949276800000,
#                 "from": 946684800000
#             }
#         }
#     },
#     "meSpatialRepresentation": {
#         "processing": {
#             "idCodeList": "FENIX_GeographicalProcessing",
#             "version" : "1.0",
#             "codes": [{"code": "AVG_MONTHLY"}]
#         },
#         "seDefaultStyle": {"name": "ghg_cultivation_organic_soils_cropland"},
#         "layerType": "vector"
#     },
#     "title": {"EN": "Cultivation Organic Soils - Croplands"},
#
#     "dsd": {
#         "contextSystem": "FENIX",
#         "workspace": "fenix",
#         "layerName": "gaul0_2"
#     }
# }
#
# metadata_manager.get_metadata_uid("fenix|gaul0_22")

#metadata_manager.publish_metadata(metadata)
