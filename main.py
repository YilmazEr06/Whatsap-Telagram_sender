

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




while True:
    i = 0
    platform = input("hangi platformdan göndermek istiyorsunuz 1- whatsapp  2-telegram  ")
    s = input("kaç mesaj göndermek istiyorsunuz   ")
    send=input("ne göndermek istiyorsunuz  ")
    if platform == "2":
        driver = webdriver.Chrome(r"C:\Users\Kaya Eryılmaz\selen\chromedriver.exe")
        print("telegram seçildi")
        driver.get("https://web.telegram.org/")
    elif platform=="1":
        driver = webdriver.Chrome(r"C:\Users\Kaya Eryılmaz\selen\chromedriver.exe")
        driver.get("https://web.whatsapp.com/")

    start = input("başlamak için 1 e iptal için 2 ye basınız ")

    if start=="1":

        while True:


            if i<int(s):

                try:
                    if platform=="1":

                        select_element = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                        select_element.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(send)
                        select_element.send_keys(Keys.ENTER)
                    elif platform=="2":
                        select_element = driver.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]')
                        select_element.find_element_by_xpath('//*[@id="ng-app"]/body/div[1]/div[2]/div/div[2]/div[3]/div/div[3]/div[2]/div/div/div/form/div[2]/div[5]').send_keys(send)
                        select_element.send_keys(Keys.ENTER)
                    else:
                        print("geçerli bir değer giriniz")
                        break


                    i=i+1
                    print(i)
                except:
                    print("olmadı Lütfen gerekli sayfaya geliniz")
                    break

            else:
                time.sleep(10)
                driver.quit()
                break
    elif  start==2:
        print("değerler sıfırlandı")
    else:
        print("Geçersiz bir değer girildi lütfen yeniden deneyiniz")
