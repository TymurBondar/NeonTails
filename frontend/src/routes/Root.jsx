import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";
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
