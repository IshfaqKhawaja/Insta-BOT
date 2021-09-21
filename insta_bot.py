from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/milkmochabear/?hl=en")
first_div = '//*[@id="fb-root"]'
js = "var element = document.querySelector('#fb-root'); console.log(element); element.parentNode.removeChild(element)"
browser.execute_script(js)
js = "var element = document.querySelector('.Z2m7o'); console.log(element); element.parentNode.removeChild(element);"
browser.execute_script(js)
time.sleep(10)
#click on follow button to pop up the screen
img = browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
#img  = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]').click()
print("Loading...")
while True:
    time.sleep(10)
    js = "var element = document.querySelector('.RnEpo._Yhr4'); console.log(element); element.parentNode.removeChild(element);"
    if(js):
        browser.execute_script(js)
        break
time.sleep(5)

browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img').click()
print("Now You can click")

'''
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]').click()


#To like
## <path d="M34.6 3.1c-4.5 0-7.9 1.8-10.6 5.6-2.7-3.7-6.1-5.5-10.6-5.5C6 3.1 0 9.6 0 17.6c0 7.3 5.4 12 10.6 16.5.6.5 1.3 1.1 1.9 1.7l2.3 2c4.4 3.9 6.6 5.9 7.6 6.5.5.3 1.1.5 1.6.5s1.1-.2 1.6-.5c1-.6 2.8-2.2 7.8-6.8l2-1.8c.7-.6 1.3-1.2 2-1.7C42.7 29.6 48 25 48 17.6c0-8-6-14.5-13.4-14.5z"></path>
'''
