
# Signal 실시간 검색어 크롤러
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time

def signal_crawler(): 

#   driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

  options = webdriver.ChromeOptions()
  options.add_argument('--headless')        # Head-less 설정 , headless
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=options)


  URL='http://signal.bz/news'
  driver.get(url=URL)
  driver.implicitly_wait(time_to_wait=15)

  lstResult = driver.find_elements(By.CSS_SELECTOR, '#app > div > main > div > section > div > section > section:nth-child(2) > div:nth-child(2) > div > div > div > a > span.rank-text')

  # driver.quit()


  result = []
  print("\n< Signal 실시간 검색어 >") 
  for k in lstResult:
      result.append(k.text)
    #   lstSignalKeyword.append(k.text)
  return result

