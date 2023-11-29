import { useParams } from "react-router-dom";

function ThemedExhibition(){
    const {theme} = useParams();
    // add validation to only redirect to exhibitions that exist.
    return (
        <>
        This is the exhibition of {theme} images
        </>
    );
};

export default ThemedExhibition;