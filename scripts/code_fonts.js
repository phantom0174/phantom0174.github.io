const inject_code = `
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code&display=swap');

    pre>span,
    code {
        font-family: 'Fira Code', sans-serif !important;
        font-display: swap;
    }
</style>
`;

hexo.extend.injector.register('head_begin', inject_code, 'post');
