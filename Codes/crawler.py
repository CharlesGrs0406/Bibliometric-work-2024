from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import multiprocessing

# replace with your own Clarivate id and password
your_id = "id"
your_password = "****"

df = pd.read_excel("journals.xlsx") # all the journals you need search

def multi_check(begin_index):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(r'https://access.clarivate.com/login?app=jcr&referrer=target%3Dhttps:%2F%2Fjcr.clarivate.com%2Fjcr%2Fbrowse-journals&alternative=true&shibShireURL=https:%2F%2Flogin.incites.clarivate.com%2F%3FDestApp%3DIC2JCR%26amp;auth%3DShibboleth&shibReturnURL=https:%2F%2Flogin.incites.clarivate.com%2F')

    time.sleep(1)


    # log in
    driver.find_element(By.NAME,'email').send_keys(your_id)
    driver.find_element(By.NAME,'password').send_keys(your_password)
    driver.find_element(By.ID,'signIn-btn').click()

    wait = WebDriverWait(driver, 10)
    old_url = driver.current_url
    new_url = wait.until(EC.url_changes(old_url))

    time.sleep(3)

    # 接受cookies
    driver.find_element(By.ID,"onetrust-accept-btn-handler").click()


    # Parallel crawling
    
    for index in range(begin_index, begin_index+25):

        if index >= len(df.index):
            continue

        journal_name = df.loc[index,'source']

        if journal_name == "Smithsonian": # This Journal has some unknown property that would crash the algorithm
            continue

        driver.find_element(By.ID, "search-bar").clear()
        driver.find_element(By.ID, "search-bar").send_keys(journal_name)
        # driver.find_element(By.ID, "search-bar").send_keys("Computers in Human Behavior")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,"[aria-label=' site search']").click()
        time.sleep(3)

        try:
            error_msg = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/div[2]/div/form/p")

        except Exception:

            try:
                driver.find_element(By.CSS_SELECTOR,"[title='Download']").click()
                time.sleep(2)
                driver.find_element(By.XPATH,'//*[@id="mat-menu-panel-3"]/div/button[1]').click()
                time.sleep(0.5)
                df.at[index,'label'] = +1
                
            except Exception:
                print("An error occured when crawling the following journal: "+journal_name)
                print("The index of this process is: "+str(begin_index))
                time.sleep(1)
                df.at[index,'label'] = -1
            
        else:
            print(journal_name+" is not in the database!")
            df.at[index,'label'] = 0

        # df.to_excel("journals.xlsx")



if __name__ == '__main__':
    # Parallel crawling
    pool = multiprocessing.Pool()
    results = pool.map(multi_check, range(0,len(df.index),25),chunksize=2)
    pool.close()
    pool.join()
    df.to_excel("journals.xlsx") # save the results into results.xlsx file
    # multi_check(1575)