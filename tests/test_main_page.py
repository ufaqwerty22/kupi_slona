import time

from playwright.sync_api import Page, expect
from pages.main_page import MainPage


def test_main_page(page: Page):
    main_page = MainPage(page)
    main_page.open()
    backpack_card = main_page.get_product_card_component('Рюкзак «Star cat»')
    backpack_card.click_on_title()
    main_page.open()
    backpack_card.input_count("12")
    backpack_card.click_buy_button()
    main_page.open()
    stickers_card = main_page.get_product_card_component('Набор наклеек')
    stickers_card.input_count("1")
    stickers_card.click_buy_button()