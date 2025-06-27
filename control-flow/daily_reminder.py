def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            reminder = "Reminder: '" + task + "' is a high priority task"
        case "medium":
            reminder = "Reminder: '" + task + "' is a medium priority task"
        case "low":
            reminder = "Note: '" + task + "' is a low priority task"
        case _:
            reminder = "Note: '" + task + "' has an unknown priority level"

    if time_bound == "yes" and priority in ("high", "medium"):
        reminder += " that requires immediate attention today!"
    elif time_bound == "no" and priority == "low":
        reminder += ". Consider completing it when you have free time."
    elif time_bound == "no" and priority in ("high", "medium"):
        reminder += ". You can schedule it for later."

    print(reminder)


if __name__ == "__main__":
    main()
