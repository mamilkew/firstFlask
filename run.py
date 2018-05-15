from bookshelf import app
from bookshelf.data.model import db


if __name__ == '__main__':
    app.run()



db.init_app(app)