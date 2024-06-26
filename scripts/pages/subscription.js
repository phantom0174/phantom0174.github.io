hexo.extend.filter.register('theme_inject', function (injects) {
  injects.pageComments.file('subscription-form', 'source/subscription/content.html', {}, { cache: true }, -1);
});
