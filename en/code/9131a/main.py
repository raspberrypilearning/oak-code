from random import choice
cities = ["Athens","Berlin","Dublin","London","Madrid","Paris","Prague","Stockholm","Vienna"]
city = choice(cities)
print("City hopping random planner")
trip = []
while len(trip) < 5:
    trip.append(city)
print("Itinerary:", trip)


