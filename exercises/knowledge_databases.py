from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

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
	knowledge = session.query(Knowledge).filter_by(topic = x).all()
	return knowledge

def delete_article_by_topic(x):
	session.query(Knowledge).filter_by(topic = x).delete()
	session.commit()

def delete_all_articles():
	session.query(Knowledge).delete()
	session.commit()

def edit_article_rating():
	pass

add_article("Basketball", "Sport", 8)
add_article("Toad", "Amphibians", 10)
add_article("Fencing", "Sport", 7)
add_article("Philosophy","Existence",8)
add_article("Frog", "Amphibians", 9)
add_article("King Louis XIV", "Monarchs", 4)

"""
TESTING
"""

delete_all_articles()
# delete_article_by_topic("Amphibians")
# print(query_article_by_topic("Sport")
print(query_all_articles())
# print(toad)