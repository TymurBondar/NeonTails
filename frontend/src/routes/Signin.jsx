function Signin() {
  return (
    <div className="w-full flex flex-col items-center mt-12 space-y-12">
        <form action="#" method="POST" className="font-light flex flex-col items-center text-left">
            <label htmlFor="username">Username or Email</label>
            <input type="text" name="username" id="username" className="text-xl bg-transparent border-4 px-4 py-1 border-violet-500 rounded-2xl"/>
            <label htmlFor="password">Password</label>
            <input type="password" name="password" id="password" className="text-xl bg-transparent border-4 px-4 py-1 border-violet-500 rounded-2xl"/>
            <input type="submit" value="Sign In"/>
        </form>
    </div>
  );
}

export default Signin;
