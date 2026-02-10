from playwright.sync_api import Playwright
from components.base_component import BaseComponent
from controls.button_control import ButtonControl
from controls.input_control import InputControl


class HeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator('#header'))
        self.logo_button = ButtonControl(self.page, self.wrapper.locator('a[title="Главная"]'))
        self.search_input = InputControl(self.page, self.wrapper.locator('input[id="edit-search"]'))
        self.search_button = ButtonControl(self.page, self.wrapper.locator('input[id="edit-submit-search-result"]'))
        self.personal_account_button = ButtonControl(self.page, self.wrapper.locator('div[class="personal"]'))
        self.personal_cart_button = ButtonControl(self.page, self.wrapper.locator('div[class="cart_block"]'))

    def click_logo(self):
        self.logo_button.click()

    def click_account(self):
        self.personal_account_button.click()

    def click_cart(self):
        self.personal_cart_button.click()

    def input_value_in_search(self, value: str):
        self.search_input.input(value)

    def click_search_button(self):
        self.search_button.click()

    def click_link_by_text(self, text: str):
        self.wrapper.get_by_text(text).click()

    def click_link_by_exact_text(self, text: str):
        self.wrapper.get_by_role('link', name=text, exact=True).click()
