import time,math,random,os #
import utils
import pickle,hashlib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
import selenium.common.exceptions
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=utils.chromeBrowserOptions())
driver.get("https://www.linkedin.com")

driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")

try:
    driver.find_element(By.ID,"username").send_keys("YOUR_EMAIL")
    time.sleep(2)
    driver.find_element(By.ID,"password").send_keys("YOUR_PASSWORD")
    time.sleep(2)
    driver.find_element("xpath",'//button[@type="submit"]').click()
    time.sleep(2)
except selenium.common.exceptions.NoSuchElementException as e:
    raise Exception(e)

# url="https://www.linkedin.com/jobs/search/?f_AL=true&keywords=frontend&f_JT=F%2CP%2CC&f_WT=1%2C2%2C3&location=NorthAmerica&geoId=102221843&&f_E=2&f_TPR=r604800&f_SB2=3&sortBy=DD"
# driver.get(url)
# time.sleep(random.uniform(1,5))
# totalJobs=driver.find_element(By.XPATH,'//small').text
# totalPages=utils.jobsToPages(totalJobs)
# print("----",totalJobs,totalPages,"----")
# time.sleep(random.uniform(1,5))

# offers=driver.find_elements(By.XPATH,'//li[@data-occludable-job-id]')
# print(offers)
# offerIds=[(offer.get_attribute(
#     "data-occludable-job-id").split(":")[-1]) for offer in offers]
# print(offerIds)
# time.sleep(random.uniform(1,5))

offerIds=[ '4024181886','4128628089']

for jobID in offerIds:
    offerPage='https://www.linkedin.com/jobs/view/' + str(jobID)
    driver.get(offerPage)
    time.sleep(random.uniform(1,5))
    driver.find_element(By.XPATH,"//div[contains(@class,'jobs-apply-button--top-card')]//button[contains(@class, 'jobs-apply-button')]").click()
    time.sleep(random.uniform(1,5))
    try:
        for _ in range(5):
            try:
                driver.find_element(By.CSS_SELECTOR,"button[aria-label='Continue to next step']").click()
                print("-----Clicked on Next-----")
                time.sleep(random.uniform(1,3))
            except:
                print("-----Unable to go to Next-----")
                break
        
        try:
            text_elements=driver.find_elements(By.XPATH,"//div[contains(@class,'artdeco-text-input')]")
            for element in text_elements:
                label=element.find_element(By.XPATH,".//label").text
                print("-----",label,"-----")
                input_field=element.find_element(By.XPATH, ".//input")
                current_val=input_field.get_attribute("value")
                if not current_val:
                    input_field.send_keys("1")
                    time.sleep(random.uniform(1,5))
                else:
                    print(current_val)
        except:
            print("No text element")
            pass
        
        try:
            fieldsets = driver.find_elements(By.XPATH, "//fieldset")
            for element in fieldsets:
                label=element.find_element(By.XPATH, "//span[@aria-hidden='true']").text
                print("-----",label,"-----")
                element.find_element(By.CSS_SELECTOR, "label[data-test-text-selectable-option__label='Yes']").click()
                time.sleep(random.uniform(1,5))
        except:
            pass
        
        
        try:    
            driver.find_element(By.CSS_SELECTOR,"button[aria-label='Review your application']").click()
            time.sleep(random.uniform(1,5))
        except:
            pass
        
        try:
            driver.find_element(By.CSS_SELECTOR, "label[for='follow-company-checkbox']").click()
            time.sleep(random.uniform(1,5))
        except:
            pass
        
        try:
            driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']").click()
            print("Applied")   
        except:
            pass
            
    except selenium.common.exceptions.NoSuchElementException as e:
        raise Exception(e)  
    
time.sleep(2)
driver.quit()