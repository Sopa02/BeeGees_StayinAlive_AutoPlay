from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class MyLittleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):                    #Ezen keresztül érjük el az oldalt
        cls.driver = webdriver.Chrome(r'chromedriver.exe')
        cls.driver.implicitly_wait(10)          #Futás előtt vár 10 másodpercet
        cls.driver.maximize_window              #Teljes képernyőre rakja  
    
    #def test_Page(self):
        # self.driver.get("http://www.lorumipse.hu")
        # print('\nElso teszt kesz!')

    #def test_Button(self):
        # print('\nMasodik teszt kezdodik...')
        # self.driver.get("http://www.lorumipse.hu")
        # self.button = self.driver.find_element_by_id('more')
        # self.button.click()
        # print('\nMasodik teszt kesz!')

    def test_Youtube(self):
        self.driver.get("https://youtube.com")


        try:
            self.driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/paper-dialog/yt-upsell-dialog-renderer/div/div[3]/div[1]/yt-button-renderer/a/paper-button').click()
            gonosz_iframe = self.driver.find_element_by_id('iframe')
            self.driver.switch_to_frame(gonosz_iframe)
            self.driver.find_element_by_id('introAgreeButton').click()
            self.driver.switch_to_default_content()
        except Exception as e:
            print('Bruh: (no first time window)'+e)

        
        self.driver.find_element_by_id('search').send_keys("Stayinalivee\n")
        
        self.result_videos = self.driver.find_elements_by_class_name('style-scope ytd-video-renderer')

        self.result_videos[0].click()

        self.driver.find_element_by_xpath('//*[@id="movie_player"]/div[24]/div[2]/div[2]/button[10]').click()
        try:
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button').click()
            try:
                time.sleep(5)
                self.driver.find_element_by_xpath('//*[@id="skip-button:6"]/span/button').click()
            except Exception as e:
                print('Bruhv2 (no second ad): '+e)
        except Exception as e:
            print('Bruhv2 (no ads): '+e)
    @classmethod
    def tearDownClass(cls):
        print('\nTest completed!')

unittest.main()                             #Futtatás