from . import db

from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create a base class for our models
Base = declarative_base()

# Define the Expressions model
class Expressions(Base):
    __tablename__ = 'expressions'
    __table_args__ = {'schema': 'british_expressions'}  # Specify the schema name

    id_exp = Column(Integer, primary_key=True, autoincrement=True)
    expression = Column(String(200), nullable=False)
    meaning = Column(Text, nullable=True)
    uses_example = Column(String(50), nullable=True)
    context = Column(Text, nullable=True)

    # Relationship to tags via a secondary table
    tags = relationship("Tag", secondary='tags_expressions', back_populates="expressions")

    # Ensure unique constraint on the id_exp field
    __table_args__ = (
        UniqueConstraint('id_exp', name='id_exp_UNIQUE'),
    )

# Define the Tag model
class Tag(Base):
    __tablename__ = 'tags'
    __table_args__ = {'schema': 'british_expressions'}  # Specify the schema name

    id_tag = Column(Integer, primary_key=True, autoincrement=True)
    tag = Column(String(45), nullable=False)

    # Relationship to expressions via a secondary table
    expressions = relationship("Expressions", secondary='tags_expressions', back_populates="tags")

# Define the TagsExpressions association table
class TagsExpressions(Base):
    __tablename__ = 'tags_expressions'
    __table_args__ = {'schema': 'british_expressions'}  # Specify the schema name

    id_tags_expressions = Column(Integer, primary_key=True, autoincrement=True)
    expressions_id_exp = Column(Integer, ForeignKey('british_expressions.expressions.id_exp'), nullable=False)
    tags_id_tag = Column(Integer, ForeignKey('british_expressions.tags.id_tag'), nullable=False)

    # Optionally define back_populates here if needed

# Create an engine and a session
engine = create_engine('mysql+pymysql://username:password@localhost/british_expressions')
Session = sessionmaker(bind=engine)
session = Session()

# Create all tables in the database
Base.metadata.create_all(engine)



# class User(db.Model):
#     __tablename__ = 'User'

#     user_id = Column(Integer, primary_key=True, autoincrement=True)
#     first_name = Column(String(255), nullable=False)
#     last_name = Column(String(255), nullable=False)
#     country = Column(String(255))
#     email = Column(String(255), unique=True, nullable=False)
#     role_id = Column(Integer, ForeignKey('UserRole.role_id'))

#     role = relationship("UserRole")



# class UserRole(db.Model):
#     __tablename__ = 'UserRole'

#     role_id = Column(Integer, primary_key=True, autoincrement=True)
#     role_name = Column(String(255), nullable=False)