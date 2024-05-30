"""add content column to post table

Revision ID: 822510a2ec86
Revises: e8f85a44d2ef
Create Date: 2024-05-09 12:54:51.930809

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '822510a2ec86'
down_revision: Union[str, None] = 'e8f85a44d2ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
