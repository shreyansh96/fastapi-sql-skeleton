from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, VARCHAR, DateTime
from sqlalchemy.orm import relationship
from db.session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    email_id = Column(String(20))
    address = Column(String(100))
    mobile_no = Column(VARCHAR(15))
    country_code = Column(Integer)
    created_date = Column(DateTime)
    modified_date = Column(DateTime)

    # items = relationship("Item", back_populates="owner")
