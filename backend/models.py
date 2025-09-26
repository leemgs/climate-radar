from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(64), unique=True, nullable=False, index=True)
    role = Column(String(32), nullable=False)  # citizen | volunteer | admin
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    vulnerability = Column(String(128), nullable=True)  # e.g., elderly, with_children

    requests = relationship("HelpRequest", back_populates="requester", foreign_keys="HelpRequest.user_id")
    assigned = relationship("HelpRequest", back_populates="assignee", foreign_keys="HelpRequest.assigned_volunteer_id")

class WeatherDatum(Base):
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    temperature = Column(Float, nullable=True)
    rainfall_mm_h = Column(Float, nullable=True)
    river_level_pct = Column(Float, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

class HelpRequest(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(String(24), default="unassigned")  # unassigned | assigned | resolved
    request_type = Column(String(32), nullable=False)  # water | medical | transport | other
    description = Column(Text, nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    assigned_volunteer_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    requester = relationship("User", foreign_keys=[user_id], back_populates="requests")
    assignee = relationship("User", foreign_keys=[assigned_volunteer_id], back_populates="assigned")
