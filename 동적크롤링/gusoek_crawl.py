import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
from time import sleep

from random import *

options = Options()

# chrome을 전체화면으로 넓히는 옵션입니다.
options = webdriver.ChromeOptions()
options.add_argument('window-size=1920,1080')

# executable_path에는 chromedriver 실행 파일의 경로를 넣고, chrome_options에는 options 변수를 넣습니다.
driver = webdriver.Chrome(executable_path='./chromedriver', options=options)
driver.implicitly_wait(1)

# chromedriver.exe의 파일명을 넣어주면 된다. (확장자 없이)
# 만약 chromedriver.exe가 다른 곳에 있다면 절대경로로 넣어주면 된다.

# 입력한 지역탭으로 이동
area_id = [1,2,3,4,5,6,7,31,32,33,34,35,36,37,38,39] # 경기부터 id가 31로 시작해서 경기라 치면 값을 못 불러옴
area_url = [] # 각 지역별 구석구석 url 저장

for num in range(len(area_id)):
    area_url.append("https://korean.visitkorea.or.kr/list/ms_list.do?areacode=" + str(area_id[num]))

driver.implicitly_wait(1)

driver.get(url=area_url[0]) # 입력된 url 창을 크롬으로 켬

area_box = driver.find_element_by_xpath('//*[@id=\"' + str(num) + '\"]/a') # Copy Xpath
area_box.click()

# 인기순으로 정렬
pop_sort_box = driver.find_element_by_xpath('// div [@ class = \'btn_txt\']//*[@id="3"]') # Copy Xpath
pop_sort_box.click()
sleep(5)

# 여행지 카테고리 클릭(전체로 되면 여행기사도 포함이 돼 우리가 원하는 여행지 타이틀만을 가져올 수 없기 때문)
pop_sort_box = driver.find_element_by_xpath('//*[@id="Tour"]/button/span') # Copy Xpath
pop_sort_box.click()
sleep(3)

i = randint(1, 100)  # 1부터 100 사이의 임의의 정수
page_next = int(((i/10)-1) / 5) # 다음 페이지 버튼 누르는 횟수
page = int((i-1) / 10 + 1) # 해당 title이 있는 페이지
title_num = int(((i-1) % 10) + 1) # 해당 title text의 인덱스

for n in range(page_next):
    next_page_box = driver.find_element_by_xpath('//*[@id=\"' + str(n*5+1) + '\"]')  # Copy Xpath
    next_page_box.click()
    sleep(3)

page_box = driver.find_element_by_xpath('// div [@ class = \'page_box\']//*[@id=\"' + str(page) + '\"]')  # Copy Xpath
page_box.click()
sleep(3)

# 여행지 제목 출력
title = driver.find_element_by_css_selector("#contents > div.wrap_contView.clfix > div.box_leftType1 > ul > li:nth-child(" + str(title_num) + ") > div.area_txt > div > a") # Copy selector
print(title.text)

# 상세정보 출력을 위해 해당 여행지 페이지로 들어감
place_box = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[1]/ul/li[' + str(title_num) + ']/div[2]/div/a')  # Copy Xpath
place_box.click()

# 상세정보 설명 출력
title_explain = driver.find_element_by_css_selector("#detailGo > div:nth-child(2) > div > div.inr_wrap > div > p") # Copy selector
print(title_explain.text)

# 전화번호 출력
title_explain = driver.find_element_by_css_selector("#detailinfoview > div > div.inr_wrap > div > ul > li:nth-child(1) > span.pc") # Copy selector
print(title_explain.text)

# 주소 출력
Address = driver.find_element_by_css_selector("#detailinfoview > div > div.inr_wrap > div > ul > li:nth-child(3) > span") # Copy selector
print(Address.text)


# 관광지 //*[@id="3f36ca4b-6f45-45cb-9042-265c96a4868c"]/button/span
# 문화시설 //*[@id="651c5b95-a5b3-11e8-8165-020027310001"]/button/span
# 레포츠 //*[@id="e6875575-2cc2-43ba-9651-28d31a7b3e23"]/button/span
# 체험 //*[@id="23bc02b8-da01-41bf-8118-af882436cd3c"]/button/span