from components.base_component import BaseComponent
from controls.button_control import ButtonControl


class FooterComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page, page.locator('#footer-wrapper'))
        self.vk_logo = ButtonControl(self.page, self.wrapper.locator('a[href="https://vk.com/kupislona_russia"]'))
        self.tg_logo = ButtonControl(self.page, self.wrapper.locator('a[href="https://t.me/kupislona_russia"]'))

    def click_vk_logo(self):
        self.vk_logo.click()

    def click_tg_logo(self):
        self.tg_logo.click()

    def click_link_by_text(self, text):
        self.wrapper.get_by_role('link', name=text).click()