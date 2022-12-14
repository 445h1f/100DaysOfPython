class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, originCity, originAirport, destinationCity, destinationAirport, outDate, returnDate, stopOvers:int=0, viaCity:str='') -> None:
        self.price = price
        self.originCity = originCity
        self.originAirport = originAirport
        self.destinationCity = destinationCity
        self.destinationAirport = destinationAirport
        self.outDate = outDate
        self.returnDate = returnDate
        self.stopOvers = stopOvers
        self.viaCity = viaCity

