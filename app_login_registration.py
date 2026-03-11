import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time


# Page Configuration

st.set_page_config(
    page_title="Course Manager",
    layout="centered"
)

st.title("Course Manager")
st.divider()


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
            "registered_at": str(datetime.now())
        }
    ]

    with open(json_file, "w") as file:
        json.dump(users, file, indent=4)


# Tabs Navigation

register_tab, login_tab = st.tabs(["Register", "Login"])


# Register Tab

with register_tab:

    with st.container():
        st.subheader("New Instructor Account")

        reg_email = st.text_input("Email Address")
        reg_name = st.text_input("First and Last Name")
        reg_password = st.text_input("Password", type="password")
        reg_role = st.selectbox("Role", ["Instructor"])

        if st.button("Create Account"):

            with st.spinner("Creating your account..."):
                time.sleep(2)

                new_user = {
                    "id": str(uuid.uuid4()),
                    "email": reg_email,
                    "full_name": reg_name,
                    "password": reg_password,
                    "role": reg_role,
                    "registered_at": str(datetime.now())
                }

                users.append(new_user)

                with open(json_file, "w") as file:
                    json.dump(users, file, indent=4)

            st.success("Account created successfully!")


# Login Tab

with login_tab:

    with st.container():
        st.subheader("Login")

        login_email = st.text_input("Email Address")
        login_password = st.text_input("Password", type="password")

        if st.button("Log In"):

            with st.spinner("Verifying credentials..."):
                time.sleep(2)

                user_found = None

                for user in users:
                    if user["email"] == login_email and user["password"] == login_password:
                        user_found = user
                        break

                if user_found:
                    st.success(f"Welcome back {user_found['full_name']}! Role: {user_found['role']}")
                else:
                    st.error("Invalid email or password.")

    st.divider()
   

   