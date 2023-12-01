import { useContext } from "react";
import { Navigate } from "react-router-dom";
import { UserContext } from "../components/UserContext";
import Card from "../components/Card";

function ArtistProfile() {
  const { user } = useContext(UserContext);
  if (!user) return <Navigate to="/signin" />;
  else
    return (
      <div className="flex flex-col items-center space-y-20 w-full">
        <h1 className="mt-12">Hello, {user.username}! Here are your images</h1>
        <div className="grid grid-cols-3 gap-36">
          <Card image={''} />
          <Card image={''} />
          <Card image={''} />
        </div>
      </div>
    );
}

export default ArtistProfile;
