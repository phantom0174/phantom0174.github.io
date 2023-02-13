/* global hexo */

'use strict';

const urlJoin = require('../utils/url-join');

// customized code
hexo.extend.helper.register('css_ex', function(base, relative, ex = '') {
  return `<link ${ex} rel="preload" href="${this.url_for(urlJoin(base, relative))}" as="style" onload="this.onload=null;this.rel='stylesheet'"/>`;
});

// <link rel="preload" href="style.css" as="style" onload="this.onload=null;this.rel='stylesheet'"></link>

hexo.extend.helper.register('js_ex', function(base, relative, ex = '') {
  return `<script ${ex} src="${this.url_for(urlJoin(base, relative))}" ></script>`;
});

hexo.extend.helper.register('url_join', function(base, relative) {
  return this.url_for(urlJoin(base, relative));
});
