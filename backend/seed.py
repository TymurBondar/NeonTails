from models import db,artist,image,AIA
from app import app
from random import choice

# created sample artist currently with no authentication just to seed the tables
def create_sample_artist():
    artist1 = artist(name="lettuce1",bio = "random bio with stuff in it")
    artist2 = artist(name="lettuce2",bio = "random bio with stuff in it")
    artist3 = artist(name="lettuce3",bio = "random bio with stuff in it")
    
    return [artist1,artist2,artist3]

# created sample images with no images yet beacuse theyre not up
def create_sample_images():
    image1 = image(name="name1",link = "definitelylink1")
    image2 = image(name="name2",link = "definitelylink2")
    image3 = image(name="name3",link = "definitelylink3")
    
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