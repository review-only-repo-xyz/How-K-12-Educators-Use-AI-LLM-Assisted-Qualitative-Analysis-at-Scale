import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine
from sqlalchemy.exc import SQLAlchemyError
from typing import Any

def connect_psql() -> Engine:
    load_dotenv()  # Load environment variables from .env
    db_password = os.getenv("PSQL_PASSWORD")
    
    if not db_password:
        raise EnvironmentError("PSQL_PASSWORD environment variable is not set.")

    try:
        # Define database URL
        database_url = f"postgresql+psycopg2://postgres:{db_password}@colleague-pg.cqc6tglrugqj.us-east-1.rds.amazonaws.com/postgres"

        # Ensure the function only returns a single engine object
        engine = create_engine(
            database_url,
            pool_size=5,  
            max_overflow=10,  
            pool_timeout=30,  
            pool_recycle=1800,  
            echo=False  
        )

        return engine

    except SQLAlchemyError as e:
        print(f"Failed to create database engine: {str(e)}")
        raise