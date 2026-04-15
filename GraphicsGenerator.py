import matplotlib.pyplot as plt
import seaborn as sns

class GraphicsGenerator:
    @staticmethod
    def plot_histogram(data):
        plt.hist(data)
        plt.show()

    @staticmethod
    def plot_boxplot(data):
        sns.boxplot(data=data)
        plt.show()

    @staticmethod
    def plot_individual_values(data):
        plt.plot(data, 'o')
        plt.show()

    @staticmethod
    def plot_probability(data):
        stats.probplot(data, dist="norm", plot=plt)
        plt.show()

# Function to generate all 4 plots...
