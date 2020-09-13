"""empty message

Revision ID: d53283a9036a
Revises: 2f7016363a80
Create Date: 2020-07-21 10:49:09.527323

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd53283a9036a'
down_revision = '2f7016363a80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address1', sa.String(length=150), nullable=False),
    sa.Column('address2', sa.String(length=150), nullable=True),
    sa.Column('address3', sa.String(length=150), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_address')
    # ### end Alembic commands ###
