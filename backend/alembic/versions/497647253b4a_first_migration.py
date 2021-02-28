"""first migration

Revision ID: 497647253b4a
Revises:
Create Date: 2021-02-28 17:07:36.478134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '497647253b4a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('user')
