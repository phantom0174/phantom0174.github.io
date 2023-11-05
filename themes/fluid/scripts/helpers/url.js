/* global hexo */

'use strict';

const urlJoin = require('../utils/url-join');

// CUSTOMIZED code
hexo.extend.helper.register('css_ex', function (base, relative, ex = '') {
  return `<link ${ex} rel="preload" href="${this.url_for(urlJoin(base, relative))}" as="style" onload="this.onload=null;this.rel='stylesheet'"/>`;
});

hexo.extend.helper.register('js_ex', function (base, relative, ex = '') {
  return `<script ${ex} src="${this.url_for(urlJoin(base, relative))}" ></script>`;
});

hexo.extend.helper.register('url_join', function (base, relative) {
  return this.url_for(urlJoin(base, relative));
});
