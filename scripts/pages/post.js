const toc_autogen = `
<p class="toc-title">Contents</p>
<%- toc(page.content, {
    list_number: false,
    max_depth: 3
}) %>
`;
hexo.extend.filter.register('theme_inject', function (injects) {
    injects.postMarkdownBegin.raw('custom-toc', toc_autogen);
});


const toc_style = `
<style>
    .toc-title {
        font-weight: bold !important;
        font-size: calc(17px * 1.5);
    }

    @media (max-width: 575px) {
        .toc-title {
            font-size: calc(16px * 1.5) !important;
        }
    }

    .toc {
        font-weight: bold !important;
    }

    .toc-level-1 {
        font-size: 21px;
    }

    .toc-level-2 {
        font-size: 19px;
    }

    .toc-level-3 {
        font-size: 17px;
    }
</style>
`;
hexo.extend.injector.register('head_end', toc_style, 'post');


const code_fonts = `
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code&display=swap');

    pre>span,
    code {
        font-family: 'Fira Code', sans-serif !important;
        font-display: swap;
    }
</style>
`;
hexo.extend.injector.register('head_begin', code_fonts, 'post');

// source: https://tsuiokuyo.netlify.app/posts/5a26/
const yt_tag = `
<style>
    .video-container {
        position: relative;
        padding-bottom: 56.25%;
        padding-top: 30px;
        margin-bottom: 16px;
        height: 0;
        overflow: hidden;
    }

    .video-container iframe, .video-container object, .video-container embed {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
    }
</style>
`;

hexo.extend.injector.register('head_begin', yt_tag, 'post');


const spoiler = `
<style>
    .spoiler {
        margin-bottom: 16px;
    }
</style>
`;

hexo.extend.injector.register('head_begin', spoiler, 'post');
