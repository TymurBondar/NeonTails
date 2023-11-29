import { Link } from "react-router-dom";

function Exhibitions(){
    return (
        <div className="flex w-full mt-12">
            <ul className="flex w-full justify-evenly">
                <li><Link to="/exhibitions/cats">Cats</Link></li>
                <li><Link to="/exhibitions/dogs">Dogs</Link></li>
                <li><Link to="/exhibitions/cyberpunk">Cyberpunk</Link></li>
            </ul>
        </div>
    );
};

export default Exhibitions;