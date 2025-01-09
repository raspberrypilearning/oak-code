from random import choice
cities = ["Athens","Berlin","Dublin","London","Madrid","Paris","Prague","Stockholm","Vienna"]

print("City hopping random planner")
trip = []
while len(trip) < 5:
    city = choice(cities)
    trip.append(city)
print(f"Itinerary: {trip}")


