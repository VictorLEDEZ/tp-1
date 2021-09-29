from scipy import stats as stats

def map_mpm_2(input, class1, class2, p1, p2, mu1, sigma1, mu2, sigma2):
    probability_Y1 = stats.norm.pdf(input, mu1, sigma1)
    probability_Y2 = stats.norm.pdf(input, mu2, sigma2)
    return class1 * (p1 * probability_Y1 > p2 * probability_Y2) + class2 * (p1 * probability_Y1 < p2 * probability_Y2)
