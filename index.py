from flask import Flask, request, jsonify
app = Flask(__name__)

from warranteasepy import Warranty


@app.route("/create", methods=['POST'])
def create():
  json = request.get_json()
  return jsonify(Warranty.create(**json).to_json())


@app.route("/list", methods=['POST'])
def list():
  json = request.get_json()
  items = Warranty.list(**json)
  items = sorted(items, key=lambda x: -x.date_of_purchase)
  return jsonify([_.to_json() for _ in items])


@app.route("/change_nick", methods=['POST'])
def change_nick():
  json = request.get_json()
  return jsonify(Warranty.change_nick(**json).to_json())


@app.route("/add_remark", methods=['POST'])
def add_remark():
  json = request.get_json()
  return jsonify(Warranty.add_remark(**json).to_json())


@app.route("/transfer", methods=['POST'])
def transfer():
  json = request.get_json()
  return jsonify(Warranty.transfer(**json).to_json())


@app.route("/validate", methods=['POST'])
def validate():
  json = request.get_json()
  return jsonify(Warranty.validate(**json).to_json())


@app.route("/invalidate", methods=['POST'])
def invalidate():
  json = request.get_json()
  return jsonify(Warranty.invalidate(**json).to_json())


@app.route("/extend", methods=['POST'])
def extend():
  json = request.get_json()
  return jsonify(Warranty.extend(**json).to_json())
