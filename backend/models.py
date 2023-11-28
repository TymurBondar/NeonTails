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
    name = db.Cloumn(db.String, unique = True, nullable = False)
    bio = db.Column(db.String, unique = False, nullable = False)

    AIA = db.relationship("AIA", back_populates = "artist")

    image = association_proxy("AIA", "image")

    serialize_rules = ("-AIA.artist")

# image class for db
class image(db.Model, SerializerMixin):
    __tablename__ = "Images"
    # Columns for the table nothing should be null
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String , unique = True, nullable = False)
    link = db.Column(db.String, unique = True, nullable = True)

    AIA = db.relationship("AIA", back_populates = "image")

    artist = association_proxy("AIA", "artist")

    serialize_rules = ("-AIA.image")


class AIA(db.Model, SerializerMixin):
    __tablename__ = "AIA"

    # Columns for the AIA table nothing should be blank and it should take ID's from other 2 classes
    id = db.Column(db.Integer, primary_key = True)
    artist_id = db.Column(db.integer, db.ForeignKey("Artists.id"))
    image_id = db.Column(db.integer, db.ForeignKey("Images.id"))

    artist = db.relationship("artist", back_populates = "AIA")
    
    image = db.relationship("image", back_populates = "AIA")

    serialize_rules  = ("-artist.AIA", "-image.AIA")
