"""empty message

Revision ID: 114c17e2291d
Revises: 43614fe53832
Create Date: 2024-11-06 21:01:53.942619

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '114c17e2291d'
down_revision = '43614fe53832'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('goal', schema=None) as batch_op:
        batch_op.drop_column('title')

    # ### end Alembic commands ###
