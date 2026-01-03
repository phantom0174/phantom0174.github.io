// subtitle enlarge & hover::glowing animation
const subtitle_style = `
<style>
    #subtitle, .typed-cursor {
        display: inline-block;
        font-size: 2.2rem;
        animation: blinking 2s ease-in-out 0.5s infinite alternate;
    }
    @keyframes blinking {
        from { opacity: 1; transform: scale(1); }
        to { opacity: 0.4; transform: scale(0.97); }
    }
    @media (max-width: 991px) { #subtitle, .typed-cursor { font-size: 2.1rem; } }
    @media (max-width: 767px) { #subtitle, .typed-cursor { font-size: 2rem; } }
    @media (max-width: 544px) { #subtitle, .typed-cursor { font-size: 1.8rem; } }
    @media (max-width: 432px) { #subtitle, .typed-cursor { font-size: 1.6rem; } }
</style>
`;
hexo.extend.injector.register('head_end', subtitle_style, 'default');
