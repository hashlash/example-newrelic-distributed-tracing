# ping

## Setup

- (Optional) Use a virtual environment

  ```
  python3 -m venv env
  source env/bin/activate
  ```

- Install the dependencies

  ```
  pip install -r requirements.txt
  ```

- Add your [license key](https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#license-key)
  to the [newrelic.ini](newrelic.ini).

  ```ini
  # You must specify the license key associated with your New
  # Relic account. This may also be set using the NEW_RELIC_LICENSE_KEY
  # environment variable. This key binds the Python Agent's data to
  # your account in the New Relic service. For more information on
  # storing and generating license keys, see
  # https://docs.newrelic.com/docs/apis/intro-apis/new-relic-api-keys/#ingest-license-key
  license_key = *** REPLACE ME ***
  ```

- Run the app

  ```
  python3 ping.py
  ```

- The service would be accessible on http://localhost:5000/ping
