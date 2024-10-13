from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Predictions(Base):
    __tablename__ = 'predictions'

    id = Column(Integer, primary_key=True)
    # profile_id = Column(Integer, ForeignKey('user_profile_info.id'))
    age = Column(Integer)
    sex = Column(Integer)
    cp = Column(Integer)
    resting_bp = Column(Integer)
    serum_cholesterol = Column(Integer)
    fasting_blood_sugar = Column(Integer)
    resting_ecg = Column(Integer)
    max_heart_rate = Column(Integer)
    exercise_induced_angina = Column(Integer)
    st_depression = Column(Float)
    st_slope = Column(Integer)
    number_of_vessels = Column(Integer)
    thallium_scan_results = Column(Integer)
    # predicted_on = Column(DateTime, default=datetime.utcnow)
    num = Column(Integer)

    profile = relationship("UserProfileInfo", back_populates="predict")

    def __repr__(self):
        return f"<Prediction(id={self.id}, profile_id={self.profile_id})>"
