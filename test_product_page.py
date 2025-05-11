
from .pages.product_page import ProductPage

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