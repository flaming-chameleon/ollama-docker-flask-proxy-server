

[![Watch the video](https://img.youtube.com/vi/pbOZE2KkNuw/maxresdefault.jpg)](https://youtu.be/pbOZE2KkNuw)


# Ollama Docker-Flask Proxy Server

This repository contains the implementation of a Flask-based proxy server designed to interface with an AI service. The proxy server is set up to forward requests to the AI service, handling GET, POST, PUT, and DELETE methods.

## Features

- **Dynamic URL Routing:** Routes all requests dynamically based on the path provided in the request URL.
- **Environment Variable Configuration:** Utilizes environment variables to configure the AI service URL, with a default fallback.
- **Request Forwarding:** Forwards headers, data, and cookies from the incoming request to the AI service.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:

```bash
git clone https://github.com/flaming-chameleon/ollama-docker-flask-proxy-server.git
cd ollama-docker-flask-proxy-server
```

### Installing

A step by step series of examples that tell you how to get a development environment running:

1. **Build the Docker Containers:**
   ```bash
   docker-compose up --build
   ```

2. **Run the Flask Application:**
   ```bash
   docker-compose up
   ```

The application will be available at `http://localhost:5000`.

## Usage

Direct all API requests to the proxy server, which will forward them to the configured AI service.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/flaming-chameleon/ollama-docker-flask-proxy-server/tags).

## Authors

- **Your Name** - *Initial work* - [Flaming Chameleon](https://github.com/flaming-chameleon)

See also the list of [contributors](https://github.com/flaming-chameleon/ollama-docker-flask-proxy-server/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Hat tip to anyone whose code was used
- Inspiration
- etc

[![Watch the video](https://img.youtube.com/vi/pbOZE2KkNuw/maxresdefault.jpg)](https://youtu.be/pbOZE2KkNuw)
