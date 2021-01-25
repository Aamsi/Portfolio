"""tables project et category

Revision ID: 32cac12d29be
Revises: 
Create Date: 2021-01-25 10:53:51.251254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32cac12d29be'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_category_id'), 'category', ['id'], unique=False)
    op.create_table('project',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('picture', sa.String(length=150), nullable=True),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title'),
    sa.UniqueConstraint('url')
    )
    op.create_index(op.f('ix_project_id'), 'project', ['id'], unique=False)
    op.create_table('projectcategory',
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projectcategory')
    op.drop_index(op.f('ix_project_id'), table_name='project')
    op.drop_table('project')
    op.drop_index(op.f('ix_category_id'), table_name='category')
    op.drop_table('category')
    # ### end Alembic commands ###
