from datetime import datetime, timedelta

class DeliveryTracker:
 
    def __init__(self, historical_data):
        self.historical_data = historical_data
        self.average_delivery_time = self.calculate_average_delivery_time()
    def calculate_average_delivery_time(self):
        total_time = sum((end_time - start_time).total_seconds() for start_time, end_time in self.historical_data)
        return total_time / len(self.historical_data)
    def predict_delivery_time(self,current_location ,estimated_arrival_time):
        current_time = datetime.now()
        time_to_destination = (estimated_arrival_time - current_time).total_seconds()
        if time_to_destination > 0:
            adjusted_delivery_time = current_time + timedelta(seconds=self.average_delivery_time)
            return adjusted_delivery_time
        else:
            return "Package already arrived or delayed"

historical_data = [
 (datetime(2024, 6, 1, 10, 0, 0), datetime(2024, 6, 1, 11, 0, 0)),
 (datetime(2024, 6, 2, 9, 0, 0), datetime(2024, 6, 2, 10, 30, 0)),
]
tracker = DeliveryTracker(historical_data)
# Simulated real-time tracking update
current_location = "City A"
estimated_arrival_time = datetime(2024, 6, 3, 12, 0, 0)
estimated_delivery_time = tracker.predict_delivery_time( current_location, estimated_arrival_time)
print("Estimated delivery time:", estimated_delivery_time)