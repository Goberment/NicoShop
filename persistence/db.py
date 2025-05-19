from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNECTION = 'mysql+pymysql://root:dmc011505@localhost:3307/nicoshop'

SessionLocal = sessionmaker(bind =create_engine(CONNECTION, echo = True))

                            
