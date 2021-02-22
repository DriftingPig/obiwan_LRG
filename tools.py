import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits
import healpy as hp
import astropy.io.fits as fits

def flux2mag(flux,mwtransmission):
        mag= 22.5 - 2.5 * np.log10(flux / mwtransmission)
        return mag
    