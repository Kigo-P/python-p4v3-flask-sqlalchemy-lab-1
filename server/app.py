# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    body = {'message': 'Flask SQLAlchemy Lab 1'}
    return make_response(body, 200)

# Add views here   
@app.route("/earthquakes/<int:id>",methods=["GET"])
def earthquakes(id):
    get_earthquake = Earthquake.query.filter(Earthquake.id == id).first()
    print(get_earthquake)
    if get_earthquake:
        response = {
        "id" : get_earthquake.id,
        "magnitude" : get_earthquake.magnitude,
        "location" : get_earthquake.location,
        "year": get_earthquake.year
        }
        return jsonify(response), 200   
    else:
        response = {
            "message": f"Earthquake {id} not found."
        }
        return jsonify(response), 404

@app.route("/earthquakes/magnitude/<float:magnitude>", methods=["GET"])
def get_magnitude(magnitude):
    get_all_earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    

    quake = [{
        "id" : get_all_earthquake.id,
        "magnitude" : get_all_earthquake.magnitude,
        "location" : get_all_earthquake.location,
        "year": get_all_earthquake.year
        } for get_all_earthquake in get_all_earthquakes]



    return jsonify({
        "count": len(quake),
        "quakes": quake
    }), 200 
    





if __name__ == '__main__':
    app.run(port=5555, debug=True)
