class Airline:
    def __init__(self,airline_id,airline_name,airline_country,airline_location):
        self.__airline_id = ""
        self.airline_name = airline_name
        self.airline_country = airline_country
        self.airline_location = airline_location

    def __str__(self):
        return f"Airline name:{self.airline_name}\n Airline country:{self.airline_country}\nAirline location:{self.airline_location}"
    
    def set_airline_id(self,airline_id):
        self.__airline_id = airline_id
    def get_airline_id(self):
        return self.__airline_id