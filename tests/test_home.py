from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
class Tests():
    def test_2(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)

        print("ejercicio 2")
        # input = driver.find_element_by_xpath('/html/body/div[1]/div[2]/fieldset/input')
        input = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/fieldset/input")
        input.send_keys('Me')
        time.sleep(3)
        input_options = driver.find_element(By.XPATH, "/html/body/ul/li[6]/div")
        input_options.click()
        time.sleep(5)

    def test_3(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)

        print("ejercicio 3")
        dropDown = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/fieldset/select")
        drop = Select(dropDown)
        drop.select_by_index(2)
        time.sleep(3)
        drop.select_by_index(3)
        time.sleep(5)

    def test_4(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)

        print("Ejercicio 4")
        window_before = driver.window_handles[0]
        switchWindow = driver.find_element(By.ID, "openwindow")
        switchWindow.click()
        window_after = driver.window_handles[1]
        time.sleep(4)
        driver.switch_to.window(window_after)

        thirtydays = driver.find_element(By.XPATH, "/html/body/section[3]/div/div/div/div[5]/div/div[2]/div/div[2]/h3")
        # Mover la vista hasta donde se encuentra el elemento
        driver.execute_script('arguments[0].scrollIntoView(true);', thirtydays)
        time.sleep(3)
        driver.close()
        driver.switch_to.window(window_before)
        time.sleep(5)

    def test_5(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)
        print("Ejercicio 5")
        window_before = driver.window_handles[0]
        switchTap = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/fieldset/a")
        switchTap.click()
        window_after = driver.window_handles[1]
        time.sleep(5)
        driver.switch_to.window(window_after)
        course = driver.find_element(By.XPATH, "/html/body/div/div[2]/section[2]/div[2]/a")
        ActionChains(driver).move_to_element(course).perform()
        driver.save_screenshot("Prueba5.png")
        time.sleep(2)
        driver.switch_to.window(window_before)
        time.sleep(5)

    def test_6(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)

        print("Ejercicio 6")
        switchAlert = driver.find_element(By.CSS_SELECTOR, "#name")
        switchAlert.send_keys("Stori Card")
        btnAlert = driver.find_element(By.XPATH, "//input[@value='Alert']")
        btnAlert.click();
        alert = driver.switch_to.alert
        print("Mensaje de la Alerta: " + alert.text)
        alert.accept()

        switchAlert.send_keys("Stori Card")
        btnConfirm = driver.find_element(By.XPATH, "//input[@value='Confirm']")
        btnConfirm.click();
        alert = driver.switch_to.alert
        alertMessage = alert.text

        alertHello = "Hello Stori Card, Are you sure you want to confirm?"

        if alertMessage == alertHello:
            print("Es igual")
        else:
            print("No es el mismo")

    def test_7(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)


        contador = 0
        table = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/fieldset/table")
        driver.execute_script('arguments[0].scrollIntoView(true);', table)
        trs = driver.find_elements(By.XPATH, "/html/body/div[3]/div[1]/fieldset/table/tbody/tr")
        for i in range(1, len(trs) + 1):
            prices = driver.find_elements(By.XPATH, "/html/body/div[3]/div[1]/fieldset/table/tbody/tr" + str(i) + "/td[3]")
            for price in prices:
                print(price.text)
                if  price == "25":
                    contador+1
        print(contador)

    def test_8(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)

        table = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/fieldset[2]/div[1]/table")
        driver.execute_script('arguments[0].scrollIntoView(true);', table)
        trs = driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr")
        for i in range(1, len(trs)+1):
            names =driver.find_elements(By.XPATH, "/html/body/div[3]/div[2]/fieldset[2]/div[1]/table/tbody/tr["+str(i)+"]/td[1]")
            for name in names:
                print(name.text)

    def test_9(self):
        url = 'https://rahulshettyacademy.com/AutomationPractice/'
        # Configuración de inicio de navegación de Google
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        # option.add_argument('--headless')
        option.add_argument('disable-infobars')
        option.add_argument('user-data-dir=C:\python27\profile')
        option.add_argument("--start-maximized");

        # Abrir navegador Chrome
        driver = webdriver.Chrome(chrome_options=option)
        # driver = webdriver.Chrome(executable_path = r 'C:\chromedriver_win32\chromedriver.exe', options = options)
        driver.get(url)
        time.sleep(3)

        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        text = driver.find_element(By.XPATH, '/html/body/div/div[2]/section[4]/div/div/div/div[2]/ul/li[2]')
        print(text.text)
        driver.switch_to.default_content()