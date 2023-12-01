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
    image1 = image(name="elephant",link = "https://static.displate.com/857x1200/displate/2022-12-16/61aac9750fcf60be73e1eb48ea252178_99e7452b66a3dde6ef93c2402df907cc.jpg", description = "cyberpunk elephant")
    image2 = image(name="dog",link = "https://static.displate.com/857x1200/displate/2022-08-15/f66919cf8b5f967cab48c2385ea4f3ca_9d26ebeb8b1ba7b1b6b22699f5282f35.jpg", description = "ghost dog")
    image3 = image(name="car",link = "https://static.displate.com/857x1200/displate/2022-12-15/b26f1f5b6578a79b2cebfbad72411252_16922d65877ad47895e139561fc4fe32.jpg", description = "cyberpunk car")
    
    image4 = image(name="ai mess",link = "https://images.nightcafe.studio/jobs/0FgBSa1wLWyX78kSC5yK/0FgBSa1wLWyX78kSC5yK.jpg?tr=w-1600,c-at_max", description = "cyberpunk human thing")
    image5 = image(name="cyberpunk cat",link = "https://static.displate.com/857x1200/displate/2023-03-13/13e12cfc4ce23562881c2a3d1a9e94b2_4350d83043ceede305362eb10b809bd5.jpg", description = "cyberpunk cat")
    image6 = image(name="person in rain",link = "https://static.displate.com/857x1200/displate/2023-01-03/f0284c7b8239d98cdb9f409e0c8dfe80_fc16bd534025ce3fad9881010e439d00.jpg", description = "cyberpunk person in rain")

    image7 = image(name="programming cat",link = "https://static.displate.com/857x1200/displate/2021-12-27/d1ebbd13f36500effce9cffff671acc1_7f2c359f01258af50ce51b9adbe684ec.jpg", description = "programming cat")
    image8 = image(name="dog with donut",link = "https://static.displate.com/857x1200/displate/2023-02-12/f0d616a0f41668a2ff7755e35a0667a3_82796f356d5cac6688888f6b51f5e0ca.jpg", description = "dog eating donut")
    image9 = image(name="real",link = "https://static.displate.com/857x1200/displate/2021-04-20/d9cf03528222ea96aea1e8487e3212e1_9868c3336b4ea853c196828dcd3a45b3.jpg", description = "real")

    return [image1,image2,image3,image4,image5,image6,image7,image8,image9]

# created sample AIA to start relationships between Artist and images
def create_sample_AIA(imageList,artistList):
    AIA_list = []
    for _ in range(3):
        s_artist = choice(artistList)
        for _ in range(3):
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