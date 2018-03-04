# -*- coding: utf-8 -*-
from flask import Flask
import json
from touristfriend.service import (
    execute_search, combine_duplicate_businesses, write_businesses)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/<distance>/<location>/<query>')
def reviews(distance, location, query):
    locations = []
    coords = location.split(",")
    try:
        location = (float(coords[0]), float(coords[1]))
        locations.append(location)
        businesses = execute_search(locations, distance, query)
        return json.dumps(
            write_businesses(combine_duplicate_businesses(businesses)))
    except Exception:
        return "[]"
