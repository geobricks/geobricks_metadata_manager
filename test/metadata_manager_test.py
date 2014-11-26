import unittest
from test.config.metadata_manager_config_test import config
from geobricks_metadata_manager.core.metadata_manager_d3s_core import MetadataManager

metadata_publish = {
    "uid": "fenix|layer_test",
    "meContent": {
        "resourceRepresentationType": "geographic",
    },
    "dsd": {
        "contextSystem": "FENIX",
        "workspace": "fenix",
        "layerName": "layer_test"
    }
}


class GeobricksTest(unittest.TestCase):

    def test_publish_metdata(self):
        metadata_manager = MetadataManager(config)
        result = metadata_manager.publish_metadata(metadata_publish)
        self.assertEqual(result['uid'], metadata_publish['uid'])

