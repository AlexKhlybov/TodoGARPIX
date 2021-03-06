"""empty message

Revision ID: 0123ecc67dcf
Revises: 
Create Date: 2021-07-07 22:31:15.951604

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0123ecc67dcf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=150), nullable=True),
        sa.Column("content", sa.String(), nullable=True),
        sa.Column("create_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("tasks")
    # ### end Alembic commands ###
