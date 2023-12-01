import { useContext, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import { UserContext } from "../components/UserContext";
import Card from "../components/Card";

function ArtistProfile() {
  const { user } = useContext(UserContext);
  const [images, setImages] = useState([]);
  const [newName, setNewName] = useState("");

  function handleImageDeletion(event) {
    const imageId = parseInt(event.target.id);
    //delete image object with given id
    fetch(`/api/image/delete/${imageId}`, {method: "DELETE"})
    .then(res => res.json())
    .then(data => console.log(data))
    .then(setImages(images.filter((image) => image.id !== imageId)))
    console.log(images);
  }

  function handleImageNameChange(event) {
    setNewName(event.target.value);
  }

  function handleImageSetNewName(event) {
    event.preventDefault();
    const imageId = parseInt(event.target.id);

    const updatedImage = {
      "name": newName,
    };
    fetch(`http://127.0.0.1:5000/api/image/update/${imageId}`, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      credentials: "same-origin",
      body: JSON.stringify({updatedImage})
    });
  }

  useEffect(() => {
    console.log(user);
    fetch(`http://127.0.0.1:5000/api/${user.id}/images`, {
      credentials: "same-origin"
    })
      .then((res) => res.json())
      .then((data) => {
        let newImages = [];
        data.forEach((element) => {
          newImages.push(element.image);
        });
        setImages(newImages);
      });
  }, []);

  if (!user) return <Navigate to="/signin" />;
  else
    return (
      <div className="flex flex-col items-center space-y-20 w-full">
        <h1 className="mt-12">Hello, {user.username}! Here are your images</h1>
        <div className="grid grid-cols-3 gap-36">
          {images.map((image) => (
            <div key={image.id}>
              <Card key={image.id} image={image} />
              <form className="" onSubmit={handleImageSetNewName} id={image.id}>
                <input
                  type="text"
                  id={image.id}
                  onChange={handleImageNameChange}
                  className=" bg-transparent rounded-md px-5 border-4 border-violet-600 mt-5"
                />
                <input
                  type="submit"
                  className="bg-blue-400 rounded-md px-5 mt-5"
                  value="Change Name"
                />
              </form>
              <br />
              <button
                id={image.id}
                className="border-4 rounded-lg px-5 bg-red-800 border-violet-700"
                onClick={handleImageDeletion}
              >
                Delete
              </button>
            </div>
          ))}
        </div>
      </div>
    );
}

export default ArtistProfile;
