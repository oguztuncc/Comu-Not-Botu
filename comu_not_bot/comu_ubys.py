from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ubys_get:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password

    def login(self):
        self.browser.get("https://ubys.comu.edu.tr/")

        time.sleep(2)

        self.browser.find_element(By.XPATH,value="//*[@id='username']").send_keys(self.username)
        self.browser.find_element(By.XPATH,value="//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH,value="/html/body/div[3]/div/section/div/div/div[2]/form/div[3]/div[1]/button").click()
        
    def get_not(self):
        time.sleep(2)
        self.browser.get("https://ubys.comu.edu.tr/AIS/Student/Class/Index?sapid=RQEBg6RNDsbXvACdurlYwA!xGGx!!xGGx!") 
        time.sleep(2) 
        items=self.browser.find_elements(By.CSS_SELECTOR,value=".table.table-striped.table-condensed") 
        
        liste=[]
        time.sleep(2)
        names = [tr for tr in self.browser.find_elements(By.XPATH, "//*[@id='Bahar2024table']/tbody/tr") if tr.is_displayed()]

        for index,n in enumerate(names,start=1):
            if index%2==1:
                liste.append(n)

        # print(len(liste))        
        time.sleep(1)

        liste2_names=[]

        for name in liste:
            liste2=name.find_elements(By.TAG_NAME,"td")
            liste2_names.append(liste2[1].text)
        time.sleep(3)
    
        for index,item in enumerate(items,start=0):
            time.sleep(0.5)
            
            try:
                a=item.find_element(By.CSS_SELECTOR,value=".text-right")
                b=a.find_element(By.XPATH,"./following-sibling::td[1]").text
                c=item.find_elements(By.CSS_SELECTOR,value=".text-right")[1]
                d=c.find_element(By.XPATH,"./following-sibling::td[1]").text
                #print(f"a.text={a.text} ve d={d} ve b={b} ve c.text={c.text}")
                if b !="Girmedi" or d!="Girmedi" :
                    print(f" değişiklik var")
                    print(f"{liste2_names[index]}\n{item.text}\n")
                else:
                    #time.sleep(1)
                    print(f"{index+1}. {liste2_names[index]} {a.text}değişiklik yok\n{c.text}değişiklik yok")
            except :
                continue        

işlem=ubys_get("Kimlik Numarası","Parola")
işlem.login()
işlem.get_not()