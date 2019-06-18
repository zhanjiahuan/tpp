"""empty message

Revision ID: 4dd26881380d
Revises: d3a6f100ed40
Create Date: 2018-12-13 14:48:27.205202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dd26881380d'
down_revision = 'd3a6f100ed40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seat_scheduling',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('seat_id', sa.Integer(), nullable=True),
    sa.Column('hall_id', sa.Integer(), nullable=True),
    sa.Column('hs_id', sa.Integer(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['hall_id'], ['hall.hid'], ),
    sa.ForeignKeyConstraint(['hs_id'], ['hall_scheduling.hsid'], ),
    sa.ForeignKeyConstraint(['seat_id'], ['seats.sid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seat_scheduling')
    # ### end Alembic commands ###
