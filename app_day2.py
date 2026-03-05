from runpy import run_path

import streamlit as st

#load assignments
st.title("Course Management APP")
st.header("Assignments")
st.subheader("Assignments Manager")

next_assignment_id_number = 0 


st.divider()


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

#add new assignment
st.markdown("# Add New Assignment")


#input

title = st.text_input("Title", placeholder = "ex. Homeowrk 1", 
                      help = "This is the name of the assignment")

description = st.text_area("Description", placeholder = "ex. database design...")

due_date = st.date_input("Due Date")
assignments_type = st.radio("Type", ["Homework", "Lab"])
points = st.number_input("Points")
#assignments_type2 = st.selectbox("Type", ["Homework", "Lab","Other"])
#if assignments_type2 == "Other":
#    assignments_type2 = st.text_input("Assignment Type")


#lab = st.checkbox("Lab")


with st.expander("Assignment Preview", expanded = True):
    st.markdown("## Live Preview")
    st.markdown(f"Title: {title}")

btn_save = st.button("Save", width ="stretch")

import time

import json
from pathlib import Path

json_path = Path("assignments.json")

if btn_save:
    with st.spinner('Saving the Assignment..'):
        time.sleep(5)
        if title == "":
            st.warning("Enter Assignment Title")

        else:
            #Add or Create a new Assignment
            new_assignment_id = "HW" + str(next_assignment_id_number)
            next_assignment_id_number += 1

        assignments.append(
            {
                "id": new_assignment_id,
                "title": title,
                "description": description,
                "points": points,
                "type": assignments_type,
            }


        )



if json_path.exists() or True:
    with json_path.open("w", encoding = "utf-8") as f:
        json.dump(assignments, f)



    st.success("Assignment is SAVED!")
    st.info("This is a new assignment")
    st.dataframe(assignments)


