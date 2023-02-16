const code = `
<script type="text/javascript"
    color="180,180,180"
    pointColor="180,180,180"
    opacity='1'
    zIndex="-1"
    count="50"
    src="//cdn.bootcss.com/canvas-nest.js/1.0.0/canvas-nest.min.js">
</script>
`;

hexo.extend.injector.register('body_end', code, 'home');
