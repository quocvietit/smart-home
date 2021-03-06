"""empty message

Revision ID: 188d30d30909
Revises: 
Create Date: 2019-03-30 11:57:22.321885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '188d30d30909'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('device',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=False),
    sa.Column('last_activity', sa.DateTime(), nullable=True),
    sa.Column('is_connect', sa.Boolean(), nullable=False),
    sa.Column('is_enable', sa.Boolean(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['type_id'], ['type.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Text(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], ['device.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('history')
    op.drop_table('device')
    op.drop_table('type')
    # ### end Alembic commands ###
