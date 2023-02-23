const code = `
<script type="text/javascript" src="/js/canvas-nice.min.js"></script>
<script type="text/javascript" src="/js/main.js"></script>
`;

hexo.extend.injector.register('body_end', code, 'home');
