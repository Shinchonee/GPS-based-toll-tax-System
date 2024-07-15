#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Toll Tax Calculator

class TollTaxCalculator:
    def __init__(self):
        self.toll_rates = {
            'small_vehicle': 7,  # in rupees per km
            'medium_vehicle': 14,  # in rupees per km
            'large_vehicle': 21,  # in rupees per km
        }

    def calculate_distance(self, start_lat, start_long, end_lat, end_long):
        # This is a very simplified distance calculation, in a real system you would use a more accurate method
        # such as the Haversine formula or a geodesy library
        distance = ((end_lat - start_lat) ** 2 + (end_long - start_long) ** 2) ** 0.5
        return distance

    def calculate_toll_tax(self, vehicle_type, start_lat, start_long, end_lat, end_long):
        distance = self.calculate_distance(start_lat, start_long, end_lat, end_long)
        toll_rate = self.toll_rates[vehicle_type]
        toll_tax = distance * toll_rate
        return toll_tax

def main():
    calculator = TollTaxCalculator()

    vehicle_type = input("Enter vehicle type (small_vehicle, medium_vehicle, large_vehicle): ")
    start_lat = float(input("Enter start latitude: "))
    start_long = float(input("Enter start longitude: "))
    end_lat = float(input("Enter end latitude: "))
    end_long = float(input("Enter end longitude: "))

    toll_tax = calculator.calculate_toll_tax(vehicle_type, start_lat, start_long, end_lat, end_long)
    print(f"The toll tax for your journey is: Rs{toll_tax:.2f}")

if __name__ == "__main__":
    main()


# In[ ]:




