import { Link } from "react-router-dom";
import { useContext } from "react";
import { UserContext } from "./UserContext";
import { useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();
  const { user } = useContext(UserContext);
  let isLoggedIn = false;
  if (user !== null) {
    isLoggedIn = true;
  }

  // Assuming this is in a component where UserContext is accessible
  const { setUser } = useContext(UserContext);

  const handleLogout = () => {
    // Clear user data from localStorage
    localStorage.removeItem("user");

    // Log out the user in the backend
    fetch("http://127.0.0.1:5000/artists/logout", { method: "DELETE" })
      .then((response) => response.json())
      .then((data) =>
        console.log(`${data} "I logged out the user from the backend!"`)
      )
      .then(
        // Update the user context to reflect that the user is logged out
        setUser(null)
      )

    //redirect the user to the login page or homepage
    navigate("/");
  };

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
        {isLoggedIn ? (
          <li className="pl-5 pr-5 rounded-lg scale-100 hover:scale-105 hover:bg-rose-700 duration-300 hover:mr-5 font-light">
            <Link to="/artist/profile">Profile</Link>
          </li>
        ) : (
          ""
        )}
        <li className="pl-5 pr-5 rounded-lg scale-100 hover:scale-105 hover:bg-rose-700 hover:ml-5 duration-300 font-light">
          {isLoggedIn ? (
            <button onClick={handleLogout}>Logout</button>
          ) : (
            <Link to="/signin">Sign In</Link>
          )}
        </li>
      </ul>
    </nav>
  );
}
export default Navbar;
