#!/usr/bin/python3

"""
    Archivo de inicializacion para el modulo de models
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
