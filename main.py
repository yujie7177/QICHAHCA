from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():

    '''win 不需要指定路径'''
    # executable_path = "C:/Users/NZXT/Documents/study/Qichacha/edgedriver_win64/msedgedriver.exe"

    '''获取&注入cookies'''
    driver = webdriver.Edge()
    driver.get("https://www.qcc.com/")
    # time.sleep(15)
    # cookies = driver.get_cookies()
    # print(cookies)
    cookies = [{'domain': 'www.qcc.com', 'expiry': 1710605272, 'httpOnly': False, 'name': 'CNZZDATA1254842228', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '1456613584-1694880464-%7C1694880473'}, {'domain': '.qcc.com', 'expiry': 1729440463, 'httpOnly': False, 'name': 'qcc_did', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'af9f52b9-444f-46d5-9c41-4c53284e7774'}, {'domain': '.qcc.com', 'expiry': 1695485271, 'httpOnly': True, 'name': 'QCCSESSID', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '09e06197a4899fc081cd67ddd8'}, {'domain': '.qcc.com', 'expiry': 1710605264, 'httpOnly': False, 'name': 'UM_distinctid', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '18a9ebf7d34581-0348cc0043dde4-78505774-384000-18a9ebf7d351ff5'}, {'domain': 'www.qcc.com', 'expiry': 1694882262, 'httpOnly': True, 'name': 'acw_tc', 'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': '78c967a316948804626642704eb16bc5be242826a098c3c6c752e56482'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    
    driver.get("https://www.qcc.com/")
    driver.find_element(By.CSS_SELECTOR, "#searchKey").send_keys("天津久日新材料股份有限公司")
    driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary").click()
    # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".frtrt.tsd0 .copy-title")))
    driver.find_element(By.CSS_SELECTOR, ".frtrt.tsd0 .copy-title").click()

    # 将激活标签页设置为最新的一项
    window = driver.window_handles
    driver.switch_to.window(window.pop())
    id = driver.current_url.split('/')[-1]
    newurl = "https://www.qcc.com/cassets/" + id
    driver.get(newurl)
    list = driver.find_elements(By.CSS_SELECTOR, "section[id='standardlist'] .pagination li")[:-1]
    for i in list:
        i.click()
        # TODO
        driver.find_elements(By.CSS_SELECTOR, "#standardlist table")
    time.sleep(1500)
if __name__ == "__main__":
    main()