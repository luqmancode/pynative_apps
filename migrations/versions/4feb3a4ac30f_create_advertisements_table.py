"""create advertisements table

Revision ID: 4feb3a4ac30f
Revises: 5ea0d6685413
Create Date: 2024-12-19 17:22:36.649155

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4feb3a4ac30f'
down_revision: Union[str, None] = '5ea0d6685413'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    query = ("CREATE TABLE IF NOT EXISTS advertisements(id integer "
             "primary key autoincrement, "
             "username varchar(30), "
             "header varchar(120), "
             "industry varchar(100), "
             "content text, "
             "date_created datetime, "
             "date_updated datetime);")
    op.execute(sa.text(query))


def downgrade() -> None:
    query = "DROP TABLE IF EXISTS advertisements;"
    op.execute(sa.text(query))
