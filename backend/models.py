from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# re initialize using update metadata
db = SQLAlchemy(metadata=metadata)


# artist class for db
class artist(db.Model, SerializerMixin):
    __tablename__ = "Artists"

    # Columns for the table nothing here should be null
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    bio = db.Column(db.String, unique = False, nullable = False)
    # password = db.Column(db.string, nullable = False)

    # Created relationship that links an artist to a AIA column 
    # NOTE: this needs to be closed back to the artist-AIA relationship
    AIA = db.relationship("AIA", back_populates = "artist")

    # creates an association proxy from the Artist-AIA relationship to the image-AIA 
    image = association_proxy("AIA", "image")

    # Creates serialization rules to avoid cascading when accessing artist data from the AIA
    serialize_rules = ("-AIA.artist",)

# image class for db
class image(db.Model, SerializerMixin):
    __tablename__ = "Images"
    # Columns for the table nothing should be null
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String , unique = True, nullable = False)
    link = db.Column(db.String, unique = True, nullable = True)

    # Created relationship that links an artist to an AIA column
    # NOTE: this needs to be closed back to the image-AIA relationship
    AIA = db.relationship("AIA", back_populates = "image")

    # creates an association proxy form the image-AIA relationship to the artist-AIA
    artist = association_proxy("AIA", "artist")

    # creates serialization rules to avoid cascading when accessing image data from the AIA
    serialize_rules = ("-AIA.img",)


class AIA(db.Model, SerializerMixin):
    __tablename__ = "AIA"

    # Columns for the AIA table nothing should be blank and it should take ID's from other 2 classes
    id = db.Column(db.Integer, primary_key = True)
    artist_id = db.Column(db.Integer, db.ForeignKey("Artists.id"))
    image_id = db.Column(db.Integer, db.ForeignKey("Images.id"))


    # Extended relationship to link from AIA row to Artist row
    # NOTE: needs to be closed from the artist-AIA relationship
    artist = db.relationship("artist", back_populates = "AIA")
    
    # Extended relationship to link from the AIA row to Image row
    # NOTE: needs to be closed from the image-AIA relationship
    image = db.relationship("image", back_populates = "AIA")

    # Creates rules to avoid cascading when accessing AIA data from artist or image
    serialize_rules  = ("-artist.AIA", "-image.AIA")
