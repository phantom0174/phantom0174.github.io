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

<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.css" integrity="sha384-5TcZemv2l/9On385z///+d7MSYlvIEw9FuZTIdZ14vJLqWphw7e7ZPuOiCHJcFCP" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/katex.min.js" integrity="sha384-cMkvdD8LoxVzGF/RPUKAcvmm49FQ0oxwDF3BGKtDXcEc+T1b2N+teh/OJfpU0jr6" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.22/dist/contrib/auto-render.min.js" integrity="sha384-hCXGrW6PitJEwbkoStFjeJxv+fSOOQKOPbJxSfM6G5sWZjAyWhXiTIIAmQqnlLlh" crossorigin="anonymous"></script>
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
