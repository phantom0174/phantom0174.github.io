const inject_code = `
<p class="toc-title">Contents</p>
<%- toc(page.content, {
    list_number: false,
    max_depth: 3
}) %>
`;

hexo.extend.filter.register('theme_inject', function (injects) {
    injects.postMarkdownBegin.raw('custom-toc', inject_code);
});
