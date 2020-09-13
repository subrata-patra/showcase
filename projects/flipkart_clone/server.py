from app.main import create_app, db
from flask_sqlalchemy import SQLAlchemy
from app.main.models import *
from flask_migrate import Migrate
# --------------------

# --------------------

app = create_app()
migrate = Migrate(app, db)

# --------------------

# --------------------

if __name__=='main':
    app.run()