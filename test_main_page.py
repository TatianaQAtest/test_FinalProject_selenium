from .pages.main_page import MainPage
from .pages.login_page import LoginPage

# Запуск теста: pytest -v --tb=line --language=en test_main_page.py 

def test_guest_can_go_to_login_page(browser):
 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу  
    page.go_to_login_page()         # переход к странице логина
    login_page = LoginPage(browser, browser.current_url) # получение текущего url-страницы (используя свойство  Webdriver) и сохранение её в переменную. 
    login_page.should_be_login_page() # проверка на наличие элемента (в main_page с assert)

    


    