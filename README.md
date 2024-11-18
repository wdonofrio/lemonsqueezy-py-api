# LemonSqueezy Py API

LemonSqueezy Py API is an unofficial Python library for interacting with the LemonSqueezy API. It provides a simple and intuitive interface for managing license keys, checkouts, webhooks, usage records, discounts, and more.

Interested in this project? Leave a ⭐️ or watch the repo to stay informed in our progress!

## Features

- List, create, retrieve, update, and delete license keys
- Manage checkouts and webhooks
- Create and list usage records
- Create, retrieve, and delete discounts
- Validate and manage license keys

## Installation

You can install LemonSqueezy using pip:

```sh
pip install lemonsqueezy
```

## Usage

Import APIs function and use them directly in your application!

```python
from lemonsqueezy.api import customer, store

store_data = store.get_store(1)
customer_data = customer.get_customer(1)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on Github.
See [CONTRIBUTING](CONTRIBUTING.md) for details.

This project is licensed under the MIT License. See the [LICENSE](LICENSE) for details.
