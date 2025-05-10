from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
    # Конструктор __init__ — метод, который вызывается, когда мы создаем объект
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
    # В конструктор добавили команду для неявного ожидания со значением по умолчанию в 10
        self.browser = browser
        self.url = url 
        self.browser.implicitly_wait(timeout)  
    
    def open(self):
    # Метод open открывает нужную страницу в браузере, используя метод get() 
        self.browser.get(self.url)

    def is_element_present(self, how, what):
    # Добавили метод is_element_present, в котором будем перехватывать исключение(с помощью конструкции try/except).
    # В него передаем два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор)
    # Требуется импорт для нужных нам исключений (в начале этого файла)
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        