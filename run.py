from booking.booking import Booking

try:
    bot = Booking()
    bot.land_first_page()
    bot.change_currency(currency="USD")
    bot.select_place_to_go('Florida')
    bot.select_dates(check_in_date='2022-02-18', check_out_date='2022-02-28')
    bot.select_adults(10)
    bot.click_search()
    bot.apply_filtrations()

except Exception as e:
    print("There is a problem running this program")