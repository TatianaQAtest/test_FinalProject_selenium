import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Запуск теста:   pytest --language=es test_items.py (тест выполняется только в chrome)
# Запуск теста: pytest -s -v --browser_name=firefox --language=ru test_items.py (тест выполняется в chrome или в firefox)

def pytest_addoption(parser):
    
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")
    
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")  

@pytest.fixture(scope="function")
def browser(request):    
    browser_name = request.config.getoption("browser_name")    
    user_language = request.config.getoption("language") 
   
    options = Options()    
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)    
    
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    

    browser.implicitly_wait(5)
    yield browser
    browser.quit()