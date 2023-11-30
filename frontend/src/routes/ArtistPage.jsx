import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";

function ArtistPage(){
    const { id } = useParams();

    const [images, setImages] = useState([]);

    //add validation so id is a number
    //fetch database to see if the artists with that id exists
    //if artists exists, get the artists images in the list
    useEffect(() => {
        fetch(`/api/${id}/images`)
      .then(res => res.json())
      .then(data => {
        let newImages = [];
        data.forEach(element => {
            newImages.push(element.image);
        });
        setImages(newImages);
        console.log("log" + newImages);
        console.log(newImages[0]);
      })
    },[]);

    return (
        <>
        This is a page of Artist with the ID of { id }

        </>
    );
};

export default ArtistPage;