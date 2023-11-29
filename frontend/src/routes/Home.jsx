import Card from "../components/Card";
function Home() {
  return (
    <div className="flex flex-col items-center space-y-20 w-full">
      <h1 className="mt-12">Featured Images</h1>
      <div className="flex flex-row flex-wrap justify-evenly w-full">
        <Card />
        <Card />
        <Card />
      </div>
    </div>
  );
}

export default Home;
