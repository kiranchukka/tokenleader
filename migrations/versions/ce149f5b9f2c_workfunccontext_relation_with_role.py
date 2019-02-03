"""workfuncContext relation with role

Revision ID: ce149f5b9f2c
Revises: 
Create Date: 2019-01-31 19:58:50.555698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce149f5b9f2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rolename', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_role_rolename'), ['rolename'], unique=True)

    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=True)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('roles_n_user_map',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('role_id', 'user_id')
    )
    op.create_table('workfunctioncontext',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('roleid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['roleid'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('workfunctioncontext', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_workfunctioncontext_name'), ['name'], unique=True)

    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('work_func_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['work_func_id'], ['workfunctioncontext.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('department', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_department_name'), ['name'], unique=True)

    op.create_table('org_unit',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('work_func_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['work_func_id'], ['workfunctioncontext.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('org_unit', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_org_unit_name'), ['name'], unique=True)

    op.create_table('organization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('orgtype', sa.String(length=64), nullable=True),
    sa.Column('auth_backend', sa.String(length=64), nullable=True),
    sa.Column('work_func_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['work_func_id'], ['workfunctioncontext.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('organization', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_organization_name'), ['name'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('organization', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_organization_name'))

    op.drop_table('organization')
    with op.batch_alter_table('org_unit', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_org_unit_name'))

    op.drop_table('org_unit')
    with op.batch_alter_table('department', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_department_name'))

    op.drop_table('department')
    with op.batch_alter_table('workfunctioncontext', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_workfunctioncontext_name'))

    op.drop_table('workfunctioncontext')
    op.drop_table('roles_n_user_map')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    with op.batch_alter_table('role', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_role_rolename'))

    op.drop_table('role')
    # ### end Alembic commands ###