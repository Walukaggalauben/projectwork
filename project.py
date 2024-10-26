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

class Aeroplane(Airline):
    def __init__(self,plane_no,plane_model,plane_capacity,plane_airline):
        self.__plane_no = plane_no
        self.plane_model = plane_model
        self.plane_capacity = plane_capacity
        self.plane_airline = plane_airline
    def __str__(self):
        return f"Plane model:{self.plane_model}\n Plane capacity:{self.plane_capacity}\n Plane airline:{self.plane_airline}"
    
    def set_plane_no(self,plane_no):
        self.__plane_no = plane_no
    def get_plane_no(self):
        return self.__plane_no

class Flights(Airline):
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
    
    
class FlightClass(Airline):
    def __init__(self,class_type,flight_id,capacity,fare):
        self.class_type = class_type
        self.__flight_id = flight_id 
        self.capacity = capacity
        self.fare = fare
    def __str__(self):
        return f"class type:{self.class_type}\ncapacity:{self.capacity}\nFare:{self.fare}"
        
    def set_flight_id(self,flight_id):
        self.__flight_id = flight_id
    def get_class_type(self):
        return self.__flight_id 
    
class Passenger(Airline):
    def __init__(self,passenger_id,passenger_name,contact,address,flight,passport_no,board_pass,class_no,seat_no):
        self.__passenger_id = passenger_id
        self.passenger_name = passenger_name 
        self.contact = contact
        self.address = address
        self.flight = flight
        self.passport_no = passport_no
        self.board_pass = board_pass
        self.class_no = class_no
        self.seat_no = seat_no
        
    def set_passenger_id(self,passenger_id):
        self.__passenger_id = passenger_id
    def get_passenger_id(self):
        return self.__passenger_id