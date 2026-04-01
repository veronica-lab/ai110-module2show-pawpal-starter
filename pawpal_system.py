from dataclasses import dataclass, field
from typing import List


@dataclass
class Task:
    """Represents one pet care task."""
    title: str
    duration_minutes: int
    priority: str

    def priority_value(self) -> int:
        """Convert priority label into a number for sorting."""
        values = {"high": 3, "medium": 2, "low": 1}
        return values.get(self.priority.lower(), 0)


@dataclass
class Pet:
    """Represents a pet and its care tasks."""
    name: str
    species: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Add a task to this pet."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Task]:
        """Return all tasks for this pet."""
        return self.tasks
    
    def update_task(self, old_title: str, new_title: str, new_duration: int, new_priority: str) -> bool:
        """Update a task by title."""
        for task in self.tasks:
            if task.title == old_title:
                task.title = new_title
                task.duration_minutes = new_duration
                task.priority = new_priority
                return True
        return False

@dataclass
class Owner:
    """Represents a pet owner with preferences and available time."""
    name: str
    available_minutes: int = 60
    preferences: str = ""
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the owner's list."""
        self.pets.append(pet)

    def get_pet(self, pet_name: str) -> Pet | None:
        """Find a pet by name."""
        for pet in self.pets:
            if pet.name.lower() == pet_name.lower():
                return pet
        return None

    def get_all_tasks(self) -> List[tuple[str, Task]]:
        """Return all tasks from all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.tasks:
                all_tasks.append((pet.name, task))
        return all_tasks


class Scheduler:
    """Builds a daily plan based on priority and available time."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def build_schedule(self) -> tuple[list[tuple[str, Task]], list[str]]:
        """
        Build a schedule using priority first, then shorter duration.
        Returns:
            schedule: list of (pet_name, task)
            reasoning: list of explanation strings
        """
        all_tasks = self.owner.get_all_tasks()

        sorted_tasks = sorted(
            all_tasks,
            key=lambda item: (-item[1].priority_value(), item[1].duration_minutes)
        )

        schedule = []
        reasoning = []
        used_minutes = 0

        for pet_name, task in sorted_tasks:
            if used_minutes + task.duration_minutes <= self.owner.available_minutes:
                schedule.append((pet_name, task))
                used_minutes += task.duration_minutes
                reasoning.append(
                    f"Chose '{task.title}' for {pet_name} because it is "
                    f"{task.priority} priority and fits in the remaining time."
                )
            else:
                reasoning.append(
                    f"Skipped '{task.title}' for {pet_name} because there was not enough time left."
                )

        return schedule, reasoning