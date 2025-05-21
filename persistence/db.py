from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION = 'mysql+pymysql://root:Guaymas@localhost:3306/nicoshop'

SessionLocal = sessionmaker(bind =create_engine(CONNECTION, echo = False))

                            
