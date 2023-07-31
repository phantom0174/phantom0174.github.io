const search_console_veri = `
<meta name="google-site-verification" content="FC5fN9pWuCG_-GE3v6DAVW-mkjNvqiDUlaAGrz1SGXo" />
`;

hexo.extend.injector.register('head_end', search_console_veri, 'home');

const img_enlarge_anima = `
<style>
    .index-img {
        transition: .4s;
    }

    .index-card:hover .index-img {
        transform: scale(1.05);
    }
</style>
`;
hexo.extend.injector.register('head_end', img_enlarge_anima, 'home');

// probably not suitable for fluid theme layout

// const alternating_flex_direction = `
// <style>
//     .row:nth-child(even) {
//         flex-direction: row-reverse;
//     }

//     // .row:nth-child(even) .index-info {
//     //     align-items: flex-end;
//     //     text-align: right;
//     // }
// </style>
// `;

// hexo.extend.injector.register('head_end', alternating_flex_direction, 'home');

const smooth_scroll = `
<script src="https://cdnjs.cloudflare.com/ajax/libs/smoothscroll/1.4.10/SmoothScroll.min.js" integrity="sha512-HaoDYc3PGduguBWOSToNc0AWGHBi2Y432Ssp3wNIdlOzrunCtB2qq6FrhtPbo+PlbvRbyi86dr5VQx61eg/daQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
`;

hexo.extend.injector.register('head_begin', smooth_scroll, 'home');
