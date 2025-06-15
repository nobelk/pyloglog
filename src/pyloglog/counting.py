from array import array
import math


def r(x: int) -> int:
    """Count the number of leading zeros in the binary representation of x."""
    return ~x & (x + 1)


# This module implements the LogLog and HyperLogLog algorithms for
# estimating the number of distinct elements in a stream.
def logLog_estimate(stream: array, M: int) -> int:
    """Estimate the number of distinct elements in a stream using the
    LogLog algorithm."""
    sketch = array(
        "i", [0] * M
    )  # Initialize an array to keep track of the maximum rank for each bucket
    for element in stream:
        # Hash the element to get a bucket index
        bucket_index = hash(element) % M
        # Count the number of leading zeros in the hash value
        sketch[bucket_index] = sketch[bucket_index] | r(element)

    total: int = 0
    for k in range(M):
        total += r(sketch[k])
    mean = 1.0 * total / M
    return int(
        M * math.pow(2, mean) / 0.77351
    )  # Return the estimated count as an integer


def hyperlogLog_estimate(stream: array, M: int) -> int:
    """
    Estimate the number of distinct elements in a stream using the HyperLogLog
    algorithm.

    Parameters:
    stream (array): An array of elements in the stream.
    M (int): The number of buckets to use for the HyperLogLog algorithm.

    Returns:
    int: The estimated number of distinct elements in the stream.

    """
    # Initialize an array to keep track of the maximum rank for each bucket
    buckets = [0] * M

    # Process each element in the stream
    for element in stream:
        # Hash the element to get a bucket index
        bucket_index = hash(element) % M
        # Count the number of leading zeros in the hash value
        leading_zeros = (hash(element) >> (bucket_index + 1)).bit_length()
        # Update the maximum rank for this bucket
        buckets[bucket_index] = max(buckets[bucket_index], leading_zeros)

    # Calculate the raw estimate using the HyperLogLog formula
    Z = 1.0 / sum(2**-b for b in buckets)

    # Apply bias correction and scaling factor
    E = M * (M**0.5) * Z

    return int(E)  # Return the estimated count as an integer
