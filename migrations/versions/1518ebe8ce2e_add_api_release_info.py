"""Add api_release info

Revision ID: 1518ebe8ce2e
Revises: f6061f55151b
Create Date: 2024-12-15 20:35:20.773118

"""
from datetime import datetime
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1518ebe8ce2e'
down_revision: Union[str, None] = 'f6061f55151b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    query = ("""
        INSERT INTO api_release(build_date, version, links, methods)
        VALUES (:build_date, :version, :links, :methods)
    """)
    params = {
        "build_date": datetime.now().isoformat(),
        "version": "v1",
        "links": "/api/v1/users",
        "methods": "get, post, put, delete"
    }
    # Pass the query text and params directly
    op.execute(sa.text(query).bindparams(**params))


def downgrade() -> None:
    query = ("DELETE FROM api_release WHERE links =:links")
    params = {"links": '/api/v1/users'}
    op.execute(sa.text(query).bindparams(**params))
