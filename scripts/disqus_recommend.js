let inject_code = `
<div id="disqus_recommendations"></div>
`;

hexo.extend.filter.register('theme_inject', function (injects) {
    // weight of comments is 99 
    // source: ./themes/fluid/scripts/filters/default-injects.js
    injects.postComments.raw('disqus-reco', inject_code, '', '', -200);
});


inject_code = `
<script> 
    (function() {
    var d = document, s = d.createElement('script');
    s.src = 'https://quantamis-realm.disqus.com/recommendations.js'; s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
`;

hexo.extend.injector.register('body_end', inject_code, 'post');
