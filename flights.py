class Flights:
    def __init__(self,flight_id,departure_airport,arrival_airport,departure_time,arrival_time,flight_duration,airline,plane_no):
        self.__flight_id = flight_id
        self.departure_airport = departure_airport 
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.flight_duration = flight_duration
        self.airline = airline
        self.__plane_no = plane_no
    def __str__(self):
        return f"Departure airport:{self.departure_airport}\n Arrival airport:{self.arrival_airport}\n Departure time:{self.departure_time}\n Arrival time:{self.arrival_time}\n Flight duration:{self.flight_duration}\n Airline:{self.airline}"    

    def set_flight_id(self,flight_id):
        self.__flight_id = flight_id
    def get_flight_id(self):
        return self.__flight_id
    def set_plane_no(self,plane_no):
        self.__plane_no = plane_no
    def get_plane_no(self):
        return self.__plane_no