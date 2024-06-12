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
    sqlalchemy.Column('firstname', sqlalchemy.String(20)),
    sqlalchemy.Column('lastname', sqlalchemy.String(20)),
    sqlalchemy.Column('birthday', sqlalchemy.Date()),
    sqlalchemy.Column('email', sqlalchemy.String(80)),
    sqlalchemy.Column('address', sqlalchemy.String(250)),
)
# String(20) - хоть в settings ограничение уже прописано, дублируя здесь запросы обрабатываются быстрее

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# "check_same_thread": False - для синхронной поддержки обращения к базе

metadata.create_all(engine)
