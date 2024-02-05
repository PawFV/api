from db.models import Base
from sqlalchemy import create_engine
import os, dotenv
dotenv.load_dotenv()
engine = create_engine(os.environ.get('DB_CONNECTION_STRING'))
Base.metadata.create_all(engine)