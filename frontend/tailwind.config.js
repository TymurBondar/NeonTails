/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      keyframes: {
        wiggle: {
          "0%, 100%": { transform: "rotate(0)" },
          "25%": { transform: "rotate(-6deg)" },
          "75%": { transform: "rotate(6deg)" },
        },
      },
    },
  },
  plugins: [],
};
