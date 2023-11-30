from flask import Flask, request,make_response,jsonify,session
from flask_cors import CORS
from flask_migrate import Migrate
from models import artist,image,AIA
from config import db, app
import bcrypt




"""

    DEFAULT/HOME ROUTES

"""
# default route
@app.route('/')
def index():
    return {"message": "Welcome to NeonTails!"}


# testing auth
@app.route('/api/message', methods=['GET'])
def view_message():
    authorization = authorize_user()
    if authorization.status_code == 401:
        return make_response({"error": "access denied"},401)
    else:
        return make_response({"message": "NOBODY BUILDS FLASK APPLICATIONS BETTER THAN ME!", "user": authorization.get_json()},200)

"""

    ARTIST ROUTES

"""

# gets all artists
@app.route('/api/artists', methods=['GET'])
def view_all_artists():
    all_artist = artist.query.all()
    artist_data = [art.to_dict(rules=("-art",)) for art in all_artist]

    return make_response(jsonify(artist_data))

# get a single artist using the ID 
@app.route('/api/artists/<int:artist_id>', methods =['GET'])
def view_artist_withID(artist_id:int):
    matching_artist = artist.query.filter(artist.id == artist_id).first()
    if not matching_artist:
        return make_response(jsonify({"error": f"artist_ID:{artist_id} not found"}))
    return make_response(jsonify(matching_artist.to_dict()),200)


"""

    images ROUTES

"""
# get all images
@app.route('/api/images', methods=['GET'])
def view_all_images():
    all_images = image.query.all()
    image_data = [img.to_dict(rules=("-image",)) for img in all_images]

    return make_response(jsonify(image_data))

# get a single image using the ID
@app.route('/api/<int:image_id>')
def view_img_withID(image_id:int):
    matching_image = image.query.filter(image.id == image_id).first()
    if not matching_image:
        return make_response(jsonify({"error": f"image_id: {image_id} not found"}))
    return make_response(jsonify(matching_image.to_dict()),200)

# have 3 random numbers between how many images there 
@app.route('/api/featuredimages', methods=['GET'])
def view_three_images():
    pass

"""

    Association ROUTES

"""

# creating/adding a painting should let you add the id of an artist to add ID the artist who "created" it
@app.route('/api/<int:artist_id>/AIA', methods=['POST'])
def add_new_image(artist_id:int):
    authorization = authorize_user()
    if authorization.status_code == 401:
        return make_response({"error": "access denied"},401)
    else:
        matching_artist = artist.query.filter(artist.id == artist_id).first()
        POST_REQ= request.get_json()
        # might change to add an image directly
        img_id = POST_REQ["img_id"]
        matching_art = image.query.filter(image.id == img_id).first()
        #####
        if not matching_art:
            return make_response(jsonify({"error": f"art ID: {img_id} not found"}))
        if not matching_artist:
            return make_response(jsonify({"error": f"artist ID: {artist_id} not found"}))
        new_AIA = AIA(
            artist_id = matching_artist,
            image_id = matching_art
        )

        db.session.add(new_AIA)
        db.session.commit()
        return make_response(jsonify(new_AIA.to_dict(rules=("-artist"))),201)


# gets all the images associated to an artist
@app.route('/api/<int:artist_id>/images', methods=['GET'])
def get_images_with_artist_id(artist_id:int):
    matching_artist = artist.query.filter(artist.id == artist_id).first()
    if not matching_artist:
        return make_response(jsonify({"error": f"Artist ID:{artist_id} not found in database"}),404)
    images_from_artist = [img.to_dict(rules=("-AIA",)) for img in matching_artist.AIA]
    return make_response(jsonify(images_from_artist),200)




# route to return 1 image and its artist
@app.route('/api/images/<int:image_id>/artist',methods =['GET'])
def get_artists_with_image_id(image_id:int):
    matching_image = image.query.filter(image.id == image_id).first()
    
    if not matching_image:
        return make_response(jsonify({"error": f"image ID:{image_id} not found in database"}))
    artist_from_images = [art.to_dict(rules = ("-AIA",))for art in matching_image.AIA]
    # artist_from_images = [matching_image.to_dict(rules=("-AIA",))]
    return make_response(jsonify(artist_from_images),200)


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

# post route to sigin and create a seccison for a user
@app.route("/artist/signin", methods=["POST"])
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
@app.route("/artist/logout", methods=["DELETE"])
def player_logout():
    if request.method == "DELETE":
        session["artist_id"] = None
        return make_response({"msg": "Player successfully logged out."}, 204)
    else:
        return make_response({"error": f"Invalid request type. (Expected DELETE; received {request.method}.)"}, 400)

@app.route("/auth")
def authorize_user():
    user_id = session.get("artist_id")
    if not user_id:
        return make_response({"error": "User account not authenticated. Please log in or sign up to continue using the application."}, 401)
    else:
        matching_user = artist.query.filter(artist.id == user_id).first()
        if matching_user is not None:
            return(make_response(matching_user.to_dict(only=("id", "username", "bio", "password")),200))
        else:
            return make_response({"error": "Invalid username try again"},401)

"""

    ERROR HANDLING

"""
@app.errorhandler(404)
def page_not_found(error):
    return make_response(jsonify({"error": "page not found"}),404)




if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)