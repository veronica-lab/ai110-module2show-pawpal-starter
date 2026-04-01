# PawPal+ Project Reflection

## 1. System Design
Core actions
    track actions
    consider time and schedules
    produce daily plans

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML design used four main classes: `Task`, `Pet`, `Owner`, and `Scheduler`.

The `Task` class was responsible for representing one pet care action. I designed it to store the task title, duration in minutes, and priority level. I also included a helper method to convert the text priority into a numeric value so the scheduler could compare tasks more easily.

The `Pet` class represented an individual pet and stored basic information like the pet’s name, species, and list of tasks. Its main responsibility was to manage the tasks that belong to that pet.

The `Owner` class represented the pet owner. I gave it responsibility for storing the owner’s name, available time, preferences, and pets.

The `Scheduler` class was the logic layer of the system. Its responsibility was to gather tasks from the owner’s pets, sort them based on priority and duration, and build a daily plan that fits into the owner’s available time. It also returned reasoning so the app could explain why tasks were chosen or skipped!


**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
Yes, my design changed during implementation. At first, I thought about adding more complexity, such as separate classes for constraints or schedule entries, but I decided that would make the project harder to finish and more difficult to connect to the Streamlit UI.
I simplified the design so that the main scheduling behavior stayed inside the `Scheduler` class. This made the project easier to understand and better matched the scope of the assignment. 
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
My scheduler considers three main things: the owner’s available time, the priority of each task, and task duration. The most important constraint is time, because the whole point of the app is to create a realistic daily plan that fits within the owner’s schedule
- How did you decide which constraints mattered most?
I decided these constraints mattered most because they were the clearest and most practical for a first version of the system. They also matched the project scenario well. 
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff my scheduler makes is that it uses a simple rule-based approach instead of a more advanced scheduling algorithm
- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable for this scenario because the goal of the app is to produce a useful daily plan without unnecessary complexity. A more advanced scheduler could consider exact times, recurring tasks, or overlapping events in more detail, but for this version, a simpler approach makes the behavior easier to understand, test, and explain.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI tools during several parts of the project, especially for brainstorming the class design, drafting a UML structure, generating starter code, and improving the implementation. AI was also helpful for turning the design into Python dataclasses, suggesting how the classes should connect, and helping me think through how to structure the scheduler.
- What kinds of prompts or questions were most helpful?
The most helpful prompts were specific ones that described the project goal and clearly listed the classes, attributes, and responsibilities I wanted.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
One moment where I did not accept an AI suggestion as-is was when more complexity was suggested than I actually needed, such as adding extra classes or making the scheduling logic more advanced than the assignment required
- How did you evaluate or verify what the AI suggested?
I verified the final approach by checking whether it matched the project requirements, whether the code was understandable, and whether I could test it easily. 
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested several important behaviors in the system. First, I tested that tasks could be added to a pet successfully. Second, I tested that the scheduler generated a plan in the correct order based on priority. Third, I tested that the core task data was stored correctly when task objects were created.
- Why were these tests important?
These tests were important because they covered the main functionality of the app. If tasks cannot be added correctly or if the scheduler does not prioritize tasks properly, then the app would not be fulfilling its main purpose. Testing these behaviors gave me more confidence that the classes were working together correctly.

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am fairly confident that my scheduler works correctly for the main project requirements. It successfully builds a daily plan, prioritizes more important tasks, and respects the owner’s available time.
- What edge cases would you test next if you had more time?
If I had more time, I would test additional edge cases. For example, I would test what happens when there are no pets, when a pet has no tasks, when several tasks have the same priority, when a task duration is longer than the owner’s entire available time, and when preferences should affect the order of the schedule more directly.
---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I am happy that the scheduler not only builds a plan but also explains why tasks were chosen, because that makes the app feel more useful and thoughtful.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
If I had another iteration, I would improve the scheduler by making it smarter about preferences, recurring tasks, and exact scheduling times. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned from this project is that designing the system clearly before coding makes implementation much easier. Having a simple UML and defined class responsibilities helped me stay organized and avoid unnecessary complexity.
I also learned that AI is most useful when I treat it as a collaborator instead of blindly accepting every suggestion