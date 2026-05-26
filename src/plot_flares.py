import matplotlib.pyplot as plt

def plot_flares(
    time,
    flux,
    flare_index
):

    plt.figure(
        figsize=(12,5)
    )

    plt.plot(
        time,
        flux
    )

    plt.scatter(
        time[flare_index],
        flux[flare_index]
    )

    plt.xlabel(
        "Time"
    )

    plt.ylabel(
        "Flux"
    )

    plt.title(
        "Detected Stellar Flares"
    )

    plt.tight_layout()

    plt.savefig(
        "flare_detection.png",
        dpi=300
    )

    plt.show()
