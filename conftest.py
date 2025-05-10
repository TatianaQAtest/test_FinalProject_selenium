import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Запуск теста:   pytest --language=es test_items.py (тест выполняется только в chrome)
# Запуск теста: pytest -s -v --browser_name=firefox --language=ru test_items.py (тест выполняется в chrome или в firefox)

def pytest_addoption(parser):
    # В командную строку передается параметр вида '--browser_name=chrome'(указание пользовательского браузера)
    # По умолчанию (если а командой строке не задан браузер), то будет выполняться в chrome 
    # (можно поставить default=None, и тогда будет ошибка, если пользователь не укажет в командной строке браузер browser_name)
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    # В командную строку передается параметр вида '--language=es'(указание пользовательского языка)
    # По умолчанию передается параметр '--language=en'
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")
   

@pytest.fixture(scope="function")
def browser(request):
    # В переменную browser_name передается параметр из командной строки
    browser_name = request.config.getoption("browser_name")

    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption("language")

    # Инициализируются опции браузера chrome и передаем параметр language из командной строки
    options = Options()    
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # В опции вебдрайвера firefox передаем параметр language из командной строки
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    
    # Выполняем инициализацию браузера , указанного в командной строке
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