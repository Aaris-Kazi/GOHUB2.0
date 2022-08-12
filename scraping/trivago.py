from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
loc = input()
driver = webdriver.Chrome('scraping/chromedriver.exe')
driver.get("https://www.trivago.in/")
time.sleep(3)
location = driver.find_element(By.ID, 'input-auto-complete')
location.click()
location.send_keys(loc)
# location.send_keys(Keys.RETURN)
time.sleep(3)
submit = driver.find_element(By.XPATH, '//*[@id="react-autowhatever-1--item-0"]/div/div')
# react-autowhatever-1--item-1
submit.click()
submit = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div[2]/div/div/form/div[3]/button')
submit.click()
time.sleep(35)
submit = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div[1]/div[4]/div/form/div[3]/button')
submit.click()
time.sleep(5)

sc = 0
while sc <=5040:
    tp = sc
    sc +=200
    driver.execute_script("window.scrollTo("+str(tp)+","+str(sc)+")")
    time.sleep(1)

h_name = driver.find_elements(By.CLASS_NAME, 'text-left.w-full.truncate.font-bold')
price = driver.find_elements(By.CLASS_NAME, 'font-bold.text-green-900.text-xl')
h_type = driver.find_elements(By.CLASS_NAME, 'whitespace-nowrap.text-m.ml-2')
images = driver.find_elements(By.CLASS_NAME, 'select-none.object-cover')
rate = driver.find_elements(By.CLASS_NAME, 'inline-flex.justify-center.items-center.rounded-full.leading-none.text-white.font-bold.w-8.text-s.RatingPill_small__L_BAr.bg-green-800')
site = driver.find_elements(By.CLASS_NAME, 'text-s')
# //*[@id="__next"]/div[1]/main/div[4]/section/div/ol/li[5]/div/article/div[2]/div[2]/div[1]/div/div[1]/strong
# //*[@id="__next"]/div[1]/main/div[4]/section/div/ol/li[6]/div/article/div[2]/div[2]/div[1]/div/div[1]/strong
location = []
hotel_name= []
hotel_price= []
hotel_type= []
hotel_image= []
hotel_rating= []

print(len(h_name), len(price), len(h_type), len(images), len(rate))

for i,j,k,l in zip(h_name, price, h_type, images):
    hotel_name.append(i.text)
    hotel_price.append(j.text)
    hotel_type.append(k.text)
    hotel_image.append(l.get_attribute("src"))
    # hotel_rating.append(m.text)
    location.append(loc)
    
driver.close()
driver.quit()

print(len(hotel_image))
df = pd.DataFrame({
    "location": location,
    "Hotel Image": hotel_image,
    "Hotel Name": hotel_name,
    "Hotel Type": hotel_type,
    "Hotel price": hotel_price,
})
df.to_csv(loc+'.csv')