"""creates role model

Revision ID: 3978fdde9f7b
Revises: a6232f32942c
Create Date: 2021-07-20 09:57:15.706476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3978fdde9f7b'
down_revision = 'a6232f32942c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('uuid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role')
    # ### end Alembic commands ###