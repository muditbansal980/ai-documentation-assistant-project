import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv()) 
DATABASE_URL = os.getenv("DATABASE_URL")

# Pass the string representation of your variable name

engine = create_async_engine(DATABASE_URL,echo=True)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)