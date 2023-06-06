"""Add Review Model

Revision ID: 829eabc6e900
Revises: 8b1947b4102b
Create Date: 2023-06-06 12:02:06.566903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '829eabc6e900'
down_revision = '8b1947b4102b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_reviews_game_id_games')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###