from flask import Flask, jsonify, render_template, request
import requests, json
import zipcode
from pprint import pprint
app = Flask(__name__)

rec_center_info = False

# Index page route
@app.route("/")
def hello():
	return render_template("index.html")

# About page
@app.route("/about")
def about():
	return render_template("about.html")

# Resources route
@app.route("/resources")
def resources():
	return render_template("resources.html")

# Emotional Support route
@app.route("/emotionalsupport")
def emotionalsupport():
	return render_template("emotionalsupport.html")

# Search page (returns nearest rec center)
@app.route('/find', methods=["GET","POST"])
def find():
	if request.method == "POST":
		the_results = find_nearest_center(request.form["user_zipcode"])
		return render_template("results.html",rec_center_results=the_results)
	else: # request.method == "GET"
		return render_template("find.html")

# List of all rec centers
@app.route("/centers")
def centers():
	rec_center_info = get_rec_center_info()
	return render_template("rec_centers.html", info=rec_center_info)

# 404 Page
@app.errorhandler(404)
def page_not_found(error):
	rec_center_info = get_rec_center_info()
	return render_template('404.html', info=rec_center_info), 404

# Helper that finds the nearest rec center to a zipcode
def find_nearest_center(user_zipcode):
	rec_centers = get_rec_center_info()
	partial_zip = str(user_zipcode)[0:4]

	nearby_rec_centers = []

	# Go through each center, and if their
	# zip code begins with the first 4 digits
	# of the user's zipcode, add it to the nearby list
	for center in rec_centers:
		center_zipcode = str(center.get('ZIP'))
		if center_zipcode is not None:
			if center_zipcode.startswith(partial_zip):
				nearby_rec_centers.append(center.copy())

	return nearby_rec_centers

# Loads the rec center JSON data
def get_rec_center_info():
	global rec_center_info
	if not rec_center_info:
		with open('data/recreation.json') as f:
			rec_center_info = json.loads(f.read())
	return rec_center_info

if __name__ == "__main__":
	app.run(debug = True, port = 4000)
