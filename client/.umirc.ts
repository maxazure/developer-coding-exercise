import { defineConfig } from 'umi';

export default defineConfig({
  nodeModulesTransform: {
    type: 'none',
  },
  routes: [
    { path: '/', component: '@/pages/index' },
    { path: '/posts/:url', component: '@/pages/posts' },
  ],
  fastRefresh: {},

  // Proxy handle with cos-domain https://mediasuite.u.jayliu.co.nz/
  proxy: {
    '/api': {
      target: 'https://mediasuite.u.jayliu.co.nz/api',
      changeOrigin: true,
      pathRewrite: { '^/api': '' },
    },
  },
});
