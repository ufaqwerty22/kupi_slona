from components.base_component import BaseComponent
from controls.button_control import ButtonControl
from controls.input_control import InputControl


class ProductCardComponent(BaseComponent):
    def __init__(self, page: Page, title: str):
        super().__init__(page, page.locator(f'//a[contains(text(), "{title}")]/ancestor::li'))
        self.title_card_button = ButtonControl(self.page, self.wrapper.get_by_text(title))
        self.count_input = InputControl(self.page, self.wrapper.get_by_role('textbox'))
        self.buy_button = ButtonControl(self.page, self.wrapper.locator('input[value="Купить"]'))

    def click_on_title(self):
        self.title_card_button.click()

    def input_count(self, count: str):
        self.count_input.input(count)

    def click_buy_button(self):
        self.buy_button.click()