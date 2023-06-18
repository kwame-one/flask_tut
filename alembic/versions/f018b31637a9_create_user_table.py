"""create user table

Revision ID: f018b31637a9
Revises: 98ac6bcb8e06
Create Date: 2023-06-18 13:22:26.176454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func

revision = 'f018b31637a9'
down_revision = '98ac6bcb8e06'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(191), unique=True, nullable=False),
        sa.Column('password', sa.String(191), nullable=False),
        sa.Column('created_at', sa.DATETIME, nullable=True, server_default=func.now()),
    )


def downgrade() -> None:
    op.drop_table('users')
