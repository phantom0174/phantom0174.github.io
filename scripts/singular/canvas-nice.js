const code = `
<script defer type="text/javascript" src="https://cdn.jsdelivr.net/npm/canvas-nice.js/dist/canvas-nice.min.js"></script>
<script defer type="text/javascript" src="/js/main.js"></script>
`;

hexo.extend.injector.register('body_end', code, 'home');
