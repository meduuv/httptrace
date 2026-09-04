# Design

HTTPTrace keeps transport inspection in a small core module and leaves formatting to the CLI. Requests use explicit timeouts and a descriptive user agent.
