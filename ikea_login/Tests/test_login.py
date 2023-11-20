import pytest

from Pages.login_page import Login_Page

from ddt import ddt, data, unpack
from utilities.csv_reader import getCSVData

import  unittest
@pytest.mark.usefixtures("oneTimeSetup")
class Test_Login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self,oneTimeSetup ):
        self.lp= Login_Page(driver=self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/home/kavya/CRs/ikea_login/testdata.csv"))
    @unpack
    def test_login(self, usename, password):
        self.lp.login_into_ikea(usename,password)
        value=self.lp.verify_successful_login()
        assert value==True