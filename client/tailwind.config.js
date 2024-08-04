/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "primary-color": "#0D1B2A",
        "secondary-color": "#E0E1DD",
        "navbar-color":"#1B263B",
      },
    },
  },
  plugins: [require("daisyui")],
};
