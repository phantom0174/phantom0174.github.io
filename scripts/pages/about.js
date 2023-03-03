const social_icon_minify = `
<style>
    i.icon-spotify {
        font-size: 1.35rem !important;
    }
</style>
`;
hexo.extend.injector.register('head_end', social_icon_minify, 'about');
