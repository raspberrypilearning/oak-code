print ("Welcome to StreamScheduler")
valid_duration = False

while valid_duration == False:
    stream_input = input("Enter the stream duration (20 to 40 minutes):")
    if stream_input.isdigit():
        stream_minutes = int(stream_input)
        if stream_minutes < 20 or stream_minutes > 40:
            print("Please enter a number between 20 and 40")
        else:
            valid_duration = True
    else:
        print("Please enter a numerical value")

stream_seconds = stream_minutes * 60

game_names = []
game_durations = []
total_time = 0
game_name = input("Enter game name: ")
game_names.append(game_name)
review_duration = input("Enter review duration in seconds: ")
review_seconds = int(review_duration)
game_durations.append(review_seconds)
print(game_names)
print(game_durations)

total_time = total_time + review_seconds