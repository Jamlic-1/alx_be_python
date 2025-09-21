# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        desc = f"'{task}' is a high priority task"
    case "medium":
        desc = f"'{task}' is a medium priority task"
    case "low":
        desc = f"'{task}' is a low priority task"
    case _:
        desc = f"'{task}' has an undefined priority"

if time_bound == "yes":
    print(f"Reminder: {desc} that requires immediate attention today!")
else:
    print(f"Note: {desc}. Consider completing it when you have free time.")
