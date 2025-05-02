from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()
    if not Game.query.first():
        game1 = Game(title="Zelda", genre="Adventure", platform="Switch")
        game2 = Game(title="Borderlands", genre="Action", platform="PS5")
        game3 = Game(title="Minecraft", genre="Sandbox", platform="Cross platform")
        game4 = Game(title="Halo", genre="Shooter", platform="Xbox")
        db.session.add_all([game1, game2, game3, game4])
        db.session.commit()

@app.route('/')
def index():
    games = Game.query.all()
    return render_template('index.html', games=games)

@app.route('/game/<int:game_id>')
def game_detail(game_id):
    game = Game.query.get_or_404(game_id)
    return render_template('detail.html', game=game)

if __name__ == '__main__':
    app.run(debug=True)
