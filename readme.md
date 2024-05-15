# Random Facts

This repository is a collection of random facts.

## Table of Contents

- [Installation](#installation)
- [How It Works](#HowItWorks)
- [Usage](#usage)
- [APIs Used](#apis-used)
- [Contributing](#contributing)
- [License](#license)

## How It Works

This project works by using two APIs to fetch and post random facts.

1. **Fetching Facts**: The project uses the API-Ninja API to fetch random facts. When the project runs, it makes a request to the API-Ninja API, which returns a random fact.

2. **Posting Facts**: After fetching the fact, the project uses the Twitter API to post this fact on Twitter. It sends a request to the Twitter API with the fact as the message body.

This process repeats, allowing the project to continuously fetch and post random facts.

Note: To use the Twitter API, you need to have a Twitter Developer account and API access. You'll use your API keys in the project to authenticate your requests.

## Installation

Clone this repository to your local machine to get started:

`git clone https://github.com/IamPiklu/Random-Facts-Using-X-API-.git`

## Usage

After cloning the repository, navigate to the directory and open the files to view the random facts.

## APIs Used

This project uses two APIs:

1. **API-Ninja**: This API is used to fetch random facts. You can find more about it [here](https://api-ninja.com).
2. **Twitter API**: This API is used to post the random facts on Twitter. To use the Twitter API, you need to create a Twitter Developer account and apply for API access. Once you have access, you'll receive API keys that you can use in your project. You can find more about it [here](https://developer.twitter.com).

## Contributing

Contributions are welcome! If you have a random fact to add, please follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b new-fact`
3. Commit your changes: `git commit -m 'Add a new fact'`
4. Push to the branch: `git push origin new-fact`
5. Open a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.