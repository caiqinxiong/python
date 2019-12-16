import time
import random
import getpass
from PIL import Image  # 处理图片
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
from selenium.webdriver.support import expected_conditions as EC

full_snap = 'full_snap.png'
portion_snap = 'portion_snap.png'

def get_img(xpath, img_path):
    """ 处理图片 """
    # 拿到带缺口的图片（整个网页），使用wait等照片加载完毕才能获取
    _canvas = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    # 拍个快照，这个是整个网页的快照，没有这个快照，往下就无从谈起
    driver.save_screenshot(img_path)
    # 从带缺口的图片中获取像素点
    left = _canvas.location.get('x')
    top = _canvas.location.get('y')
    right = left + _canvas.size['width']
    bottom = top + _canvas.size['height']
    # 从网页快照中截取出我们想要的带缺口的照片
    img_file_obj = Image.open(img_path)
    # 从完整的图片中，截取带缺口的部分照片并保存
    img_file = img_file_obj.crop((left, top, right, bottom))  # 裁剪，别忘了是元组类型
    # img_file.show()  # 展示裁剪后的图片
    img_file.save(img_path)  # 保存裁剪后的图片
    return img_file

def get_distance(image1, image2):
    """  对比两张图片，获取需要位移的距离 """
    p1 = image1.load()
    p2 = image2.load()
    x = 60
    for i in range(x, image1.size[0]):
        for j in range(20, image1.size[1] - 20):
            print(i, j)
            dot1 = p1[i, j]
            dot2 = p2[i, j]
            r = abs(dot1[0] - dot2[0])
            g = abs(dot1[1] - dot2[1])
            b = abs(dot1[2] - dot2[2])
            if not (r < 60 and g < 60 and b < 60):
                return i - 7
                # return i
    return i  # 当返回这个i的时候，意味着破解失败了，因为没有找到合适的位移点


def get_tracks(distance):
    """ 根据distance值，模拟出一段段的滑动轨迹，位移公式: s=V0t+(at^2)/2 """
    track = []
    current = 0  # 当前速度 0
    mid = distance * 3 / 5  # 前3/5是匀加速运动，后2/5是匀减速
    # t = random.randint(1, 3) / 10  # 0.2 或者 0.3
    # t = 0.18456
    t = 0.3
    v = 0  # 初始速度
    while current < distance:
        if current < mid:  # 前半段，是匀加速
            a = random.randint(2, 3)
        else:
            a =  - random.randint(2, 3)
        v0 = v
        v = v0 + a * t
        move = v0 * t + 0.5 * a * (t ** 2)
        current += move
        track.append(round(move))  # 取整
    return track


def crack_cnblogs_signin(user, pwd, url):
    """ 破解博客园登录的极验验证 """
    try:
        # 第1步：访问URL
        driver.get(url)

        # 第2步，获取用户名和密码标签并输入相应的值
        time.sleep(1)
        driver.find_element_by_id('LoginName').send_keys(user)
        driver.find_element_by_id('Password').send_keys(pwd)
        driver.find_element_by_class_name('ladda-label').click()

        # 第4步，拿到缺口和完整图片，用于后续做对比
        # 4.1 获取缺口图片
        time.sleep(1)
        portion_img = get_img('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[1]',
                              portion_snap)  # 传递缺口图片标签的xpath和图片名称

        # 4.2 获取完整的图片，但由于完整图片默认是隐藏的，我们无法截取，所以先让它显示出来
        # 4.2.1 通过js脚本将隐藏标签显示出来
        time.sleep(1)
        # 4.2.2 执行js脚本
        js = "document.getElementsByClassName('geetest_canvas_fullbg geetest_fade geetest_absolute')[0].style.display='block'"
        driver.execute_script(js)

        # 4.3 获取完整图片截图
        time.sleep(0.5)
        full_img = get_img('/html/body/div[2]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/canvas',
                           full_snap)  # 传递完整图片标签的xpath和图片名称

        # 第5步，对比两张图的像素RGB,得到不一样的像素点，取位移
        distance = get_distance(portion_img, full_img)
        # print(distance)  # 97就是我们想要的位移，并且这个值是不固定的

        # 第6步，获取移动轨迹
        tracks_list = get_tracks(distance)

        # 第7步， 按照轨迹列表开始匀加速再匀减速运动，水平移动
        # 7.1 获取滑动按钮
        geetest_slider_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'geetest_slider_button')))
        # 7.2 按住不放
        ActionChains(driver).click_and_hold(geetest_slider_button).perform()
        print(1111, tracks_list)
        for track in tracks_list:
            print(22222222222,track)
            ActionChains(driver).move_by_offset(xoffset=track, yoffset=0).perform()  # 水平移动，所以x轴在变，y轴不变
        # else:  # 模拟人滑动到缺口位置之后再滑动一点再滑动回来
        ActionChains(driver).move_by_offset(xoffset=3, yoffset=0).perform()
        ActionChains(driver).move_by_offset(xoffset=-3, yoffset=0).perform()
        # 在滑到位置后，不是立即松开，而是在一段时间之后再松开
        ActionChains(driver).pause(random.randint(6, 15) / 10).release(geetest_slider_button).perform()


    finally:
        # 关闭浏览器
        time.sleep(3)
        driver.quit()


if __name__ == '__main__':
    user = input('输入你的用户名: ').strip() # 替换为你的用户名
    pwd = getpass.getpass('输入的密码: ').strip()  # 替换为你的密码
    # 获取webdriver实例
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    url = r'https://account.cnblogs.com/signin?returnUrl=http%3a%2f%2fi.cnblogs.com%2f'
    crack_cnblogs_signin(user, pwd, url)
    # 截止到2019/11/8号，代码运行无误