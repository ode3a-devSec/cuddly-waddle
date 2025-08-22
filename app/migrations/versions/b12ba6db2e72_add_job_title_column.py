"""add_job_title column

Revision ID: b12ba6db2e72
Revises: b358ce8a2026
Create Date: 2025-08-22 10:38:05.710463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b12ba6db2e72'
down_revision: Union[str, Sequence[str], None] = 'b358ce8a2026'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "employee",
        sa.Column("job_title", sa.String(64), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("employee","job_title")
