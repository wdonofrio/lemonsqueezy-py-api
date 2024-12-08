# LemonSqueezy Py API

An unofficial Python SDK for the LemonSqueezy API. Simplify your integration with LemonSqueezy's platform to manage license keys, checkouts, webhooks, usage records, discounts, and more.

[![Leave a star](https://img.shields.io/github/stars/wdonofrio/lemonsqueezy-py-api?style=social)](https://github.com/wdonofrio/lemonsqueezy-py-api)

## Features

- 🔑 License Key Management
- 💳 Checkout & Payment Processing
- 🔔 Webhook Integration
- 📊 Usage Tracking
- 🏷️ Discount Management
- 🏪 Store & Product Management
- 👥 Customer Data Access
- 📦 Digital File Management

## Installation

```sh
pip install lemonsqueezy
```

## Quick Start

Initialize the client with your API key:

```python
from lemonsqueezy import LemonSqueezy

client = LemonSqueezy(api_key="your_api_key")
```

### Examples

```python
# List all your stores
stores = client.list_stores()

# Get customer information
customers = client.list_customers()

# Manage products
product = client.get_product(123)
all_products = client.list_products()
product_variants = client.get_product_variants(123)

# Handle digital files
file = client.get_file(456)
all_files = client.list_files()

# Work with variants
variant = client.get_variant(789)
all_variants = client.list_variants()
```

## Configuration

You can configure the client using environment variables:

```env
LEMONSQUEEZY_API_KEY=your_api_key
LEMONSQUEEZY_API_URL=https://api.lemonsqueezy.com/v1  # Optional
```

Or pass configuration directly to the client:

```python
client = LemonSqueezy(
    api_key="your_api_key",
    api_url="https://api.lemonsqueezy.com/v1"  # Optional
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING](CONTRIBUTING.md) for more details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 🌟 Star this repo to show your support
- 🐛 Open an issue to report bugs
- 💡 Open an issue to request features
- 📖 Documentation coming soon!
