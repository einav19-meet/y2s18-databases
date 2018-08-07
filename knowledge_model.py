from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):

	__tablename__= "knowledge"
	knowledge_id = Column(Integer, primary_key=True)
	topic = Column(String)
	article = Column(String)
	rate = Column(Integer)

	def __repr__(self):
		return ("Knowledge ID: {}\n"
				"Article Topic: {}\n"
				"Article Name: {}\n"
				"Article Rate: {}\n" ).format(self.knowledge_id, self.topic, self.article,self.rate)

x=Knowledge(knowledge_id=1, topic= "theater", article= "Theater | art", rate=10)

print (x)