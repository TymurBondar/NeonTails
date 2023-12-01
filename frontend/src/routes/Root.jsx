import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";


// AUTHORIZATION STEPS:
// Mario is going to have an authorization route built that SHOULD RETURN A USER OBJECT.
// This user object SHOULD CONTAIN AN ID.
// We need to save this user object in state at the home level.
//    This will probably need a `useEffect` to perform a fetch every time Home is reloaded.
//    And we'll need a `useState` at the end of the fetch's promise to store the user in state.
//        `currentUser, setCurrentUser = useState(null);
// Once the user data is saved in state, we can transfer it across the application using PROPS.
// At every authorizable view/component, we check if the ID matches the artist's page ID.
//    If it does, display something/enable something.
//    IF it doesn't, do something else.

function Root() {
  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-r from-stone-950 to-zinc-800 text-white">
      <Navbar />
      <div className="flex flex-1 justify-center font-semibold text-4xl w-full">
        <Outlet />
      </div>
    </div>
  );
}

export default Root;
