#!/usr/bin/python3
"""class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """classes that inherit from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""