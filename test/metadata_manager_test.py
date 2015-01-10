import unittest
from geobricks_metadata_manager.config.config import config
from geobricks_metadata_manager.core.metadata_manager_d3s_core import MetadataManager

workspace = "fenix"
layername = "test"

metadata = {
    "uid": workspace + "|" + layername,
    "meContent": {
        "resourceRepresentationType": "geographic",
    },
    "dsd": {
        "contextSystem": "FENIX",
        "workspace": workspace,
        "layerName": layername
    }
}


class GeobricksTest(unittest.TestCase):

    def test_publish_metdata(self):
        metadata_manager = MetadataManager(config)
        try:
            metadata_manager.delete_metadata(metadata['uid'])
        except Exception, e:
            pass
        result = metadata_manager.publish_metadata(metadata)
        self.assertEqual(result['uid'], metadata['uid'])

    def test_delete(self):
        metadata_manager = MetadataManager(config)
        result = metadata_manager.delete_metadata(metadata['uid'])
        print result
        self.assertEqual(result['uid'], metadata['uid'])

