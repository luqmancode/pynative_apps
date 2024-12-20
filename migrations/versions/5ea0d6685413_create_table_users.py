"""create table users

Revision ID: 5ea0d6685413
Revises: 1518ebe8ce2e
Create Date: 2024-12-19 08:25:51.804668

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ea0d6685413'
down_revision: Union[str, None] = '1518ebe8ce2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    query = ("CREATE TABLE IF NOT EXISTS users(id integer primary key "
             "autoincrement, "
             "username varchar(30) unique, "
             "email varchar(30) unique, "
             "password varchar(200), "
             "full_name varchar(30));")
    op.execute(sa.text(query))


def downgrade() -> None:
    query = "DROP TABLE IF EXISTS users"
    op.execute(sa.text(query))
