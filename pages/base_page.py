# Класс базовой страницы
class BasePage:

    # driver - текущий драйвер браузера
    # url - передаваемый url
    # timeout=10 - таймаут ожидания элемента, по умолчанию 10
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)
        # Всегда разворачиваем окно максимально
        self.driver.maximize_window()

    # открыть ссылку
    def open(self):
        self.driver.get(self.url)

    # Функция выставляет параметры для проверки существования объекта
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
