import streamlit as st
import time
import json
from pathlib import Path

st.title("Course Management App")
st.divider()

next_assignment_id_number = 3

assignments = [
    {   "id": "HW1",
        "title": "Introduction to Database",
        "points": 100,
        "type": "homework" },
    {   "id": "HW2",
        "title": "Normalization",
        "points": 100,
        "type": "lab" }
]

json_path = Path("assignments.json")

if json_path.exists():
    with json_path.open("r", encoding="utf-8") as f:
        assignments = json.load(f)

tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Update an Assignment"])

with tab1:
    tab_option = st.radio("View/Search", ["View", "Search"])
    st.dataframe(assignments)

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
    st.caption("Homework type")

    assignment_type2 = st.selectbox("Type", ["Select an option", "Homework", "Lab", "Other"])

    if assignment_type2 == "Other":
        assignment_type2 = st.text_input("Type", placeholder="Enter the assignment type")

    due_date = st.date_input("Due Date")

with tab3:
    st.info("Maybe coming soon...")