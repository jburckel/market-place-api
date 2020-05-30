import sqlalchemy
from mpapi.database import metadata

products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("code", sqlalchemy.Text)
    sqlalchemy.Column("description", sqlalchemy.Text)

)
