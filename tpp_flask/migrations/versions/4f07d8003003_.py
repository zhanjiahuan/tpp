"""empty message

Revision ID: 4f07d8003003
Revises: 1b53df572482
Create Date: 2019-01-24 10:30:41.934676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f07d8003003'
down_revision = '1b53df572482'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('good_id', sa.String(length=32), nullable=True),
    sa.Column('cid', sa.Integer(), nullable=True),
    sa.Column('shop_id', sa.Integer(), nullable=True),
    sa.Column('brand_id', sa.Integer(), nullable=True),
    sa.Column('good_name', sa.String(length=255), nullable=False),
    sa.Column('show_img', sa.String(length=255), nullable=True),
    sa.Column('good_desc', sa.String(length=255), nullable=True),
    sa.Column('good_price', sa.Numeric(precision=11, scale=2), nullable=True),
    sa.Column('stocks', sa.Integer(), nullable=True),
    sa.Column('good_tips', sa.String(length=255), nullable=True),
    sa.Column('is_hot', sa.Integer(), nullable=True),
    sa.Column('is_new', sa.Integer(), nullable=True),
    sa.Column('is_recom', sa.Integer(), nullable=True),
    sa.Column('is_sale', sa.Integer(), nullable=True),
    sa.Column('good_status', sa.Integer(), nullable=True),
    sa.Column('sale_volume', sa.Integer(), nullable=True),
    sa.Column('sale_time', sa.DateTime(), nullable=True),
    sa.Column('is_delete', sa.Boolean(), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('good_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('goods')
    # ### end Alembic commands ###
