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
    .toc-title, .toc { font-weight: bold !important; }
    .toc-title { font-size: 1.7em; }
    .toc-level-1 { font-size: 1.3rem; }
    .toc-level-2 { font-size: 1.2rem; }
    .toc-level-3 { font-size: 1.1rem; }

    @media (min-width: 992px) {
        .toc, .toc-title { display: none !important; }
    }
</style>
`;
hexo.extend.injector.register('head_end', toc_style, 'post');


const code_fonts = `
<style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code&display=swap');
    pre > span, code { font-family: 'Fira Code', sans-serif !important; }
</style>
`;
hexo.extend.injector.register('head_begin', code_fonts, 'post');


// source: https://tsuiokuyo.netlify.app/posts/5a26/
// also used as wrapper for all kinds of iframe in post to prevent overflow!  
const yt_tag = `
<style>
    .video-container {
        position: relative;
        padding: 30px 0 56.25%;
        margin-bottom: 16px;
        height: 0;
        overflow: hidden;
    }
    .video-container iframe,
    .video-container object,
    .video-container embed {
        position: absolute;
        inset: 0; /* 取代 top:0; left:0; */
        width: 100%;
        height: 100%;
    }
</style>
`;
hexo.extend.injector.register('head_begin', yt_tag, 'post');


const adjust_image_preview_size = `
<style>
    .group-image-wrap { align-items: center; }

    .group-image-wrap .fancybox,
    .group-image-container img {
        width: -webkit-fill-available;
        width: -moz-fill-available;
        width: fill-available;
    }

    .post-content img { max-height: 350px; }
</style>
`;
hexo.extend.injector.register('head_begin', adjust_image_preview_size, 'post');


// warning: code block is also implemented by table,
// but the selector is .markdown-body > figure > table

const full_size_table = `
<style>
    .markdown-body > table { display: table !important; }
</style>
`;
hexo.extend.injector.register('head_begin', full_size_table, 'post');


const delete_LHS_column = `
<style>
    @media (min-width: 992px) {
        .post-content, .post-custom { padding: 0 12% !important; }
    }
</style>
`;
hexo.extend.injector.register('head_begin', delete_LHS_column, 'post');


// distinguish header and content by serif / sans-serif
// from himiku.com
const serif_header = `
<style>
    .toc-title,
    h1, h2, h3, h4, h5, h6 {
        font-family: "PingFang SC","Hiragino Sans GB","Microsoft Yahei",
                    "WenQuanYi Micro Hei","Segoe UI Emoji","Segoe UI Symbol",
                    Helvetica, Arial, -apple-system, system-ui, sans-serif !important;
    }
</style>
`;
hexo.extend.injector.register('head_begin', serif_header, 'post');