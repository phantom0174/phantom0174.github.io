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
        font-size: 1.7em;
    }

    .toc {
        font-weight: bold !important;
    }

    .toc-level-1 {
        font-size: 1.3rem;
    }

    .toc-level-2 {
        font-size: 1.2rem;
    }

    .toc-level-3 {
        font-size: 1.1rem;
    }

    </style>
`;
hexo.extend.injector.register('head_end', toc_style, 'post');

/*
@media (max-width: 575px) {
    .toc-title {
        font-size: calc(1.7em * (16/17));
    }

    .toc-level-1 {
        font-size: calc(1.3rem * (16/17));
    }

    .toc-level-2 {
        font-size: calc(1.2rem * (16/17));
    }

    .toc-level-3 {
        font-size: calc(1.1rem * (16/17));
    }
}
*/

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
// also used as wrapper for all kinds of iframe in post to prevent overflow!  
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

// hexo.extend.injector.register('head_begin', spoiler, 'post');

const smooth_scroll = `
<style>
    html, body {
        scroll-behavior: smooth;
    }
</style>

<script src="https://cdnjs.cloudflare.com/ajax/libs/smoothscroll/1.4.10/SmoothScroll.min.js" integrity="sha512-HaoDYc3PGduguBWOSToNc0AWGHBi2Y432Ssp3wNIdlOzrunCtB2qq6FrhtPbo+PlbvRbyi86dr5VQx61eg/daQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
`;

hexo.extend.injector.register('head_begin', smooth_scroll, 'post');

const adjust_image_preview_size = `
<style>
    .group-image-wrap {
        align-items: center;
    }

    .group-image-wrap .fancybox {
        width: -webkit-fill-available;
        width: -moz-fill-available;
        width: -moz-available;
        width: fill-available;
    }

    .group-image-container img {
        width: -webkit-fill-available;
        width: -moz-fill-available;
        width: -moz-available;
        width: fill-available;
    }

    .post-content img {
        max-height: 350px;
    }
</style>
`;
hexo.extend.injector.register('head_begin', adjust_image_preview_size, 'post');


// warning: code block is also implemented by table,
// but the selector is .markdown-body > figure > table

const full_size_table = `
<style>
    .markdown-body > table {
        display: table !important;
    }
</style>
`;

hexo.extend.injector.register('head_begin', full_size_table, 'post');

const del_left_col = `
<style>
    @media (min-width: 992px) {
        .post-content, post-custom {
            padding-left: 12% !important;
            padding-right: 12% !important;
        }
    }
</style>
`;

hexo.extend.injector.register('head_begin', del_left_col, 'post');


// distinguish header and content by serif / sans-serif
// from himiku.com

const serif_header = `
<style>
    h1, h2, h3, h4, h5, h6, h7 {
        font-family: "PingFang SC","Hiragino Sans GB","Microsoft Yahei","WenQuanYi Micro Hei","Segoe UI Emoji","Segoe UI Symbol",Helvetica,Arial,-apple-system,system-ui,sans-serif !important;
    }
</style>
`;

hexo.extend.injector.register('head_begin', serif_header, 'post');