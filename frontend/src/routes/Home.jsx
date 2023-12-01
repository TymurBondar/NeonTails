import Card from "../components/Card";

function Home() {

  const image1 = 'https://static.displate.com/280x392/displate/2022-07-18/ed970c75e7c28f898755c7c437aa95a4_baab9fc4daba4f2dda2bfac1d8848aee.jpg';
  const image2 = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.MJPHrFv8OgTIAHjAm17clAAAAA%26pid%3DApi&f=1&ipt=114a5f6ebd50baedc1981249c7ec5e0868613f1675ce866ec942dd45289d8d70&ipo=images';
  const image3 = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.0FzNucDKjPIgbq7-sd1niwAAAA%26pid%3DApi&f=1&ipt=a0b0da281f92883400b51a02bb7cfa2c9830f9d338b9d9eb14897dbcf4462e18&ipo=images';
  return (
    <div className="flex flex-col items-center space-y-20 w-full">
      <h1 className="mt-12">Featured Images</h1>
      <div className="grid grid-cols-3 gap-36">
        <Card image={image1}/>
        <Card image={image2}/>
        <Card image={image3}/>
      </div>
    </div>
  );
}

export default Home;
