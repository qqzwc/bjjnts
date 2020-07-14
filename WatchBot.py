from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
# import pyautogui
# extension_dir = r"C:\Users\CY\AppData\Roaming\Mozilla\Firefox\Profiles\vb20rt8e.default-release\extensions\{7be2ba16-0f1e-4d93-9ebc-5164397477a9}.xpi"
# option = webdriver.ChromeOptions()
# option.add_argument("--user-data-dir="+r"C:\Users\CY\AppData\Local\Google\Chrome\User Data")
# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Firefox(executable_path='.\geckodriver.exe')
# driver.install_addon(extension_dir, temporary=True)
driver.get("https://www.bjjnts.cn/login")
driver.maximize_window()

while True:
    signal = input("进入课程播放页面后输入ok继续，输入quit退出")
    if signal == "ok":
        break
    else:

        exit(0)


cur_url = driver.current_url
url_template = cur_url.split("/")[:-1]
# print(url_template)
url_template = '/'.join(url_template)
# print(url_template)
first = cur_url.split("/")[-1]
# print(first)
# print(type(first))

course_study_videomenu = WebDriverWait(driver, 10, 0.5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "course_study_videomenu"))
)
new_demoul = course_study_videomenu.find_element_by_tag_name("ul")
li_list = []
li_list = new_demoul.find_elements_by_tag_name("li")
video_num = len(li_list)
print("共有{}个视频".format(video_num))
first = int(first)
url_list = []
for i in range(0, video_num):
    index = str(first + i)
    url = url_template + "/" + index
    # print(url)
    url_list.append(url)
video_name_list = []
for li in li_list:
    div = li.find_element_by_tag_name("div")
    a = div.find_element_by_tag_name("a")
    h4 = a.find_element_by_tag_name("h4")
    video_name = h4.text.split("(")[0]
    video_name_list.append(video_name)
    '''
    print(video_name)
    span = a.find_element_by_tag_name("span")
    if "100%"  in span.text:
        print("next")
    print(span.text)
    '''
try:
    face_startbtn = WebDriverWait(driver, 6, 0.5).until(
        EC.element_to_be_clickable((By.ID, "face_startbtn")))
    face_startbtn.click()
except:
    pass


for i, url in enumerate(url_list):
    driver.switch_to.window(driver.window_handles[0])
    driver.get(url)
    try:
        face_startbtn = WebDriverWait(driver, 3, 0.5).until(
            EC.element_to_be_clickable((By.ID, "face_startbtn")))
        face_startbtn.click()
    except:
        pass



    course_study_videomenu = WebDriverWait(driver, 3, 0.5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "course_study_videomenu"))
    )
    new_demoul = course_study_videomenu.find_element_by_tag_name("ul")
    cur_li = new_demoul.find_elements_by_tag_name("li")[i]
    progress = cur_li.find_element_by_tag_name("div").find_element_by_tag_name("a").find_element_by_tag_name(
        "span").text
    if "100%" in progress:
        continue
    else:
        cur_li.click()
    sleep(2)
    print("正在学习第{}个视频 {}".format(i+1, video_name_list[i]))
    course_study_videobox = driver.find_element_by_class_name("course_study_videobox")
    play = course_study_videobox.find_element_by_tag_name("video")
    # play.click()

    # pyautogui.press('d')
    while True:
        '''
        pyautogui.moveTo(900, 300, 2)
        pyautogui.moveTo(300, 300, 2)

        confirm_location = pyautogui.locateCenterOnScreen("CONFIRM.png", confidence=0.7, grayscale=True)
        print(confirm_location)
        if confirm_location is not None:
            pyautogui.click(confirm_location[0], confirm_location[1])
            print("确定")
        else:
            print("未发现确定")
        '''
        try:
            # accept = driver.find_element_by_class_name("layui-layer-btn0")
            accept = WebDriverWait(driver, 6, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "layui-layer-btn0")))
            accept.click()
        except:
            pass

        try:
            face_startbtn = WebDriverWait(driver, 6, 0.5).until(
                EC.element_to_be_clickable((By.ID, "face_startbtn")))
            face_startbtn.click()
        except:
            pass

        progress = cur_li.find_element_by_tag_name("div").find_element_by_tag_name("a").find_element_by_tag_name("span").text
        if "100%" in progress:
            print("{} 学习完毕".format(video_name_list[i]))
            break
        else:
            sleep(10)
            '''
            s = 10
            while s > 0:
                print(s)
                s -= 1
                sleep(1)
            '''