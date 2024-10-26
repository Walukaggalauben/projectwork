class FlightClass:
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