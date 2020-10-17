from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, Date
)

__all__ = ['employee']

meta = MetaData()

employee = Table(
    'employee', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(200), nullable=False),
    Column('pub_date', Date, nullable=False)
)
