from selenium import webdriver

from selenium.webdriver.common.by import By

import time
driver = webdriver.Chrome('F:/innovation skills/course/python/NLP/sentiment_analysis/chromedriver-win64/chromedriver.exe')


driver.maximize_window()

total_prod_in_a_page =41

title_list = []
link_list = []
image_link = []
driver.get('https://www.daraz.com.bd/products/animal-prints-cotton-canvas-children-bags-backpack-lash-messenger-bags-backpack-cartoon-school-i228794528-s1172556907.html?spm=a2a0e.searchlistcategory.sku.1.6d1a252bWdmkfF&search=1')
# for page_num in range(1,2):
    


    # for i in range(1,total_prod_in_a_page):
    #     j = str(i)


    #     title = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[4]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').text
    #     link = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[4]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[2]/div[2]/a').get_attribute('href')
    #     image = driver.find_element(By.XPATH,'/html/body/div[3]/div/div[4]/div[1]/div/div[1]/div[2]/div['+j+']/div/div/div[1]/div/a/img').get_attribute('src')
    #     title_list.append(title)
    #     link_list.append(link)
    #     image_link.append(image)

    

# print(title_list)
# print(link_list)
# print(image_link)



# prod_details_url = driver.get(link_list[0])

height = driver.execute_script('return document.body.scrollHeight')
print(height)
for j in range(0,height-800,30):
    driver.execute_script(f'window.scrollTo(0,{j});')
    time.sleep(0.2)

# all_comments =driver.find_elements(By.CLASS_NAME,'review-content-sl')
# for k in all_comments:
#     print(k.text)



all_comments =driver.find_elements(By.CLASS_NAME,'review-content-sl')
for k in all_comments:
    print(" 1",k.text)



# Click the element
# a_element.click()

all_comments =driver.find_elements(By.CLASS_NAME,'review-content-sl')
for k in all_comments:
    print("2",k.text)

time.sleep(50)

driver.quit()
