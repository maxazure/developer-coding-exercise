# Recat Client for Media Suite Blog

DEMO: https://mediasuite.u.jayliu.co.nz/


## Getting Started

1. Install dependencies,

    ```bash
    yarn
    ```

2. Start the dev server,

    ```bash
    yarn start
    ```

Note: To make it easier to debug this code, the proxy address defaults to <https://mediasuite.u.jayliu.co.nz/api>, you can also change it to a local address.
Modify the content in the file .umirc.ts to the following

```javascript
  proxy: {
    '/api': {
      target: 'https://127.0.0.1:8000',
      changeOrigin: true,
      pathRewrite: { '^/api': '' },
    },
  },
```
