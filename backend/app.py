from flask import Flask, request,make_response,jsonify,session
from flask_cors import CORS
from flask_migrate import Migrate
from models import artist,image,AIA
from config import db, app
import bcrypt

# app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
# CORS(app, resources={r"/*": {"origins": "*"}})

# migrate = Migrate(app,db)
# db.init_app(app)

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

# creating/adding a painting should let you add the id of an artist to add ID the artist who "created" it
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

    AUTHENTICATION ROUTES

"""
# POST route to create new user/player within database.
@app.route("/artists", methods=["POST"])
def add_player():
    if request.method == "POST":
        payload = request.get_json()

        username = payload["username"]
        password = payload["password"]

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt=salt)

        new_artist = artist(
            username=username,
            password=hashed_password.decode("utf-8")
        )

        if new_artist is not None:
            db.session.add(new_artist)
            db.session.commit()
            session["artist_id"] = new_artist.id
            return make_response(
                new_artist.to_dict(only=("id", "username", "bio", "password")), 
                201
            )
        else:
            return make_response({"error": "Invalid username or password. Try again."}, 401)
    else:
        return make_response({"error": f"Invalid request type. (Expected POST; received {request.method}.)"}, 400)

@app.route("/artists/login", methods=["POST"])
def player_login():
    if request.method == "POST":
        payload = request.get_json()
        # look out for this line
        matching_artist = artist.query.filter(artist.username.like(f"%{payload['username']}%")).first()
        
        AUTHENTICATION_IS_SUCCESSFUL = bcrypt.checkpw(
            password=payload["password"].encode("utf-8"),
            hashed_password=matching_artist.password.encode("utf-8")
        )

        if matching_artist is not None and AUTHENTICATION_IS_SUCCESSFUL:
            session["artist_id"] = matching_artist.id
            return make_response(
                matching_artist.to_dict(only=("id", "username", "bio", "password")), 
                200
            )
        else:
            return make_response({"error": "Invalid username or password. Try again."}, 401)
    else:
        return make_response({"error": f"Invalid request type. (Expected POST; received {request.method}.)"}, 400)
    
# DELETE route to clear player credentials from server session.
@app.route("/artists/logout", methods=["DELETE"])
def player_logout():
    if request.method == "DELETE":
        session["artist_id"] = None
        return make_response({"msg": "Player successfully logged out."}, 204)
    else:
        return make_response({"error": f"Invalid request type. (Expected DELETE; received {request.method}.)"}, 400)


"""

    EROR HANDLING

"""
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"error": "page not found"}),404)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)