import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="p-10 bg-gradient-to-r from-purple-700 to-rose-600 font-bold rounded-b-2xl">
      <ul className="flex text-2xl w-full">
        <li className="pl-5 pr-5 rounded-lg scale-100 hover:scale-105 hover:bg-purple-800 hover:mr-5 duration-300">
          <Link to="/">Home</Link>
        </li>
        <li className=" pl-5 pr-5 rounded-lg scale-100 hover:scale-105 hover:bg-purple-800 hover:ml-5 hover:mr-5 duration-300">
          <Link to="/artists">Artists</Link>
        </li>
        <li className=" pl-5 pr-5 rounded-lg scale-100 hover:scale-105 hover:bg-purple-800 hover:ml-5 duration-300 mr-auto">
          <Link to="/exhibitions">Exhibitions</Link>
        </li>
        <li className="pl-5 pr-5 rounded-lg scale-100 hover:scale-105 hover:bg-rose-700 duration-300 font-light">
          <Link to="/signin">Artist Sign In</Link>
        </li>
      </ul>
    </nav>
  );
}
export default Navbar;