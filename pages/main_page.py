import os

from components.footer_component import FooterComponent
from components.product_card_component import ProductCardComponent
from pages.base_page import BasePage
from components.header_component import HeaderComponent


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page, os.getenv('MAIN_PAGE'))
        self.header = HeaderComponent(page)

    def get_header_component(self):
        return HeaderComponent(self.page)

    def get_product_card_component(self, title: str):
        return ProductCardComponent(self.page, title)

    def get_footer_component(self):
        return FooterComponent(self.page)