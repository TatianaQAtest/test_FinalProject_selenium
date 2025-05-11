import pytest
import time
from .pages.product_page import ProductPage

# Запуск теста: pytest -v --tb=line --language=en test_main_page.py
# Маркировка теста для его пропуска @pytest.mark.skip
# Маркировка упавших тестов @pytest.mark.xfail

@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    # Задание: добавление в корзину со страницы товара
    # 1. Открываем страницу товара
    # 2. Нажимаем на кнопку "Добавить в корзину"
    # 3. Посчитать результат математического выражения - метод solve_quiz_and_get_code() (файл base_page.py) и ввести ответ.


    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    product_page = ProductPage(browser, link)
    product_page.open()                      # открываем страницу товара
    
      
    product_page.add_to_basket()             # метод - добавить товар в корзину   
    product_page.solve_quiz_and_get_code()   # метод для получения проверочного кода (в base_page)
    product_page.should_be_add_to_basket()   # метод - проверка,что товар добавлен в корзину (название товара и его цена совпадает)(в product_page)


@pytest.mark.skip
@pytest.mark.parametrize('link_add', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, link_add):
#Задание: независимость контента, ищем баг (c параметризацией)
#Упавший тест "offer7" отмечен как xfail

    okay_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link_add}"

    product_page = ProductPage(browser, okay_link)
    product_page.open()   
 
    product_page.add_to_basket()   
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket()

#Задание: отрицательные проверки
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    #Проверяем (с помощью is_not_element_present), что нет сообщения об успехе после добавления товара в корзину
    #1. Открываем страницу товара 
    #2. Добавляем товар в корзину 
    #3. Проверяем, что нет сообщения об успехе.
   
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
            
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):  
    #Проверяем (с помощью is_not_element_present), что нет сообщения об успехе после того, как открыли страницу товара
    #1. Открываем страницу товара 
    #2. Проверяем, что нет сообщения об успехе

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() 
    
    time.sleep(1)   
    product_page.should_not_be_success_message()

@pytest.mark.xfail    
def test_message_disappeared_after_adding_product_to_basket(browser):
    #Проверяем (с помощью is_disappeared), что нет сообщения об успехе после добавления товара в корзину 
    #1. Открываем страницу товара
    #2. Добавляем товар в корзину
    #3. Проверяем, что нет сообщения об успех.

    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open() 
          
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_be_success_message() 

def test_guest_should_see_login_link_on_product_page(browser):
#Тест: гость видит ссылку login_link на странице продукта"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()        
    page.should_be_login_link()   

def test_guest_can_go_to_login_page_from_product_page(browser):
#Тест: гость может перейти на страницу логина со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()    
    page.go_to_login_page()