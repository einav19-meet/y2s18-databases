from knowledge_model import Base, Knowledge
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, article, rate):
	new_article = Knowledge(
		topic=topic,
		article=article,
		rate=rate)
	session.add(new_article)
	session.commit()


def query_all_articles():
	 articles = session.query(Knowledge).all()
	 return articles


def query_article_by_topic(topic):
	 article = session.query(Knowledge).filter_by(topic=topic).first()
	 return article

def query_article_by_rating(article,rate):
	article = session.query(Knowledge).filter_by(rate=rate).first()
	threshold = 5
	if rate < threshold:
		return article


def delete_all_articles(article):
	session.query(Knowledge).filter_by(
		article=article).delete()
	session.commit()


def edit_article_rating(article,rate):
	article_object= session.query(Knowledge).filter_by(article=article).first()
	print(article_object)
	article_object.rate = rate
	session.commit()


add_article("judo","judo with asaf", 3)
add_article("theater","melechet hahaim", 10)
#print (query_all_articles())
#print (query_article_by_topic("judo"))
print(query_article_by_topic("judo"))
#delete_all_articles("judo with asaf")
edit_article_rating("judo with asaf", 1)
query_article_by_rating("judo",2)