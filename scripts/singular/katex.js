// styling and auto-rendering
const katex = `
<style>
    .katex>.katex-html {
        white-space: nowrap;
        overflow-x: scroll;
        overflow-y: hidden;
    }

    .katex>.katex-html>.tag {
        position: relative !important;
        left: 10% !important;
    }
</style>

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.css" integrity="sha384-vKruj+a13U8yHIkAyGgK1J3ArTLzrFGBbBc0tDp4ad/EyewESeXE/Iv67Aj8gKZ0" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/katex.min.js" integrity="sha384-PwRUT/YqbnEjkZO0zZxNqcxACrXe+j766U2amXcgMg5457rve2Y7I6ZJSm2A0mS4" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.4/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {
        renderMathInElement(document.body, {
            delimiters: [
                { left: '$$', right: '$$', display: true },
                { left: '$', right: '$', display: false }
            ],
            throwOnError: false
        });
    });
</script>
`;
hexo.extend.injector.register('head_end', katex, 'post');
hexo.extend.injector.register('head_end', katex, 'about');


// prevents google-translate from translating
const no_trans = `
<script>
    document.addEventListener("DOMContentLoaded", function() {
        katex_list = document.getElementsByClassName('katex');
        for (let i = 0; i < katex_list.length; i++) {
            katex_list[i].classList.add('notranslate');
        }
    });
</script>
`;
hexo.extend.injector.register('body_end', no_trans, 'post');
hexo.extend.injector.register('body_end', no_trans, 'about');
