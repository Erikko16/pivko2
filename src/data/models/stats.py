from datetime import datetime, timedelta
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Boolean, Integer, String, DateTime,Float, VARCHAR, REAL

from ..database import db
from ..mixins import CRUDModel

class Stats(CRUDModel):
    __tablename__ = 'stats'
    __table_args__ = {'sqlite_autoincrement': True}
    id = Column(Integer, primary_key=True, autoincrement=True )
    cas = Column(DateTime, nullable=False, index=False)
    nadpis = Column(VARCHAR, nullable=False, index=True)
    CPU = Column(REAL, nullable=False,default=0)
    # Use custom constructor
    # pylint: disable=W0231
    def __init__(self, **kwargs):
        for k, v in kwargs.iteritems():
            setattr(self, k, v)

