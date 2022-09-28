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

- Run the development server:

  ```
  yarn dev
  ```

- Open http://localhost:3000 with your browser to see the result.
