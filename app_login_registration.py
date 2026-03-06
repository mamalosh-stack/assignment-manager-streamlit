import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

# Page configuration
st.set_page_config(
    page_title="Course Manager",
    layout="centered"
)

st.title("Course Manager")


# Data Loading Logic

json_file = Path("users.json")

if json_file.exists():
    with open(json_file, "r") as file:
        users = json.load(file)
else:
    users = [
        {
            "id": "1",
            "email": "admin@school.edu",
            "full_name": "System Admin",
            "password": "123ssag@43AE",
            "role": "Admin",
            "registered_at": "..."
        }
    ]

    with open(json_file, "w") as file:
        json.dump(users, file, indent=4)

# Navigation

page = st.sidebar.radio("Navigation", ["Register", "Login"])


# Registration Page

if page == "Register":

    with st.container():
        st.subheader("New Instructor Account")

        email = st.text_input("Email Address")
        name = st.text_input("First and Last Name")
        password = st.text_input("Password", type="password")
        role = st.selectbox("Role", ["Instructor"])

        if st.button("Create Account"):

            with st.spinner("Creating your account..."):
                time.sleep(2)

                new_user = {
                    "id": str(uuid.uuid4()),
                    "email": email,
                    "full_name": name,
                    "password": password,
                    "role": role,
                    "registered_at": str(datetime.now())
                }

                users.append(new_user)

                with open(json_file, "w") as file:
                    json.dump(users, file, indent=4)

            st.success("Account created successfully!")


# Login Page

if page == "Login":

    with st.container():
        st.subheader("Login")

        login_email = st.text_input("Email")
        login_password = st.text_input("Password", type="password")

        if st.button("Log In"):

            with st.spinner("Verifying credentials..."):
                time.sleep(2)

                found_user = None

                for user in users:
                    if user["email"] == login_email and user["password"] == login_password:
                        found_user = user
                        break

                if found_user:
                    st.success(f"Welcome back, {found_user['full_name']}! Role: {found_user['role']}")
                else:
                    st.error("Invalid email or password.")

    st.divider()

    st.subheader("User Database")

    st.dataframe(users)