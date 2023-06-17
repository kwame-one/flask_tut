"""create blogs table

Revision ID: 7c321abc47cf
Revises: 
Create Date: 2023-06-17 13:13:24.935687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c321abc47cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'blogs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(191), nullable=False),
        sa.Column('content', sa.TEXT, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('blogs')
