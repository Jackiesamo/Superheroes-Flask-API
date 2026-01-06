
from flask import Flask
from flask_migrate import Migrate
from models import db
from flask import jsonify
from models import Hero
from models import Power
from flask import request


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()

    heroes_list = [
        {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        }
        for hero in heroes
    ]

    return jsonify(heroes_list), 200

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [
            {
                "id": hp.id,
                "hero_id": hp.hero_id,
                "power_id": hp.power_id,
                "strength": hp.strength,
                "power": {
                    "id": hp.power.id,
                    "name": hp.power.name,
                    "description": hp.power.description
                }
            }
            for hp in hero.hero_powers
        ]
    }

    return jsonify(hero_data), 200

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()

    powers_list = [
        {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        for power in powers
    ]

    return jsonify(powers_list), 200

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }

    return jsonify(power_data), 200

@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.get_json()

    description = data.get("description", "").strip()

    # Validation
    errors = []
    if not description:
        errors.append("Description is required")
    elif len(description) < 20:
        errors.append("Description must be at least 20 characters long")

    if errors:
        return jsonify({"errors": errors}), 400

    # Update and save
    power.description = description
    db.session.commit()

    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }

    return jsonify(power_data), 200





if __name__ == '__main__':
    app.run(port=5555, debug=True)
