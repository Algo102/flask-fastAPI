import sqlalchemy
import databases
from settings import settings

DATABASE_URL = settings.DATABASE_URL
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    'users',
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('username', sqlalchemy.String(20)),
    sqlalchemy.Column('email', sqlalchemy.String(80)),
    sqlalchemy.Column('password', sqlalchemy.String(255)),
)
# String(20) - хоть в settings ограничение уже прописано, дублируя здесь запросы обрабатываются быстрее

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# "check_same_thread": False - для синхронной поддержки обращения к базе

metadata.create_all(engine)
