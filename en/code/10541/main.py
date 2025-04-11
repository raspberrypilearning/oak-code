days_of_week = ["Monday", "Tuesday", "Wednesday", 
                "Thursday", "Friday"]
lesson_slots = ["9am - 10am", "10am - 11am", "11am - 12pm", 
    "1pm - 2pm", "2pm - 3pm"]

for day in days_of_week:
    print(f"Timetable for {day}:")
    for slot in lesson_slots:
        print(f"  {slot}")
    print()
