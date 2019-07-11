import unittest
from selenium import webdriver
import  HtmlTestRunner
import sys
import  time
from Test.PageObjects.Pages.HomePage import HomePage

sys.path.append("C:/Users/admin/PycharmProjects/WebAutomation/Test/PageObjects/Pages")

class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='F:/chromedrive/chromedriver.exe')
        driver=cls.driver
        #cls.driver.get(cls.baseurl)
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test_title_verify(self):
        driver=self.driver
        lp=HomePage(driver)
        lp.navigate("http://live.guru99.com/index.php")
        # time.sleep(10)
        # lp.menu()
        actual=lp.Title()
        expected="THIS IS DEMO SITE FOR"
        lp.mobile()
        lp.sort()
    """
        def tearDownClass(cls):
        cls.driver.close()
    """

    if __name__== '__main__':
       unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(OUTPUT="C:/Users/admin/PycharmProjects/WebAutomation"))





