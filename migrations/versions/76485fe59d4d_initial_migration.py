"""Initial Migration

Revision ID: 76485fe59d4d
Revises: 
Create Date: 2021-04-25 21:44:54.935612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76485fe59d4d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=225), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.Column('pass_hash', sa.String(length=255), nullable=True),
    sa.Column('profile_pic', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('pitches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nametype', sa.String(length=255), nullable=True),
    sa.Column('pitch_info', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pitches')
    op.drop_table('users')
    # ### end Alembic commands ###