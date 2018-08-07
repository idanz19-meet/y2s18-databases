from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

"""
Functions
"""

def add_article(name, topic, rating):
	wikipedia_obj = Knowledge(
		name = name,
		topic = topic,
		rating = rating)
	session.add(wikipedia_obj)
	session.commit()
	
def query_all_articles():
	knowledge = session.query(Knowledge).all()
	return knowledge

def query_article_by_topic(x):
	articles = session.query(Knowledge).filter_by(topic = x).all()
	return articles

def query_article_by_rating(x):
	articles = session.query(Knowledge).filter(Knowledge.rating <= x).all()
	return articles

def query_article_by_primary_key(x):
	article = session.query(Knowledge).filter_by(article_id = x)
	return article

def delete_article_by_topic(x):
	session.query(Knowledge).filter_by(topic = x).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating(article_name, new_rating):
	x = session.query(Knowledge).filter_by(name = article_name).first()
	x.rating = new_rating
	session.commit()

def remove_article_by_rating(x):
	session.query(Knowledge).filter(Knowledge.rating < x).delete()
	session.commit()

"""
Articles
"""

add_article("Basketball", "Sport", 8)
add_article("Toad", "Amphibians", 10)
add_article("Fencing", "Sport", 7)
add_article("Philosophy","Existence",8)
add_article("Frog", "Amphibians", 5)
add_article("King Louis XIV", "Monarchs", 4)
add_article("Detroit", "Cities", 9)

"""
TESTING
"""

# delete_all_articles()
# delete_article_by_topic("Amphibians")
# print(query_article_by_topic("Sport")
# edit_article_rating("King Louis XIV", 5)
# remove_article_by_rating(6)

print(query_article_by_rating(7))
