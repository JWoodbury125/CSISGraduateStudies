from flask import Flask, jsonify
import sys
import json
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Family Game Night Player's Page"

@app.route('/players')
def all_players():
	file = open("players.json").read()
	player_data= json.loads(file)
	return jsonify(results = player_data)

@app.route('/players/<id>')
def player(id):
	file = open("players.json").read()
	player_data= json.loads(file)

 	try:
		return jsonify(player_data["players"][int(id)])
 	except:
		return "Please enter a valid Player"

if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0')
