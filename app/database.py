from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker


url_object = URL.create(
    "postgresql",
    username="tudiman555",
    password="tushar123",  # plain (unescaped) text
    host="localhost",
    database="fastapi_tutorial",
    port=5432
)

engine = create_engine(url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


