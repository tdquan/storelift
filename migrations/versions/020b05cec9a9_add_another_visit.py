"""add another visit

Revision ID: 020b05cec9a9
Revises: d9dda16f4953
Create Date: 2020-02-21 22:24:43.482029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '020b05cec9a9'
down_revision = 'd9dda16f4953'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visit',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('time_enter', sa.DateTime(), nullable=False),
    sa.Column('time_exit', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('visit')
    # ### end Alembic commands ###
