import { Link, Outlet } from "react-router-dom";
function Root() {
  return (
    <div className="flex flex-col h-screen bg-gradient-to-r from-stone-950 to-zinc-800 text-white">
      <nav className="p-10 bg-gradient-to-r from-purple-700 to-rose-600 font-bold rounded">
        <ul className="flex text-2xl space-x-12">
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
      <div className="flex flex-1 justify-center items-center font-semibold text-4xl">
      <Outlet/>
      </div>
    </div>
  );
}

export default Root;
