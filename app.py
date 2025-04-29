from flask import Flask, render_template, request, redirect, url_for
from models import db, Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    items = Item.query.all()  # Fetch all items from the database
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    item_name = request.form['name']
    new_item = Item(name=item_name)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)