import streamlit as st
import time
import json
from pathlib import Path


st.set_page_config(
    page_title="Course Management",
    page_icon="",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("Course Management App")
st.divider()

next_assignment_id_number = 3

assignments = [
    {
        "id": "HW1",
        "title": "Introduction to Database",
        "points": 100,
        "type": "homework",
        "description": "Intro to databases"
    },
    {
        "id": "HW2",
        "title": "Normalization",
        "points": 100,
        "type": "lab",
        "description": "Normalization concepts"
    }
]

json_path = Path("assignments.json")

if json_path.exists():
    with json_path.open("r", encoding="utf-8") as f:
        assignments = json.load(f)

tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Update an Assignment"])

# -----------------------
# TAB 1 VIEW / SEARCH
# -----------------------

with tab1:

    tab_option = st.radio("View/Search", ["View", "Search"])

    if tab_option == "View":
        st.dataframe(assignments)

    else:
        titles = []

        for assignment in assignments:
            titles.append(assignment["title"])

        selected_title = st.selectbox("Select a title", titles, key="selected_title")

        selected_assignment = {}

        for assignment in assignments:
            if assignment["title"] == selected_title:
                selected_assignment = assignment
                break

        if selected_assignment:
            with st.expander("Assignment Details", expanded=True):
                st.markdown(f"### Title: {selected_assignment['title']}")
                st.markdown(f"Description: {selected_assignment['description']}")
                st.markdown(f"Type: **{selected_assignment['type']}**")


# -----------------------
# TAB 2 ADD ASSIGNMENT
# -----------------------

with tab2:

    st.markdown("## Add New Assignment")

    title = st.text_input("Title")

    description = st.text_area(
        "Description",
        placeholder="Normalization is covered here",
        help="Here you are entering the assignment details"
    )

    points = st.number_input("Points")

    assignment_type = st.radio("Type", ["Homework", "Lab"], horizontal=True)

    due_date = st.date_input("Due Date")

    btn_save = st.button("Save", use_container_width=True)

    if btn_save:

        if not title:
            st.warning("Title need to be provided!")

        else:
            with st.spinner("Assignment is being recorded..."):
                time.sleep(3)

                new_assignment_id = "HW" + str(next_assignment_id_number)

                assignments.append(
                    {
                        "id": new_assignment_id,
                        "title": title,
                        "description": description,
                        "points": points,
                        "type": assignment_type
                    }
                )

                with json_path.open("w", encoding="utf-8") as f:
                    json.dump(assignments, f)

                st.success("New Assignment is recorded!")
                st.dataframe(assignments)


# -----------------------
# TAB 3 UPDATE ASSIGNMENT
# -----------------------

with tab3:

    st.markdown("## Update Assignment")

    titles = []

    for assignment in assignments:
        titles.append(assignment["title"])

    selected_item = st.selectbox("Select assignment to update", titles)

    assignment_edit = {}

    for assignment in assignments:
        if assignment["title"] == selected_item:
            assignment_edit = assignment
            break

    if assignment_edit:

        edit_title = st.text_input(
            "Title",
            value=assignment_edit["title"],
            key=f"edit_title_{assignment_edit['id']}"
        )

        edit_description = st.text_area(
            "Description",
            value=assignment_edit["description"],
            key=f"edit_description_{assignment_edit['id']}"
        )

        btn_update = st.button(
            "Update",
            key="update_button",
            type="secondary",
            use_container_width=True
        )

        if btn_update:

            with st.spinner("Updating..."):
                time.sleep(3)

                assignment_edit["title"] = edit_title
                assignment_edit["description"] = edit_description

                with json_path.open("w", encoding="utf-8") as f:
                    json.dump(assignments, f)

                st.success("Updated!")
                st.rerun()