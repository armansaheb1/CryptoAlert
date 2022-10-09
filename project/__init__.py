from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    socketio = SocketIO(app)
    db.init_app(app)
    
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect('/login')
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    import logging
    logging.basicConfig(filename='error.log',level=logging.DEBUG)
    
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .chat import chat as chat_blueprint
    app.register_blueprint(chat_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    socketio.init_app(app)
    
    if __name__ == "__main__":
        app.run(host='176.9.185.90',port=5000)

    return app
app = create_app()