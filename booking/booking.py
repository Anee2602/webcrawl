import os
import time

from selenium import webdriver

from pythonProject1.booking.booking_filtration import BookingFiltration


class Booking(webdriver.Edge):
    def __init__(self, driver_path=r"C:/Users/anush/Documents"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.maximize_window()

    def land_first_page(self):
        self.get("https://www.booking.com")
        ##time.sleep(20)

    def change_currency(self,currency='None'):
        currency_element = self.find_element_by_css_selector('button[data-tooltip-text="Choose your currency"]')
        currency_element.click()
        self.implicitly_wait(20)
        selected_currency_element = self.find_element_by_css_selector(f'a[data-modal-header-async-url-param*="changed_currency=1;selected_currency={currency}"]')
        selected_currency_element.click()

    def select_place_to_go(self,place_to_go):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place_to_go)
        self.implicitly_wait(20)
        f = self.find_element_by_css_selector('li[data-i="0"]')
        f.click()

    def select_dates(self,check_in_date, check_out_date):
        #self.implicitly_wait(20)
        check_in_element = self.find_element_by_css_selector(f'td[data-date="{check_in_date}"]')
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(f'td[data-date="{check_out_date}"]')
        check_out_element.click()

    def select_adults(self,count=1):
        #self.implicitly_wait(20)
        selection_element = self.find_element_by_id("xp__guests__toggle")
        selection_element.click()
        time.sleep(2)

        while True:
            decrease_adults_element=self.find_element_by_css_selector('button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()
            adults_value_element= self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute('value')

            if int(adults_value) == 1:
                break

        increase_adults_element = self.find_element_by_css_selector('button[aria-label="Increase number of Adults"]')

        for i in range(count-1):
           increase_adults_element.click()

    def click_search(self):
        search_button = self.find_element_by_css_selector('button[type="submit"]')
        search_button.click()

    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3,4,5)

        filtration.sort_price_lowest_first()























