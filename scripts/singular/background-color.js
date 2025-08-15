const disable_color_transition_animation = `
<style>
    body { transition: none !important; }
</style>
`;
hexo.extend.injector.register('body_end', disable_color_transition_animation, 'default');
