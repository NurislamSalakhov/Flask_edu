from datetime import datetime

from config import app, db


class Human(db.Model):
    """Модель описания квартир"""
    id = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(30), index=True, unique=False)
    sec_name: str = db.Column(db.String(50), index=True, unique=False)
    photo: str = db.Column(db.String(1500), index=True, unique=False)
    gender: str = db.Column(db.String(10), index=True, unique=False)
    age: int = db.Column(db.String(3), index=True, unique=False)
    country: str = db.Column(db.String(50), index=True, unique=False)
    bio: str = db.Column(db.String(10000), index=True, unique=False)


class Flat(db.Model):
    """Модель описания квартир."""
    id = db.Column(db.Integer, primary_key=True)
    period: int = db.Column(db.String(10), unique=False)
    bathroom: int = db.Column(db.String(2), unique=False)
    floor: int = db.Column(db.String(3), unique=False)
    Square: int = db.Column(db.String(4), unique=False)
    city: str = db.Column(db.String(30), unique=False)
    rooms: str = db.Column(db.String(50),  unique=False)
    price: int = db.Column(db.String(10), unique=False)
    area: str = db.Column(db.String(50), unique=False)
