import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { UserContext } from "../components/UserContext";

function Signin() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { setUser } = useContext(UserContext);

  const handleLogin = async (event) => {
    event.preventDefault();
    try {
      const response = await fetch("http://127.0.0.1:5000/artist/signin", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        response.json().then((data) => {
          const userData = { id: data.id, username: data.username };
          localStorage.setItem("user", JSON.stringify(userData));
          setUser(userData);
        });
        const redirectLink = `/`;
        navigate(redirectLink); // Redirect on success
      } else {
        // Handle errors (e.g., incorrect credentials)
        console.log("Incorrect!");
      }
    } catch (error) {
      // Handle network errors
      console.log(error);
    }
  };
  return (
    <div className="w-full flex flex-col mt-12 space-y-12 text-3xl">
      <form
        onSubmit={handleLogin}
        className="font-light flex flex-col items-center text-left"
      >
        <label htmlFor="username">Username or Email</label>
        <input
          type="text"
          name="username"
          id="username"
          autoComplete="email"
          value={username}
          onChange={(event) => setUsername(event.target.value)}
          className="text-xl bg-transparent border-4 px-4 py-1 border-violet-500 rounded-2xl mt-2"
        />
        <label htmlFor="password" className="mt-5">
          Password
        </label>
        <input
          type="password"
          name="password"
          autoComplete="current-password"
          id="password"
          value={password}
          onChange={(event) => setPassword(event.target.value)}
          className="text-xl bg-transparent border-4 px-4 py-1 border-violet-500 rounded-2xl mt-2"
        />
        <button
          type="submit"
          className="text-xl bg-transparent border-4 px-4 py-1 border-violet-500 rounded-2xl mt-2"
        >
          Sign In
        </button>
      </form>
    </div>
  );
}

export default Signin;
