/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        'bodoni': ['BodoniFLF', 'serif'], // Define 'bodoni' como una clase utilizable en Tailwind
      },
    },
  },
  plugins: [
    require('daisyui'),
  ],
}

