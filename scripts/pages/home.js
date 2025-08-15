const search_console_veri = `
<meta name="google-site-verification" content="FC5fN9pWuCG_-GE3v6DAVW-mkjNvqiDUlaAGrz1SGXo" />
`;
hexo.extend.injector.register('head_end', search_console_veri, 'home');

const img_enlarge_anima = `
<style>
    .index-img { transition: .4s; }
    .index-card:hover .index-img { transform: scale(1.05); }
</style>
`;
hexo.extend.injector.register('head_end', img_enlarge_anima, 'home');


const remove_blurred_navbar_effect = `
<style>
    .navbar .dropdown-collapse, .navbar-col-show, .top-nav-collapse {
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
    }
</style>
`;
hexo.extend.injector.register('head_begin', remove_blurred_navbar_effect, 'home');
