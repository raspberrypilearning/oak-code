import random

print ("Welcome to StreamScheduler")

valid_duration = False

while valid_duration == False:
  stream_input = input("Enter the stream duration (20 to 40 minutes):")
  stream_minutes = int(stream_input)
  if stream_minutes < 20 or stream_minutes > 40:
    print("Please enter a number between 20 and 40")
  else:
     valid_duration = True

stream_seconds = stream_minutes * 60
total_time = 0
game_names = []
game_durations = []

while total_time < stream_seconds:
    game_name = input("Enter game name: ")
    game_names.append(game_name)
    review_duration = input("Enter review duration in seconds: ")
    review_seconds = int(review_duration)
    game_durations.append(review_seconds)
    total_time = total_time + review_seconds

print("\nEnough games entered for the stream!\n")

print("Stream summary:")
stream_duration_minutes = total_time  // 60
stream_duration_seconds = total_time % 60
print(f"Total stream duration: {stream_duration_minutes} minutes and {stream_duration_seconds} seconds")
print(f"Total games reviewed: {len(game_names)}")

giveaway_time = random.randint(1, stream_seconds)
giveaway_minutes = giveaway_time // 60
giveaway_seconds = giveaway_time % 60
print(f"Giveaway time selected at {giveaway_minutes} minutes and {giveaway_seconds} seconds")
