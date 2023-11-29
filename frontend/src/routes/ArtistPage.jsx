import { useParams } from "react-router-dom";
// import { useState } from "react";

function ArtistPage(){
    const { id } = useParams();

    //add validation so id is a number
    //fetch database to see if the artists with that id exists

    return (
        <>
        This is a page of Artist with the ID of { id }
        </>
    );
};

export default ArtistPage;