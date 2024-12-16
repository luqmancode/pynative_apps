"""Initial Migrations

Revision ID: f6061f55151b
Revises: 
Create Date: 2024-12-15 19:09:41.104956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6061f55151b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    query = ("CREATE TABLE IF NOT EXISTS api_release(build_date "
             "datetime, version varchar(30) primary key, links "
             "varchar(30), methods varchar(30))")
    op.execute(sa.text(query))


def downgrade() -> None:
    query = ("DROP TABLE IF EXISTS api_release")
    op.execute(sa.text(query))
