"""empty message

Revision ID: 226347ec4bb2
Revises: c832f9900cad
Create Date: 2020-04-21 10:58:39.040646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '226347ec4bb2'
down_revision = 'c832f9900cad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pod',
    sa.Column('pod_name', sa.String(length=64), nullable=False),
    sa.Column('pod_namespace', sa.String(length=32), nullable=True),
    sa.Column('pod_ip', sa.String(length=32), nullable=True),
    sa.Column('pod_image', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('pod_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pod')
    # ### end Alembic commands ###