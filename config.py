import os

class Config:

    SECRET_KEY = "securetrace-secret"

    JWT_SECRET_KEY = "securetrace-jwt"

    SQLALCHEMY_DATABASE_URI = \
        "sqlite:///securetrace.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
