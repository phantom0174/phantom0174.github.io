const inject_code = `
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

hexo.extend.injector.register('head_end', inject_code, 'post');
