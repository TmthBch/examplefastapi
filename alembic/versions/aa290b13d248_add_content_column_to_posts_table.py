"""add content column to posts table

Revision ID: aa290b13d248
Revises: 1b132c5d36ee
Create Date: 2023-09-02 16:37:18.663634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa290b13d248'
down_revision: Union[str, None] = '1b132c5d36ee'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
