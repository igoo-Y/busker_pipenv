const colors = require('tailwindcss/colors')

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        'busker-navy': '#1D1D43',
        'busker-light-blue': '#7381FF',
      },
      spacing: {
        "25vh": "25vh",
        "50vh": "50vh",
        "75vh": "75vh",
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}