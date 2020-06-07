from flask import Blueprint, render_template, jsonify

from twitter.model.trend_visualizer import graph_labels_by_woeid
from twitter.util.location_util import woeid_to_location_map, location_models

home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='templates/static')


@home.route("/")
def show_home():
    locations = woeid_to_location_map()
    locations_by_parent = location_models()
    # expensive call (do not uncomment)
    # trends = twitter_trends.trends_by_location(locations.keys())

    # trends = twitter_trends.trends_by_location() # world wide call
    # webpage = trends_to_string_util(trends)
    return render_template("home.html", map=locations, locations_by_parent=locations_by_parent)


@home.route("/json/<location>")
def raw_chart(location):
    topics, volumes, title = graph_labels_by_woeid(location)
    return jsonify(title=title, volumes=volumes, topics=topics)