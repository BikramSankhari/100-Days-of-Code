from sheet_manager import Sheet
from flight_manager import FlightManager

sheet = Sheet()

while sheet.has_more_place():
    sheet.get_next_place()
    flight_manager = FlightManager(sheet.city, sheet.iata_code, sheet.lowest_price)

    if sheet.iata_code == '':
        sheet.iata_code = flight_manager.get_iata_code()
        sheet.update_iata_code()

    flight_manager.search_cheap_rate()

