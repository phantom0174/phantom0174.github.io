const inject_code = `
<script>
    document.addEventListener("DOMContentLoaded", function() {
        katex_list = document.getElementsByClassName('katex');
        for (let i = 0; i < katex_list.length; i++) {
            katex_list[i].classList.add('notranslate');
        }
    });
</script>
`;

hexo.extend.injector.register('body_end', inject_code, 'post');
hexo.extend.injector.register('body_end', inject_code, 'about');
