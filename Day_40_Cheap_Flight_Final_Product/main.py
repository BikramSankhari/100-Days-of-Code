from sheet_manager import Sheet
from flight_manager import FlightManager

sheet = Sheet()

while True:
    new_customer = input("Do you want to register a new customer? (Y/N) ").lower()
    if new_customer == 'y':
        sheet.add_new_customer()
    else:
        break

while sheet.has_more_place():
    sheet.get_next_place()
    flight_manager = FlightManager(sheet.city, sheet.iata_code, sheet.lowest_price, sheet.customer_list)

    if sheet.iata_code == '':
        sheet.iata_code = flight_manager.get_iata_code()
        sheet.update_iata_code()

    flight_manager.search_cheap_rate()

