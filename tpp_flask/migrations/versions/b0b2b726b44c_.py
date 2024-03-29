"""empty message

Revision ID: b0b2b726b44c
Revises: 23f5aae64799
Create Date: 2019-01-24 09:24:57.703834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0b2b726b44c'
down_revision = '23f5aae64799'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('good_id', sa.String(length=32), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.Column('good_name', sa.String(length=255), nullable=False),
    sa.Column('show_img', sa.String(length=255), nullable=True),
    sa.Column('good_desc', sa.String(length=255), nullable=True),
    sa.Column('good_price', sa.Numeric(precision=11, scale=2), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('good_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goods')
    # ### end Alembic commands ###
