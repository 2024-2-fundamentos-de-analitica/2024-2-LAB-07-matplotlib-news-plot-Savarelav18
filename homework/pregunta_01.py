"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd
import matplotlib.pyplot as plt
import os


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """
    input_file = "files/input/news.csv"
    output_file = "files/plots"
    df = load_data(input_file)
    graficar(df, output_file)


def load_data(input_file):

    df = pd.read_csv(input_file, sep=",", index_col=0)

    return df


def graficar(dataframe, output_file):

    colors = {
        "Television": "dimgray",
        "Newspaper": "grey",
        "Internet": "tab:blue",
        "Radio": "lightgrey",
    }

    zorder = {
        "Television": 1,
        "Newspaper": 1,
        "Internet": 2,
        "Radio": 1,
    }

    linewidths = {
        "Television": 2,
        "Newspaper": 2,
        "Internet": 3,
        "Radio": 2,
    }

    for col in dataframe.columns:
        plt.plot(
            dataframe[col],
            label=col,
            color=colors[col],
            zorder=zorder[col],
            linewidth=linewidths[col],
        )
    plt.title("How people get their news", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    for col in dataframe.columns:
        first_year = dataframe.index[0]
        plt.scatter(
            x=first_year,
            y=dataframe[col][first_year],
            color=colors[col],
            zorder=zorder[col],
        )
        plt.text(
            first_year - 0.2,
            dataframe[col][first_year],
            col + " " + str(dataframe[col][first_year]) + "%",
            ha="right",
            va="center",
            color=colors[col],
        )

        last_year = dataframe.index[-1]
        plt.scatter(
            x=last_year,
            y=dataframe[col][last_year],
            color=colors[col],
            zorder=zorder[col],
        )

        plt.text(
            last_year + 0.2,
            dataframe[col][last_year],
            col + " " + str(dataframe[col][last_year]) + "%",
            ha="left",
            va="center",
            color=colors[col],
        )

    plt.xticks(ticks=dataframe.index, label=dataframe.index, ha="center")

    plt.tight_layout()
    if not os.path.exists(output_file):
        os.makedirs(output_file)
        plt.savefig(f"{output_file}/news.png")
    plt.show()


if "__main__" in __name__:
    pregunta_01()
