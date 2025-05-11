from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        
        # проверка, что подстрока "login" есть в текущем url браузера (свойство Webdriver)              
        assert "login" in self.browser.current_url, "Login is not presented in current url"

    def should_be_login_form(self):
        
        # проверка, что есть форма логина на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#login_form"), "Login form is not presented"
        

    def should_be_register_form(self):
        
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(By.CSS_SELECTOR, "#register_form"), "Register form is not presented"
        