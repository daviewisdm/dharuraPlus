from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .config import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    blood_type = Column(String)
    medical_conditions = Column(String)
    contacts = relationship("EmergencyContact", back_populates="owner")

class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone_number = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="contacts")