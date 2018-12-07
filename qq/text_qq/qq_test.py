#  /usr/bin/env python
# -*- coding:utf-8-*-
from qq.confing.以11 import 请求
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import  time

a=请求()
a.qingqiu()
class QQ(unittest.TestCase):
    def test_1(self):
        for i in range(10):
            try:
                self.stat = a.dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]').is_displayed()
            except:
                aa = a.dr.find_element_by_xpath('//*[@id="QZ_Toolbar_Container"]/div/a').is_displayed()
                self.assertTrue(aa)
                a.dr.quit()

            else:
                a.dr.switch_to_frame(self.stat)
                a.dr.find_element_by_xpath('//*[@id="newVcodeArea"]/div[1]/div/div[2]')
                ActionChains(a.dr).drag_and_drop_by_offset(self.stat, 180, 0).perform()
                a.dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]').is_displayed()
                time.sleep(2)





if __name__=='__main__':
    unittest.main()
