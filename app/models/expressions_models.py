from . import db


# from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
# from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()


class Tags(db.Model):
    __tablename__ = 'Category'

    tag_id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String(255), nullable=False)


class User(db.Model):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    country = Column(String(255))
    email = Column(String(255), unique=True, nullable=False)
    role_id = Column(Integer, ForeignKey('UserRole.role_id'))

    role = relationship("UserRole")


class Expressions(db.Model):
    __tablename__ = 'Words'

    expression_id = Column(Integer, primary_key=True, autoincrement=True)
    expression = Column(String(255), nullable=False)
    meaning = Column(Text)
    tag_id = Column(Integer, ForeignKey('Tags.tag_id'))
    usage_examples = Column(Text)

    category = relationship("Tags")


class Content(db.Model):
    __tablename__ = 'Content'

    content_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'))
    word_id = Column(Integer, ForeignKey('Words.word_id'))
    created_at = Column(TIMESTAMP, nullable=False, server_default="CURRENT_TIMESTAMP")

    user = relationship("User")
    word = relationship("Words")


#tag_expression

# class UserRole(db.Model):
#     __tablename__ = 'UserRole'

#     role_id = Column(Integer, primary_key=True, autoincrement=True)
#     role_name = Column(String(255), nullable=False)