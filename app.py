
from flask import Flask
from flask_migrate import Migrate
from models import db
from flask import jsonify
from models import Hero
from models import Power
from flask import request
from models import HeroPower 


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

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()

    hero_id = data.get("hero_id")
    power_id = data.get("power_id")
    strength = data.get("strength", "").strip()

    errors = []

    # Check hero exists
    hero = Hero.query.get(hero_id)
    if not hero:
        errors.append("Hero does not exist")

    # Check power exists
    power = Power.query.get(power_id)
    if not power:
        errors.append("Power does not exist")

    # Check strength
    if strength not in ["Strong", "Weak", "Average"]:
        errors.append("Strength must be 'Strong', 'Weak', or 'Average'")

    if errors:
        return jsonify({"errors": errors}), 400

    # Create HeroPower
    hero_power = HeroPower(hero_id=hero_id, power_id=power_id, strength=strength)
    db.session.add(hero_power)
    db.session.commit()

    response_data = {
        "id": hero_power.id,
        "hero_id": hero_power.hero_id,
        "power_id": hero_power.power_id,
        "strength": hero_power.strength,
        "hero": {
            "id": hero.id,
            "name": hero.name,
            "super_name": hero.super_name
        },
        "power": {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
    }

    return jsonify(response_data), 201





if __name__ == '__main__':
    app.run(port=5555, debug=True)
