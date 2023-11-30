import { useState } from "react";

function Card() {
  const [isFlipped, setIsFlipped] = useState(false);
  const [isBouncing, setIsBouncing] = useState(false);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
    setIsBouncing(true);
    setTimeout(() => {
      setIsBouncing(false);
    }, 550); // Duration of the animation
  };

  return (
    <div
      onClick={handleFlip}
      className={
        isBouncing
          ? "max-wsm rounded-lg flex flex-col justify-center transition-transform duration-300 object-scale-down border-8 border-fuchsia-400 animate-[wiggle_0.55s_ease-in-out_both] overflow-hidden"
          : "max-wsm rounded-lg flex flex-col justify-center transition-transform duration-300 object-scale-down scale-100 border-8 border-fuchsia-600 hover:border-fuchsia-500 overflow-hidden"
      }
    >
      {isFlipped ? (
        <>
            <img
              src="https://static.displate.com/280x392/displate/2022-05-10/f0edbfd528a2d95e397dfe3d5eef1f68_5e86cb4cbc9618c4140f77c360215d11.jpg"
              className="mb-2 rounded-b-md border-b-8 border-fuchsia-600 blur-lg brightness-75 duration-700"
            />
            <p className="absolute w-full text-center font-light">Cat looking at cyberbutterfly</p>
          <h2 className="mb-2 text-2xl font-light tracking-light text-white pt-2 text-center duration-700 ">
            Artist
          </h2>
        </>
      ) : (
        <>
          <img
            src="https://static.displate.com/280x392/displate/2022-05-10/f0edbfd528a2d95e397dfe3d5eef1f68_5e86cb4cbc9618c4140f77c360215d11.jpg"
            className="mb-2 rounded-b-md border-b-8 border-fuchsia-600 duration-700 scale-100 hover:scale-110"
          />
          <h2 className="mb-2 text-2xl font-normal tracking-light text-white text-center mt-3">
            Image
          </h2>
        </>
      )}
    </div>
  );
}

export default Card;
