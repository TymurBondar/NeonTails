import { useContext, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import { UserContext } from "../components/UserContext";
import Card from "../components/Card";

function ArtistProfile() {
  const { user } = useContext(UserContext);
  const [images, setImages] = useState([]);

  function handleImageDeletion(event){
    const imageId = parseInt(event.target.id);
    //delete image object with given id
    setImages(images.filter(image => image.id !== imageId));
    console.log(images);
  };

  useEffect(() => {
    fetch(`/api/${user.id}/images`)
      .then((res) => res.json())
      .then((data) => {
        let newImages = [];
        data.forEach((element) => {
          newImages.push(element.image);
        });
        setImages(newImages);
        console.log(newImages);
      });
  }, []);

  if (!user) return <Navigate to="/signin" />;
  else
    return (
      <div className="flex flex-col items-center space-y-20 w-full">
        <h1 className="mt-12">Hello, {user.username}! Here are your images</h1>
        <div className="grid grid-cols-3 gap-36">
          {images.map((image) => (
            <div>
            <Card key={image.id} image={image} />
            <button className="border-4 rounded-lg px-5 bg-blue-800 border-violet-700">Edit</button>
            <br />
            <button id={image.id} className="border-4 rounded-lg px-5 bg-red-800 border-violet-700" onClick={handleImageDeletion}>Delete</button>
            </div>
          ))}
        </div>
      </div>
    );
}

export default ArtistProfile;
