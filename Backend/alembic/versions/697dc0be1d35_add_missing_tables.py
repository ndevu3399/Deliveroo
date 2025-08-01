"""Add missing tables

Revision ID: 697dc0be1d35
Revises: 
Create Date: 2025-07-25 17:44:07.425475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '697dc0be1d35'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('weight_categories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('min_weight', sa.Float(), nullable=False),
    sa.Column('max_weight', sa.Float(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('label', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parcels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pickup_address', sa.String(), nullable=False),
    sa.Column('pickup_lat', sa.Float(), nullable=False),
    sa.Column('pickup_lng', sa.Float(), nullable=False),
    sa.Column('destination_address', sa.String(), nullable=False),
    sa.Column('destination_lat', sa.Float(), nullable=False),
    sa.Column('destination_lng', sa.Float(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('recipient_name', sa.String(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('weight_category_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['weight_category_id'], ['weight_categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parcel_status_histories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('parcel_id', sa.Integer(), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['admin_id'], ['admins.id'], ),
    sa.ForeignKeyConstraint(['parcel_id'], ['parcels.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parcel_status_histories')
    op.drop_table('parcels')
    op.drop_table('weight_categories')
    op.drop_table('users')
    op.drop_table('admins')
    # ### end Alembic commands ###
