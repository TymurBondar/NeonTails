from models import artist,image,AIA
from config import db, app
from random import choice
import bcrypt

# created sample artist currently with no authentication just to seed the tables
def create_sample_artist():
    def encrypt_password(password):
        salt = bcrypt.gensalt()
        hashed_pass = bcrypt.hashpw(password.encode("utf-8"), salt=salt)
        return hashed_pass.decode("utf-8")
    artist1 = artist(username="lettuce1",bio = "random bio with stuff in it", password= encrypt_password("password123"))
    artist2 = artist(username="lettuce2",bio = "random bio with stuff in it", password= encrypt_password("stuffandmorestuff"))
    artist3 = artist(username="lettuce3",bio = "random bio with stuff in it", password= encrypt_password("lettuceandtomato"))
    
    return [artist1,artist2,artist3]

# created sample images with no images yet beacuse theyre not up
def create_sample_images():
    image1 = image(name="elephant",link = "https://static.displate.com/857x1200/displate/2022-12-16/61aac9750fcf60be73e1eb48ea252178_99e7452b66a3dde6ef93c2402df907cc.jpg")
    image2 = image(name="dog",link = "https://static.displate.com/857x1200/displate/2022-08-15/f66919cf8b5f967cab48c2385ea4f3ca_9d26ebeb8b1ba7b1b6b22699f5282f35.jpg")
    image3 = image(name="car",link = "https://static.displate.com/857x1200/displate/2022-12-15/b26f1f5b6578a79b2cebfbad72411252_16922d65877ad47895e139561fc4fe32.jpg")
    
    return [image1,image2,image3]

# created sample AIA to start relationships between Artist and images
def create_sample_AIA(imageList,artistList):
    AIA_list = []
    for _ in range(3):
        s_artist = choice(artistList)
        s_images = choice(imageList)
        AIA_list.append(
            AIA(
                artist_id = s_artist.id,
                image_id = s_images.id
            )
        )
    return AIA_list


# SEEDING app.db
with app.app_context():
    print("seeding data............")

    print("\n\t Deleting pre existing table data.........")
    artist.query.delete()
    image.query.delete()
    AIA.query.delete()

    db.session.commit()
    print("\t Data deleteion succesful")

    print("\n\t Generating sample data for artist with no hashing at the moment")
    sample_artist = create_sample_artist()
    db.session.add_all(sample_artist)
    db.session.commit()
    print("\t Artist sample data generated")

    print("\n\tGenerating sample data for the images with no links at the moment")
    sample_images = create_sample_images()
    db.session.add_all(sample_images)
    db.session.commit()
    print("\t Image sample data generated")

    print("\n\t Generating AIA sample data")
    sample_AIA = create_sample_AIA(sample_images,sample_artist)
    db.session.add_all(sample_AIA)
    db.session.commit()
    print("\t AIA sample data generation complete")


    print("\n Data seeding complete")