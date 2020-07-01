#!/usr/bin/python3
""" User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """User Attributes"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
