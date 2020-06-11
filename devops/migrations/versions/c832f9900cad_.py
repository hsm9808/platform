"""empty message

Revision ID: c832f9900cad
Revises: 61fc00492004
Create Date: 2020-04-15 20:50:18.230542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c832f9900cad'
down_revision = '61fc00492004'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ain',
    sa.Column('monitor_time', sa.String(length=32), nullable=False),
    sa.Column('InternetInRate', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('monitor_time')
    )
    op.create_table('aout',
    sa.Column('monitor_time', sa.String(length=32), nullable=False),
    sa.Column('InternetOutRate', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('monitor_time')
    )
    op.create_table('bin',
    sa.Column('monitor_time', sa.String(length=32), nullable=False),
    sa.Column('IntranetInRate', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('monitor_time')
    )
    op.create_table('bout',
    sa.Column('monitor_time', sa.String(length=32), nullable=False),
    sa.Column('IntranetOutRate', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('monitor_time')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bout')
    op.drop_table('bin')
    op.drop_table('aout')
    op.drop_table('ain')
    # ### end Alembic commands ###
