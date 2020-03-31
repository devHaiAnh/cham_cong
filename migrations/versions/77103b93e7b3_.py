"""empty message

Revision ID: 77103b93e7b3
Revises: 
Create Date: 2020-03-31 10:07:22.157395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77103b93e7b3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Employees',
    sa.Column('employeeId', sa.Integer(), nullable=False),
    sa.Column('ho', sa.String(), nullable=True),
    sa.Column('ten', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('employeeId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Employees')
    # ### end Alembic commands ###