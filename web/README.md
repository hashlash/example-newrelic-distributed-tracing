# web

## Setup

- Create New Relic browser app using [Copy/Paste Javascript code](https://docs.newrelic.com/docs/browser/browser-monitoring/installation/install-browser-monitoring-agent/#select-apm-app)
  method.

- Enable [Distributed Tracing](https://docs.newrelic.com/docs/browser/new-relic-browser/browser-pro-features/browser-data-distributed-tracing/#enable),
  [CORS](https://docs.newrelic.com/docs/browser/new-relic-browser/browser-pro-features/browser-data-distributed-tracing/#cors),
  and add `http://127.0.0.1:5000` as an approved cross-origin resource.

- Put the generated [JavaScript snippet](https://docs.newrelic.com/docs/browser/browser-monitoring/installation/install-browser-monitoring-agent/)
  inside the [`newrelic-browser.js`](newrelic-browser.js) (don't include the `<script>` tag from the beginning and the end of the Javascript snippet).

  ```js
  <script type="text/javascript">
  // script from newrelic console
  </script>
  ```

- Serve the file using any file server. With python, you could do:

  ```
  python3 -m http.server
  ```
