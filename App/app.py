from flask import Flask, request, jsonify
import psycopg2
from db_connections.connections import session

from model.table import Vehicles

app = Flask(__name__)


@app.route('/get_all_vehicles', methods=['GET'])
def get_vehicles():
    vehicles = session.query(Vehicles).all()
    vehicles_list = [
        {'id': vehicle.id, 'make': vehicle.make, 'model': vehicle.model, 'year': vehicle.year, 'color': vehicle.color} for
        vehicle in vehicles]
    return jsonify(vehicles_list)


@app.route('/add_vehicles', methods=['POST'])
def add_vehicle():
    new_vehicle_data = request.get_json()
    new_vehicle = Vehicles(
        id=new_vehicle_data['id'],
        make=new_vehicle_data['make'],
        model=new_vehicle_data['model'],
        year=new_vehicle_data['year'],
        color=new_vehicle_data['color']
    )
    session.add(new_vehicle)
    session.commit()
    return jsonify({"message": "New vehicle added successfully"})


@app.route('/update_vehicles', methods=['PUT'])
def update_vehicle():
    user_data = request.get_json()
    session.query(Vehicles).filter(Vehicles.id == user_data.get('id')).update(user_data)

    session.commit()

    return jsonify({"message": "New vehicle updated successfully"})


@app.route('/delete_vehicles', methods=['DELETE'])
def delete_vehicle():
    data = request.get_json()
    session.query(Vehicles).filter(Vehicles.id == data.get('id')).delete()
    session.commit()
    return jsonify({"message": "New vehicle deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
