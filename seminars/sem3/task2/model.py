from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book(db.Model):
    # __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
    authors = db.relationship('Author', backref='books', secondary='book_author', lazy=True)
# backref='books' - (обратная ссылка) если захотим получить у автора список его книг, через таблицу BookAuthor

    def __repr__(self):
        return f'Books({self.title}, {self.year})'


class Author(db.Model):
    # __tablename__ = 'author'  # явное указание имени таблицы
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=True, nullable=False)
    lastname = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'Author({self.firstname}, {self.lastname})'


class BookAuthor(db.Model):
    # __tablename__ = 'book_author'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
# 'book.id' можно написать с большой буквы, как объект, но без ковычек
