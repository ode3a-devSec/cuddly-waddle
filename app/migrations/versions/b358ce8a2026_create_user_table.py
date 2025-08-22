"""Create User table

Revision ID: b358ce8a2026
Revises: 
Create Date: 2025-08-22 10:19:34.694521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b358ce8a2026'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "employee",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("current", sa.Boolean, default=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("employee")
