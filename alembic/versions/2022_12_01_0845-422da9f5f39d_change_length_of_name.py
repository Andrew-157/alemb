"""change length of name

Revision ID: 422da9f5f39d
Revises: e13f29500630
Create Date: 2022-12-01 08:45:29.065930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '422da9f5f39d'
down_revision = 'e13f29500630'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('contacts', 'name',
                    existing_type=sa.VARCHAR(length=12),
                    type_=sa.String(length=15),
                    existing_nullable=False)


def downgrade() -> None:
    op.alter_column('contacts', 'name',
                    existing_type=sa.String(length=15),
                    type_=sa.VARCHAR(length=12),
                    existing_nullable=False)
