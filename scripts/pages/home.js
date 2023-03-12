const search_console_veri = `
<meta name="google-site-verification" content="FC5fN9pWuCG_-GE3v6DAVW-mkjNvqiDUlaAGrz1SGXo" />
`;

hexo.extend.injector.register('head_end', search_console_veri, 'home');

const img_enlarge_anima = `
<style>
    .index-img {
        transition: .4s;
    }

    .index-card:hover .index-img {
        transform: scale(1.05);
    }
</style>
`;
hexo.extend.injector.register('head_end', img_enlarge_anima, 'home');
