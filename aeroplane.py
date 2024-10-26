class Aeroplane:
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