from Base.basepage import BasePage
from  selenium.webdriver.support.select import Select
class HomePage(BasePage):

    page_title_xpath="//div[@class='page-title']/h2"
    Mobile_menu_xpath="//A[@href='http://live.guru99.com/index.php/mobile.html'][text()='Mobile']"



    def __init__(self,driver):
        BasePage.__init__(self,driver,base_url="http://live.guru99.com/index.php")

    def navigate(self,base_url):
        self.driver.get(base_url)

    def Title(self):
        title=self.driver.find_element_by_xpath(self.page_title_xpath).text
        print(title)
    def mobile(self):
        self.driver.find_element_by_xpath(self.Mobile_menu_xpath).click()
        mbl_title=self.driver.title
        print(mbl_title)

    def sort(self):
        select=Select(self.driver.find_element_by_xpath("(//SELECT[@onchange='setLocation(this.value)'])[1]"))
        select.select_by_index(1)

