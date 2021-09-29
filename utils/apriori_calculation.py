def apriori_calculation(input, class1, class2):
    """calculate the a priori probability of a signal

    Args:
        input ([Number]): the emitted signal
        class1 (Number): the first threshold
        class2 (Number): the second threshold

    Returns:
        [Number]: the two probabilities
    """
    p1 = sum((input == class1)) / len(input)
    p2 = 1 - p1
    return p1, p2