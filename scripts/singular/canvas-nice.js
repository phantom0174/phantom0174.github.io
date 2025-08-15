const code = `
<script defer type="text/javascript" src="https://cdn.jsdelivr.net/npm/canvas-nice.js@1.0.4/dist/canvas-nice.min.js"></script>
<script defer type="text/javascript" src="/js/background-animation.js"></script>
`;
hexo.extend.injector.register('body_end', code, 'home');
