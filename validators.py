from datetime import datetime
import re


def validate_input(name="", email="",username="", password=""):
    
    if name.strip() == "" or len(name.strip()) < 2:
        return {"status": False, "message": "invalid, Enter name please"}

    if not re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email):
        return {"status": False, "message": "Enter valid email "}

    if password.strip() == "":
        return {"status": False, "message": "Enter password"}

    if len(password) < 5:
        return {"status": False, "message": "Password is too short, < 5"}
    return {"status":True}
