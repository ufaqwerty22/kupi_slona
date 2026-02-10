from playwright.sync_api import Page, Locator


class BaseControl:
    def __init__(self, page: Page, wrapper: Locator):
        self.page: Page = page
        self.wrapper: Locator = wrapper

    def waitForLoad(self):
        return self.wrapper.wait_for()

    def waitForLoadInDOM(self):
        return self.wrapper.wait_for(state="attached")

    def input(self, value: str):
        self.wrapper.fill(value)

    def click(self):
        self.wrapper.click(force=True)