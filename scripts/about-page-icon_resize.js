const inject_code = `
<style>
    .about-icons>a>i {
        font-size: 1.3rem;
    }
</style>
`;

hexo.extend.injector.register('head_end', inject_code, 'about');
