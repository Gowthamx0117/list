import streamlit as st

# Title
st.title("✅ Simple To-Do List App")
st.write("Manage your daily tasks efficiently!")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

new_task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append(new_task)
        st.rerun()

st.subheader("Your Tasks:")
for i, task in enumerate(st.session_state.tasks):
    col1, col2 = st.columns([4, 1])
    col1.write(f"- {task}")
    if col2.button("❌", key=i):
        st.session_state.tasks.pop(i)
        st.rerun()
