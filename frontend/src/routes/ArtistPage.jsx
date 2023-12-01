import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import Card from "../components/Card";

function ArtistPage() {
  const { id } = useParams();

  const [images, setImages] = useState([]);

  //add validation so id is a number
  //fetch database to see if the artists with that id exists
  //if artists exists, get the artists images in the list
  useEffect(() => {
    fetch(`/api/${id}/images`)
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

  return (
    <div className="flex flex-col items-center text-center mt-12 w-full">
      This is a page of Artist with the ID of {id}
      <div className="flex flex-row space-x-24 justify-center w-full mt-16">
        {images.map((image) => (
          <Card key={image.id} image={image} />
        ))}
      </div>
    </div>
  );
}

export default ArtistPage;
