// set disqus recommendations element
const recom_element  = `
<div id="disqus_recommendations"></div>
`;
hexo.extend.filter.register('theme_inject', function (injects) {
    // weight of comments is 99 
    // source: ./themes/fluid/scripts/filters/default-injects.js
    injects.postComments.raw('disqus-reco', recom_element, '', '', -200);
});


// disqus-recommend scripts
const recom_script = `
<script> 
    (function() {
    var d = document, s = d.createElement('script');
    s.src = 'https://quantamis-realm.disqus.com/recommendations.js'; s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
`;
hexo.extend.injector.register('body_end', recom_script, 'post');
