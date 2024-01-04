"""add_relationship_user_blog

Revision ID: cd7165b30e58
Revises: 06a57395b702
Create Date: 2024-01-03 20:31:05.473938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd7165b30e58'
down_revision: Union[str, None] = '06a57395b702'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('creator_id', sa.Integer(), nullable=False))
    op.create_foreign_key('fk_user_blog', 'blogs', 'users', ['creator_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("fk_user_blog", 'blogs', type_='foreignkey')
    op.drop_column('blogs', 'creator_id')
    # ### end Alembic commands ###
