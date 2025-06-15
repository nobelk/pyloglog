import random
from array import array

from src.pyloglog.counting import hyperlogLog_estimate, logLog_estimate


def test_loglog_estimate():
    """Test the logLog_estimate function."""
    import random
    from array import array

    # Generate a random stream of integers
    stream = array("i", [random.randint(1, 1000) for _ in range(10000)])
    M = 16  # Number of buckets

    # Call the logLog_estimate function
    estimate = logLog_estimate(stream, M)

    # Check if the estimate is within a reasonable range
    assert estimate > 0, "Estimate should be greater than 0"
    assert estimate < 20000, "Estimate should be less than 20000"


def test_hyperloglog_estimate():
    """Test the hyperlogLog_estimate function."""
    # Generate a random stream of integers
    stream = array("i", [random.randint(1, 1000) for _ in range(10000)])
    M = 16  # Number of buckets

    # Call the hyperlogLog_estimate function
    estimate = hyperlogLog_estimate(stream, M)

    # Check if the estimate is within a reasonable range
    assert estimate > 0, "Estimate should be greater than 0"
    assert estimate < 20000, "Estimate should be less than 20000"
