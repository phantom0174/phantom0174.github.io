const inject_code = `
<style>
    .index-img {
        transition: .4s;
    }

    .index-card:hover .index-img {
        transform: scale(1.05);
    }
</style>
`;

hexo.extend.injector.register('head_end', inject_code, 'home');
