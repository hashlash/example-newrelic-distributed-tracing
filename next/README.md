# Pingpong Next

## Setup

- Install the dependencies

  ```
  yarn install
  ```

- Add your [license key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#license-key)
  to the [newrelic.js](newrelic.js).

  ```js
  exports.config = {
    ...
    /**
     * Your New Relic license key.
     */
    license_key: 'license key here',
    ...
  }
  ```

- Run the development server, and make sure that the APM Service has been created in your
  https://one.newrelic.com.

  ```
  yarn dev
  ```

- Create the New Relic browser app using [New Relic APM](https://docs.newrelic.com/docs/browser/browser-monitoring/installation/install-browser-monitoring-agent/#copy-paste-app)
  method.

- Open http://localhost:3000 with your browser to see the result.
