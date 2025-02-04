"""Finance model

Revision ID: 9381d8159985
Revises: fd1846a04a23
Create Date: 2024-12-09 14:23:09.357386

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "9381d8159985"
down_revision: Union[str, None] = "fd1846a04a23"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("finances", "amount")
    op.drop_column("finances", "year")
    op.drop_column("finances", "month")
    op.drop_column("finances", "hours")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "finances", sa.Column("hours", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "finances", sa.Column("month", sa.VARCHAR(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "finances", sa.Column("year", sa.INTEGER(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "finances",
        sa.Column("amount", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    # ### end Alembic commands ###
