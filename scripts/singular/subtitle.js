// subtitle enlarge & hover::glowing animation
const subtitle_style = `
<style>
    #subtitle, .typed-cursor {
        font-size: 2.2rem;
        animation: blinking 2s ease-in-out 0.5s infinite alternate;
    }

    @keyframes blinking {
        from {
            text-shadow: none;
        }
        to {
            text-shadow: 0 0 10px #FC0, 0 0 20px #FC0, 0 0 40px #FC0;
        }
    }

    @media (max-width: 991px) {
        #subtitle, .typed-cursor {
            font-size: 2.1rem;
        }
    }

    @media (max-width: 767px) {
        #subtitle, .typed-cursor {
            font-size: 2rem;
        }
    }

    @media (max-width: 544px) {
        #subtitle, .typed-cursor {
            font-size: 1.8rem;
        }
    }

    @media (max-width: 432px) {
        #subtitle, .typed-cursor {
            font-size: 1.6rem;
        }
    }
</style>
`;
hexo.extend.injector.register('head_end', subtitle_style, 'default');
