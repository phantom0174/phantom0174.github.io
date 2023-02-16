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
