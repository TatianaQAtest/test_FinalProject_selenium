class BasePage():
    def __init__(self, browser, url):
    # Конструктор __init__ — метод, который вызывается, когда мы создаем объект
    # В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
        self.browser = browser
        self.url = url 
        

    def open(self): 
    # Метод open открывает нужную страницу в браузере, используя метод get()
        self.browser.get(self.url) 
        