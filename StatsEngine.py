import scipy.stats as stats

class StatsEngine:
    @staticmethod
    def one_sample_t(data, mu):
        return stats.ttest_1samp(data, mu)

    @staticmethod
    def two_sample_t(data1, data2):
        return stats.ttest_ind(data1, data2)

    @staticmethod
    def paired_t(data1, data2):
        return stats.ttest_rel(data1, data2)

    # Additional statistical functions... 

    @staticmethod
    def mann_whitney_u(data1, data2):
        return stats.mannwhitneyu(data1, data2)

    @staticmethod
    def chi_square(observed):
        return stats.chi2_contingency(observed)

    # Diagnostics methods like Shapiro-Wilk and Levene's test...
