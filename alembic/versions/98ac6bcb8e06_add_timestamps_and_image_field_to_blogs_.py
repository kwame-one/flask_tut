"""add timestamps and image field to blogs table'


Revision ID: 98ac6bcb8e06
Revises: 7c321abc47cf
Create Date: 2023-06-17 13:22:14.178236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98ac6bcb8e06'
down_revision = '7c321abc47cf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('blogs', sa.Column('image', sa.String(191), nullable=True))
    op.add_column('blogs', sa.Column('created_at', sa.TIMESTAMP, nullable=True))


def downgrade() -> None:
    op.drop_column('blogs', 'created_at')
    op.drop_column('blogs', 'image')
