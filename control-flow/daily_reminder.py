def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    match priority:
        case "high":
            if time_bound == "yes":
                print("Reminder: '" + task + "' is a high priority task that requires immediate attention today!")
            else:
                print("Reminder: '" + task + "' is a high priority task.")
        case "medium":
            if time_bound == "yes":
                print("Reminder: '" + task + "' is a medium priority task that requires immediate attention today!")
            else:
                print("Reminder: '" + task + "' is a medium priority task.")
        case "low":
            if time_bound == "no":
                print("Note: '" + task + "' is a low priority task. Consider completing it when you have free time.")
            else:
                print("Note: '" + task + "' is a low priority task.")
        case _:
            print("Note: '" + task + "' has an unknown priority level.")

if __name__ == "__main__":
    main()
