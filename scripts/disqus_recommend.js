const inject_code = `
<script> 
    (function() {
    var d = document, s = d.createElement('script');
    s.src = 'https://quantamis-realm.disqus.com/recommendations.js'; s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
`;

hexo.extend.injector.register('body_end', inject_code, 'post');
