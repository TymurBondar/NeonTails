import { Link } from "react-router-dom";
function Root() {
  return (
    <nav>
      <ul className="flex justify-between text-2xl">
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/artists">Artists</Link>
        </li>
        <li>
          <Link to="/exhibitions">Exhibitions</Link>
        </li>
      </ul>
    </nav>
  );
}

export default Root;
