"""Initial migration

Revision ID: f66ad20d491b
Revises: 
Create Date: 2024-08-22 21:16:47.734972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f66ad20d491b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cattle_disease',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cattle_id', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('breed', sa.String(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('symptoms', sa.String(), nullable=False),
    sa.Column('diagnosis', sa.String(), nullable=False),
    sa.Column('treatment', sa.String(), nullable=False),
    sa.Column('date_of_entry', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cattle_disease')
    # ### end Alembic commands ###