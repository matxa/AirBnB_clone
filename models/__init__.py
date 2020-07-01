#!/usr/bin/python3
""" where the init lives """
from models.engine.file_storage import FileStorage


storage = FileStorage()

storage.reload()
