import numpy as np

def detect_flares(
    flux,
    threshold=2
):

    mean_flux = np.mean(
        flux
    )

    std_flux = np.std(
        flux
    )

    flare_index = np.where(
        flux >
        mean_flux +
        threshold * std_flux
    )[0]

    return flare_index
