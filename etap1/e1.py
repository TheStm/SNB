
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as stats
if __name__ == '__main__':

    df = pd.read_csv("breast_cancer_wisconsin/data.csv")

    df.hist( column='radius_mean', bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu radius_mean')
    plt.show()

    df.hist(column="texture_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu texture_mean')
    plt.show()

    df.hist(column="perimeter_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu perimeter_mean')
    plt.show()

    df.hist(column="area_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu area_mean')
    plt.show()

    df.hist(column="smoothness_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu smoothness_mean')
    plt.show()

    df.hist(column="compactness_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu compactness_mean')
    plt.show()

    df.hist(column="concavity_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu concavity_mean')
    plt.show()

    df.hist(column="concave points_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu concave points_mean')
    plt.show()

    df.hist(column="symmetry_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu symetry_mean')
    plt.show()

    df.hist(column="fractal_dimension_mean", bins=100)
    plt.xlabel('Wartości')
    plt.ylabel('Liczba wystąpień')
    plt.title('Histogram atrybutu fractal_dimension_mean')
    plt.show()
