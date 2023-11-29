from flask import Flask, request,make_response,jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db, artist,image,AIA

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
CORS(app, resources={r"/*": {"origins": "*"}})

migrate = Migrate(app,db)
db.init_app(app)

"""

    DEFAULT/HOME ROUTES

"""

@app.route('/')
def index():
    return {"message": "Welcome to NeonTails!"}

@app.route('/api/message', methods=['GET'])
def view_message():
    return {"message": "NOBODY BUILDS FLASK APPLICATIONS BETTER THAN ME!"}

"""

    ARTIST ROUTES

"""

@app.route('/api/artists', methods=['GET'])
def view_all_artists():
    all_artist = artist.query.all()
    artist_data = [art.to_dict(rules=("-art",)) for art in all_artist]

    return make_response(jsonify(artist_data))


"""

    images ROUTES

"""

@app.route('/api/images', methods=['GET'])
def view_all_images():
    all_images = image.query.all()
    image_data = [img.to_dict(rules=("-image",)) for img in all_images]

    return make_response(jsonify(image_data))



"""

    Association ROUTES

"""
# @app.route('/api/<int:artist_id>/images', methods=['GET'])
# def add_new_image(artist_id:int):
#     # matching_artist = artist.query.filter(artist.id == artist_id).first()
#     # POST_REQ= request.get_json()
#     # img_id = POST_REQ["id"]
#     pass

@app.route('/api/<int:artist_id>/images', methods=['GET'])
def get_images_with_artist_id(artist_id:int):
    matching_artist = artist.query.filter(artist.id == artist_id).first()
    if not matching_artist:
        return make_response(jsonify({"error": f"Artist ID:{artist_id} not found in database"}),404)
    images_from_artist = [img.to_dict(rules=("-AIA",)) for img in matching_artist.AIA]
    return make_response(jsonify(images_from_artist),200)

"""

    EROR HANDLING

"""
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"error": "page not found"}),404)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)