"""The hottest new db changes around

Revision ID: 98be1d14f054
Revises: d30ab2ee6175
Create Date: 2022-08-08 22:58:37.869955

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '98be1d14f054'
down_revision = 'd30ab2ee6175'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parent')
    op.drop_table('child')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('child',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('birthdate', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('height', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.Column('parent_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['parent_id'], ['parent.id'], name='child_parent_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='child_pkey')
    )
    op.create_table('parent',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('birthdate', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('height', sa.NUMERIC(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='parent_pkey')
    )
    # ### end Alembic commands ###
