"""image table

Revision ID: 4001fe2138ac
Revises: 
Create Date: 2019-10-02 20:47:36.009124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4001fe2138ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(length=64), nullable=True),
    sa.Column('file_path', sa.String(length=96), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_image_file_name'), 'image', ['file_name'], unique=True)
    op.create_index(op.f('ix_image_file_path'), 'image', ['file_path'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_image_file_path'), table_name='image')
    op.drop_index(op.f('ix_image_file_name'), table_name='image')
    op.drop_table('image')
    # ### end Alembic commands ###
