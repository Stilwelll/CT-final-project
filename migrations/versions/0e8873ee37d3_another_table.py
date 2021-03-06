"""another table

Revision ID: 0e8873ee37d3
Revises: 2d1e04c03aa5
Create Date: 2022-05-01 16:23:21.388875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e8873ee37d3'
down_revision = '2d1e04c03aa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vacation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plan_name', sa.String(length=50), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('guests', sa.Integer(), nullable=False),
    sa.Column('date_leaving', sa.Date(), nullable=False),
    sa.Column('date_returning', sa.Date(), nullable=False),
    sa.Column('budget', sa.Float(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacation')
    # ### end Alembic commands ###
