/** @type {import('tailwindcss').Config} */
module.exports = {
  // NOTE: Update this to include the paths to all of your component files.
  content: ["./app/**/*.{js,jsx,ts,tsx}"],
  presets: [require("nativewind/preset")],
  theme: {
    extend: {
      colors: {
        primary: '#1B263B',
        secondary: '#E0E1DD',
        text: '#778DA9',
        textDim: '#415A77',
        error: '#c1121f',
        good: '#588157'
      }
    },
  },
  plugins: [],
}