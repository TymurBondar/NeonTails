import { Link } from "react-router-dom";

function Artists() {
  return (
    <div className="flex w-full mt-12">
      <ul className="flex w-full justify-evenly">
        <li>
          <Link to="/artists/1">Artist 1</Link>
        </li>
        <li>
          <Link to="/artists/2">Artist 2</Link>
        </li>
        <li>
          <Link to="/artists/3">Artist 3</Link>
        </li>
      </ul>
    </div>
  );
}

export default Artists;
