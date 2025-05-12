import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

# Запуск тестов с маркировкой @pytest.mark.need_review:  pytest -v --tb=line --language=en -m need_review
# Тесты из предыдущих заданий отмечены маркировкой @pytest.mark.skip для пропуска.

@pytest.mark.skip
@pytest.mark.parametrize('link_add', ["offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6", pytest.param("offer7", marks=pytest.mark.xfail), "offer8", "offer9"])
def test_guest_can_add_product_to_basket(browser, link_add):
    okay_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link_add}"

    product_page = ProductPage(browser, okay_link)
    product_page.open()   
 
    product_page.add_to_basket()   
    product_page.solve_quiz_and_get_code()
    product_page.should_be_add_to_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    product_page = ProductPage(browser, link)
    product_page.open()
          
    time.sleep(1)
    product_page.add_to_basket()
                    
    product_page.solve_quiz_and_get_code() 
    time.sleep(2)  
    product_page.should_be_add_to_basket()   

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):   
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    product_page = ProductPage(browser, link)
    product_page.open()
            
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    product_page = ProductPage(browser, link)
    product_page.open() 
    
    time.sleep(1)   
    product_page.should_not_be_success_message()

@pytest.mark.skip    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    product_page = ProductPage(browser, link)
    product_page.open() 
          
    product_page.add_to_basket()
    time.sleep(1)
    product_page.should_be_success_message() 

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()        
    page.should_be_login_link()   

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"

    page = ProductPage(browser, link)
    page.open()
 
    time.sleep(2)   
    page.go_to_login_page()

    time.sleep(2)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()
 
    time.sleep(2)
    page.go_to_basket_page()    

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()

@pytest.mark.login_user
class TestUserAddToBasketFromProductPage():    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):   
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

        login_page = LoginPage(browser, link)
        login_page.open()

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())

        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()
    

    def test_user_cant_see_success_message(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

        product_page = ProductPage(browser, link)
        product_page.open() 
    
        time.sleep(1)   
        product_page.should_not_be_success_message()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

        product_page = ProductPage(browser, link)
        product_page.open()
                   
        time.sleep(1)
        product_page.add_to_basket()
                       
        product_page.solve_quiz_and_get_code() 
        time.sleep(2)  
        product_page.should_be_add_to_basket()    

