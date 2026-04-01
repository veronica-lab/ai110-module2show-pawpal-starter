from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    owner = Owner("Jordan", available_minutes=45, preferences="Prioritize important tasks first")

    dog = Pet("Mochi", "dog")
    cat = Pet("Luna", "cat")

    dog.add_task(Task("Morning walk", 20, "high"))
    dog.add_task(Task("Feed breakfast", 10, "high"))
    cat.add_task(Task("Play time", 15, "medium"))
    cat.add_task(Task("Brush fur", 25, "low"))

    owner.add_pet(dog)
    owner.add_pet(cat)

    scheduler = Scheduler(owner)
    schedule, reasoning = scheduler.build_schedule()

    print("\n=== TODAY'S SCHEDULE ===")
    for pet_name, task in schedule:
        print(f"{pet_name}: {task.title} ({task.duration_minutes} min, {task.priority})")

    print("\n=== REASONING ===")
    for reason in reasoning:
        print(f"- {reason}")


if __name__ == "__main__":
    main()