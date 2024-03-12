"""add content column to post table

Revision ID: 1680e0ec00f6
Revises: 906342f1400b
Create Date: 2024-03-11 17:49:54.965946

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1680e0ec00f6'
down_revision: Union[str, None] = '906342f1400b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
