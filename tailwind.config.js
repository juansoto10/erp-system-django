/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./apps/**/*.{html,js}'],
  darkMode: 'class', // or 'media' or 'class'
  theme: {
    extend: {
      height: {
        100: 'calc(100vh - 177px)',
      },
      minHeight: {
        nice: 'calc(100vh - 223px)',
        cool: 'calc(100vh - 177px)',
      },
      colors: {
        'dark-main': '#181818',
        'dark-bg': '#22202A',
        'dark-second': '#242526',
        'dark-third': '#100f14',
        'dark-txt': '#c1c1c1',
        dark: '#1C1D1F',
        'fb-gray': '#f0f2f5',
        purple: '#7C24D9',
        'gray-footer-500': '#1C1D1F',
        search: '#F7F9FA',
        careers: '#FEF9F5',
        ivory: '#F4F7F0',
        green: 'rgb(45 212 191);',
        misty: '#BFD2D0',
        'purple-mid': '#A084DC',
        azulito: '#4E4FEB',
        'dark-azulito': '#EA5455',
      },
      keyframes: {
        wiggle: {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' },
        },
        click: {
          '0%, 100%': { transform: 'scale(0.95)' },
          '80%': { transform: 'scale(0.95)' },
        },
        card: {
          '0%, 100%': { transform: 'scale(1.01)' },
          '80%': { transform: 'scale(1.01)' },
        },
      },
      animation: {
        wiggle: 'wiggle 200ms ease-in-out',
        click: 'click 10000ms ease-in-out',
        card: 'card 10000ms ease-in-out',
      },
    },
    boxShadow: {
      '2sm':
        '0 25px 50px 3px rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.04)',
      sm: '0 1px 2px 0 rgba(0, 0, 0, 0.05)',
      DEFAULT:
        '0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)',
      fb: '0 2px 2px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      md: '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)',
      lg: '0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)',
      button:
        '0 0px 10px 1px rgba(0, 0, 0, 0.2), 0 0px 2px 0px rgba(0, 0, 0, 0.05)',
      featured:
        '0 0px 50px 1px rgba(0, 0, 0, 0.1), 0 0px 2px 0px rgba(0, 0, 0, 0.05)',
      xl: '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
      '2xl': '0 0px 15px 0px rgba(0, 0, 0, 0.25)',
      '3xl': '0 35px 60px -15px rgba(0, 0, 0, 0.3)',
      inner: 'inset 0 2px 4px 0 rgba(0, 0, 0, 0.06)',
      none: 'none',
      complete: '2px 2px 17px -7px rgba(0, 0, 0, 0.25)',
    },
    screens: {
      s: '420px',

      sm: '640px',
      // => @media (min-width: 640px) { ... }

      md: '768px',
      // => @media (min-width: 768px) { ... }

      lg: '1024px',
      // => @media (min-width: 1024px) { ... }

      xl: '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
    },
  },
  variants: {
    extend: {
      display: ['group-hover'],
      transform: ['group-hover'],
      scale: ['group-hover'],
      textOpacity: ['dark'],
      outline: ['responsive', 'focus', 'hover', 'active'],
    },
  },
  plugins: [
    // require('@tailwindcss/forms'),
    // require('@tailwindcss/typography'),
    // require('@tailwindcss/line-clamp'),
    // require('@tailwindcss/aspect-ratio'),
    // require('tailwindcss-question-mark'),
    // require('tailwind-scrollbar-hide'),
  ],
};
