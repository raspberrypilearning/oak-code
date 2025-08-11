import random

def collect_stream_duration():
    while True:
        stream_input = input("Enter the stream duration (20 to 40 minutes): ")
        if stream_input.isdigit():
            stream_minutes = int(stream_input)
            if stream_minutes >= 20 and stream_minutes <= 40:
                # Send the valid number back to the main program
                return stream_minutes          
            else:
                print("Please enter a number between 20 and 40")
        else:
            print("Please enter a numerical value.")

def display_stream_schedule(time, games):
    print("Stream summary:")
    stream_duration_minutes = time  // 60
    stream_duration_seconds = time % 60
    print(f"Total stream duration: {stream_duration_minutes} minutes and {stream_duration_seconds} seconds")
    print(f"Total games reviewed: {games}")  

def choose_giveaway(seconds):
    giveaway_time = random.randint(1, seconds)
    giveaway_minutes = giveaway_time // 60
    giveaway_seconds = giveaway_time % 60
    print(f"Giveaway time selected at {giveaway_minutes} minutes and {giveaway_seconds} seconds")


print ("Welcome to StreamScheduler")

stream_minutes = collect_stream_duration()
stream_seconds = stream_minutes * 60
total_time = 0
game_names = []
game_durations = []

while total_time < stream_seconds:
    game_name = input("Enter game name: ")
    game_names.append(game_name)
    valid_review = False

    while not valid_review: 
        review_duration = input("Enter review duration in seconds: ")
        review_seconds = int(review_duration)
        if total_time + review_seconds > stream_seconds:
            print (f"That review would make the stream too long.You only have {stream_seconds-total_time} seconds left.")
        else:
            valid_review = True 

    game_durations.append(review_seconds)
    total_time = total_time + review_seconds

print("\nEnough games entered for the stream!\n")

display_stream_schedule(total_time, len(game_names))
choose_giveaway(stream_seconds)