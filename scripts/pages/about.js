const social_icon_minify = `
<style>
    .about-icons>a>i {
        font-size: 1.3rem;
    }
</style>
`;
hexo.extend.injector.register('head_end', social_icon_minify, 'about');
