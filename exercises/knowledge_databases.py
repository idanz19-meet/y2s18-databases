from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article():
	pass

def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass

basketball = Knowledge(name="Basketball", topic="Sport", article_id=1, rating=8)
fencing = Knowledge(name="Fencing", topic="Combat", article_id=2, rating=6)
toad = Knowledge(name="Toad", topic="Amphibians", article_id=3, rating=10)