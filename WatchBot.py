from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.bjjnts.cn/login")
driver.maximize_window()

while True:
    signal = input("登录完成后输入ok继续，输入quit退出")
    if signal == "ok":
        break
    else:
        driver.quit()
        exit(0)


driver.get("https://www.bjjnts.cn/lessonStudy/210/4598")
course_study_videomenu = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "course_study_videomenu"))
)
new_demoul = course_study_videomenu.find_element_by_tag_name("ul")
li_list = []
for li in new_demoul.find_elements_by_tag_name("li"):
