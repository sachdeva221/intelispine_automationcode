import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action ='store',default = "edge", help = "Default is chrome "
    )


@pytest.fixture(scope="class")
def invoking_code(request):
    global Driver
    Browser_name = request.config.getoption("browser_name")
    if Browser_name == "chrome":
        serv = Service("C:\\Users\\DELL\\Desktop\\Driver\\chromedriver.exe")
        Driver = webdriver.Chrome(service=serv)
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        Driver.get("https://stage-admin.myintellispine.com/login")
        Driver.implicitly_wait(5)

    elif Browser_name == "firefox":
        obj = Service("C:\\Users\\DELL\\Desktop\\driverfirefox\\geckodriver.exe")
        Driver = webdriver.Firefox(service=obj)
        Driver.maximize_window()
        Driver.get('https://stage-admin.myintellispine.com/login')
        Driver.implicitly_wait(5)

    elif Browser_name == "edge":
        obj2 = Service('C:\\Users\\DELL\\Desktop\\Driver_Notes\\msedgedriver.exe')
        Driver = webdriver.Edge(service=obj2)
        Driver.maximize_window()
        Driver.get('https://stage-admin.myintellispine.com/login')
        Driver.implicitly_wait(5)
    else:
        print('Please provide the right name')

    request.cls.Driver = Driver
    yield
    # Driver.close()

