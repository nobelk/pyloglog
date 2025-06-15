# pyloglog
Cardinality estimation using loglog algorithm

[Reference](https://sedgewick.io/wp-content/uploads/2022/03/2016-19Cardinality.pdf)

# Practical Applications
- In a given stream of data values, how many different values are present?
- Reference application. How many unique visitors in a web log?

# Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management. To install dependencies, run:

```bash
poetry install
```

# Usage

You can use the LogLog algorithm implementation in your Python code by importing from the `pyloglog` package. See `src/pyloglog/counting.py` for details.

## Building and Running 
To run the example code, you can execute the following command:

```bash
make build
```

## Running Tests

To run the test suite, use:

```bash
poetry run pytest
```

This will discover and run all tests in the `tests/` directory.


# LogLog Algorithm Explanation

The LogLog algorithm is a probabilistic algorithm for cardinality estimation, i.e., estimating the number of distinct elements in a large dataset or stream. It is especially useful when the dataset is too large to fit in memory.

## How It Works
- The algorithm hashes each element in the stream to a uniformly random value.
- It keeps track of the maximum number of leading zeros observed in the binary representation of the hash values.
- The number of leading zeros is used to estimate the cardinality, based on the intuition that the probability of seeing a hash with many leading zeros decreases exponentially with the number of zeros.
- The final estimate is computed using a mathematical formula involving the observed maximum and a correction factor.

## References
- Durand, M., & Flajolet, P. (2003). LogLog Counting of Large Cardinalities. In Algorithms - ESA 2003 (pp. 605–617). Springer. [PDF](https://sedgewick.io/wp-content/uploads/2022/03/2016-19Cardinality.pdf)
- [Wikipedia: LogLog algorithm](https://en.wikipedia.org/wiki/LogLog_counting)

# License
See [LICENSE](LICENSE) for details.
