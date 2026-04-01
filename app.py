import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to **PawPal+**, a pet care planning assistant.

This app helps a pet owner organize pet care tasks based on:
- time available
- task priority
- owner preferences
"""
)

# Session state setup
if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan", available_minutes=60, preferences="")

owner = st.session_state.owner

with st.expander("Owner + Pet Info", expanded=True):
    owner.name = st.text_input("Owner name", value=owner.name)
    owner.available_minutes = st.number_input(
        "Time available today (minutes)",
        min_value=10,
        max_value=300,
        value=owner.available_minutes
    )
    owner.preferences = st.text_input("Owner preferences", value=owner.preferences)

    pet_name = st.text_input("Pet name", value="Mochi")
    species = st.selectbox("Species", ["dog", "cat", "other"])

    if st.button("Add pet"):
        existing_pet = owner.get_pet(pet_name)
        if existing_pet is None:
            owner.add_pet(Pet(name=pet_name, species=species))
            st.success(f"{pet_name} was added!")
        else:
            st.warning("That pet already exists.")

st.divider()

st.subheader("Add Tasks")

if owner.pets:
    pet_names = [pet.name for pet in owner.pets]
    selected_pet_name = st.selectbox("Choose pet", pet_names)

    col1, col2, col3 = st.columns(3)
    with col1:
        task_title = st.text_input("Task title", value="Morning walk")
    with col2:
        duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    with col3:
        priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add task"):
        pet = owner.get_pet(selected_pet_name)
        if pet:
            new_task = Task(
                title=task_title,
                duration_minutes=int(duration),
                priority=priority
            )
            pet.add_task(new_task)
            st.success(f"Task added for {selected_pet_name}!")

    st.markdown("### Current Tasks")
    found_tasks = False
    for pet in owner.pets:
        if pet.tasks:
            found_tasks = True
            st.write(f"**{pet.name} ({pet.species})**")
            st.table(
                [
                    {
                        "title": task.title,
                        "duration_minutes": task.duration_minutes,
                        "priority": task.priority
                    }
                    for task in pet.tasks
                ]
            )

    if not found_tasks:
        st.info("No tasks yet. Add one above.")

else:
    st.info("Add a pet first.")
st.markdown("### Edit Existing Task")

pets_with_tasks = [pet for pet in owner.pets if pet.tasks]

if pets_with_tasks:
    edit_pet_name = st.selectbox(
        "Choose pet to edit task",
        [pet.name for pet in pets_with_tasks],
        key="edit_pet_select"
    )

    edit_pet = owner.get_pet(edit_pet_name)

    if edit_pet and edit_pet.tasks:
        selected_task_title = st.selectbox(
            "Choose task to edit",
            [task.title for task in edit_pet.tasks],
            key="edit_task_select"
        )

        selected_task = next(
            (task for task in edit_pet.tasks if task.title == selected_task_title),
            None
        )

        if selected_task:
            edited_title = st.text_input("New task title", value=selected_task.title, key="edited_title")
            edited_duration = st.number_input(
                "New duration (minutes)",
                min_value=1,
                max_value=240,
                value=selected_task.duration_minutes,
                key="edited_duration"
            )
            edited_priority = st.selectbox(
                "New priority",
                ["low", "medium", "high"],
                index=["low", "medium", "high"].index(selected_task.priority),
                key="edited_priority"
            )

            if st.button("Save task changes"):
                updated = edit_pet.update_task(
                    old_title=selected_task_title,
                    new_title=edited_title,
                    new_duration=int(edited_duration),
                    new_priority=edited_priority
                )

                if updated:
                    st.success("Task updated successfully!")
                    st.rerun()
                else:
                    st.error("Task could not be updated.")
else:
    st.info("Add tasks first if you want to edit them.")
    
st.divider()

st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler(owner)
    schedule, reasoning = scheduler.build_schedule()

    if schedule:
        st.success("Schedule generated successfully!")

        st.markdown("### Today's Plan")
        st.table(
            [
                {
                    "pet": pet_name,
                    "task": task.title,
                    "duration": task.duration_minutes,
                    "priority": task.priority
                }
                for pet_name, task in schedule
            ]
        )

        st.markdown("### Why this plan was chosen")
        for reason in reasoning:
            st.write(f"- {reason}")
    else:
        st.warning("No tasks could fit into the available time.")