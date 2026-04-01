from pawpal_system import Task, Pet, Owner, Scheduler


def test_mark_complete_like_behavior():
    task = Task("Walk", 20, "high")
    assert task.title == "Walk"
    assert task.duration_minutes == 20
    assert task.priority == "high"


def test_add_task_to_pet():
    pet = Pet("Mochi", "dog")
    pet.add_task(Task("Feed", 10, "high"))
    assert len(pet.tasks) == 1


def test_schedule_prioritizes_high_priority_tasks():
    owner = Owner("Jordan", available_minutes=30)

    pet = Pet("Mochi", "dog")
    pet.add_task(Task("Low priority task", 20, "low"))
    pet.add_task(Task("High priority task", 20, "high"))

    owner.add_pet(pet)

    scheduler = Scheduler(owner)
    schedule, _ = scheduler.build_schedule()

    assert schedule[0][1].title == "High priority task"


def test_update_task_changes_values():
    pet = Pet("Mochi", "dog")
    pet.add_task(Task("Walk", 20, "high"))

    updated = pet.update_task("Walk", "Evening Walk", 30, "medium")

    assert updated is True
    assert pet.tasks[0].title == "Evening Walk"
    assert pet.tasks[0].duration_minutes == 30
    assert pet.tasks[0].priority == "medium"