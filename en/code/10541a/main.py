days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday",                 
"Friday"]
timeslots = ["9am - 11am", "11am - 1pm", "2pm - 4pm"]
subjects = ["Maths", "English", "Biology", "History"]

for day in days_of_week:
    print(f"Revision Timetable for {day}:")
    for slot in timeslots:
        print(f"  {slot}")
        for subject in subjects:
            print(f"   - {subject}")