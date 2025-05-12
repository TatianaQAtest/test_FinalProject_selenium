import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

# Запуск теста: pytest -v --tb=line --language=en test_main_page.py

# При группировке тестов с помощью класса и маркировкой для всего класса, 
# тогда запуск теста :pytest -s -m "login_guest" test_product_page.py

@pytest.mark.login_guest
class TestLoginFromMainPage():
# при объединении в класс не забываем передать первым аргументом self 
    def test_guest_can_go_to_login_page(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                     # открываем страницу  
        page.go_to_login_page()         # переход к странице логина
        login_page = LoginPage(browser, browser.current_url) # получение текущего url-страницы (используя свойство  Webdriver) и сохранение её в переменную. 
        login_page.should_be_login_page() # проверка на наличие элемента (в main_page с assert)

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
# для задания: наследование и отрицательные проверки
# 1 Гость открывает главную страницу 
# 2 Переходит в корзину по кнопке в шапке сайта
# 3 Ожидаем, что в корзине нет товаров
# 4 Ожидаем, что есть текст о том что корзина пуста
 
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()    

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()

    