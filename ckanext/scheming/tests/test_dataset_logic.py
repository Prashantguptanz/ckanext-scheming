from nose.tools import assert_raises
from ckanapi import LocalCKAN, NotFound

class TestDatasetSchemaLists(object):
    def test_dataset_schema_list(self):
        lc = LocalCKAN('visitor')
        dataset_schemas = lc.action.scheming_dataset_schema_list()
        assert 'camel-photos' in dataset_schemas

    def test_dataset_schema_show(self):
        lc = LocalCKAN('visitor')
        schema = lc.action.scheming_dataset_schema_show(type='camel-photos')
        assert schema['dataset_fields'][2]['label'] == 'Humps'

    def test_dataset_schema_not_found(self):
        lc = LocalCKAN('visitor')
        assert_raises(NotFound,
            lc.action.scheming_dataset_schema_show,
            type='ernie')

