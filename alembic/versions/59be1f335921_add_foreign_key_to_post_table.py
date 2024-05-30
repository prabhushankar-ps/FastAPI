"""add foreign key to post table

Revision ID: 59be1f335921
Revises: 255c5f1ccaa2
Create Date: 2024-05-09 15:58:35.184263

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '59be1f335921'
down_revision: Union[str, None] = '255c5f1ccaa2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table = "posts", referent_table= "users", 
                          local_cols=['owner_id'], remote_cols = ['id'], ondelete="CASCADE")

    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
