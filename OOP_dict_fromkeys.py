class Postman:
    def __init__(self):
        self.delivery_data = []
        
    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))
    
    def get_houses_for_street(self, street):
        house = [h for s, h, a in self.delivery_data if s == street]
        return list(dict.fromkeys(house))
    
    def get_flats_for_house(self, street, house):
        apartment = [a for s, h, a in self.delivery_data if s == street and h == house]
        return list(dict.fromkeys(apartment))
