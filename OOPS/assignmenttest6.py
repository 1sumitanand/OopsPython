from assignment6 import ConfigDict, MyError
import pytest
import shutil, os

class TestConfigDict:

    conf_template = 'config_file.txt'
    conf_testor = 'Test_config_file.txt'

    def setup_class(self):
        shutil.copy(TestConfigDict.conf_template, TestConfigDict.conf_testor)

    def teardown_class(self):
        os.remove(TestConfigDict.conf_testor)

    def test_obj(self):

        bc = ConfigDict(TestConfigDict.conf_testor)
        assert isinstance(bc, ConfigDict)
        assert isinstance(bc, dict)
        assert bc._filename == TestConfigDict.conf_testor

    def test__setitem__(self):

        cc = ConfigDict(TestConfigDict.conf_template)
        cc['chennai'] = 'tamilnadu'
        cc['bangalore'] = 'karnataka'

    def test__getitem__(self):
        #ab = ConfigDict(TestConfigDict.conf_testor)
        #print(ab.keys())
        with pytest.raises(KeyError):
            print(ConfigDict(TestConfigDict.conf_testor)['chen'])

            #print(ab['bangalore'])



cd = TestConfigDict()

cd.setup_class()
cd.test_obj()
cd.teardown_class()

cd.test__setitem__()
cd.setup_class()
cd.test__getitem__()
cd.teardown_class()





