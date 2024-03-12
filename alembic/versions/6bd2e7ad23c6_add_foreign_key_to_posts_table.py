"""add foreign key to posts table

Revision ID: 6bd2e7ad23c6
Revises: 181f5b95704b
Create Date: 2024-03-11 20:12:33.912839

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6bd2e7ad23c6"
down_revision: Union[str, None] = "181f5b95704b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key(
        "fk_posts_users",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )
    pass


def downgrade() -> None:
    op.drop_constraint('fk_post_users', table_name='posts')
    op.drop_column('posts', 'owner_id')
    
    pass
