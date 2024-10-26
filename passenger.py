class Passenger:
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