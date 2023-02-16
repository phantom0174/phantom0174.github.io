// subtitle enlarge & hover::glowing animation
const subtitle_style = `
<style>
    #subtitle, .typed-cursor {
        font-size: 2rem;
        transition: .6s;
        transition-delay: 0.1s;
    }

    @media (max-width: 767px) {
        #subtitle, .typed-cursor {
            font-size: 1.8rem;
        }
    }
    
    .banner-text:hover #subtitle,
    .banner-text:hover .typed-cursor {
        text-shadow: 0 0 10px #FC0, 0 0 20px #FC0, 0 0 40px #FC0;
    }
</style>
`;
hexo.extend.injector.register('head_end', subtitle_style, 'default');
