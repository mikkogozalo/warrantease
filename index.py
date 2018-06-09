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
  return jsonify([_.to_json() for _ in Warranty.list(**json)])


@app.route("/change_nick", methods=['POST'])
def list():
  json = request.get_json()
  return jsonify([_.to_json() for _ in Warranty.change_nick(**json)])


@app.route("/add_remark", methods=['POST'])
def list():
  json = request.get_json()
  return jsonify([_.to_json() for _ in Warranty.add_remark(**json)])


@app.route("/transfer", methods=['POST'])
def list():
  json = request.get_json()
  return jsonify([_.to_json() for _ in Warranty.transfer(**json)])


@app.route("/validate", methods=['POST'])
def list():
  json = request.get_json()
  return jsonify([_.to_json() for _ in Warranty.validate(**json)])


@app.route("/invalidate", methods=['POST'])
def list():
  json = request.get_json()
  return jsonify([_.to_json() for _ in Warranty.invalidate(**json)])


@app.route("/extend", methods=['POST'])
def list():
  json = request.get_json()
  return jsonify([_.to_json() for _ in Warranty.extend(**json)])
