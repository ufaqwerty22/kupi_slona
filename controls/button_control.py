from controls.base_control import BaseControl


class ButtonControl(BaseControl):
    def __init__(self, page: Page, wrapper: Locator):
        super().__init__(page, wrapper)
