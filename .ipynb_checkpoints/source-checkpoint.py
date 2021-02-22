import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits
import healpy as hp
import astropy.io.fits as fits

class source(object):
    def __init__(self,source_type,region):
        topdir = '/global/cscratch1/sd/ajross/tarcat/vtest/tv0.50.0/'
        if source_type=='ELG':
            dat = fits.getdata(topdir+'ELGtargetsDR9v0.49.0_masked.fits')
            random = fits.getdata(topdir+'randomsDR9v0.49.0_0_masked.fits')
        elif source_type=='LRG':
            dat = fits.getdata(topdir+'LRG_IRsv1targetsDR9v0.50.0_masked.fits')
            random = fits.getdata(topdir+'LRG_IRsv1targetsDR9v0.50.0_masked.fits')
        if region == 'BassMzls':
            sel_dat = (dat['PHOTSYS']=='N')
            sel_ran = (random['PHOTSYS']=='N')
        elif region == 'DS':
            sel_dat = self.sel_reg(dat['ra'],dat['dec'],'DS')
            sel_ran = self.sel_reg(random['ra'],random['dec'],'DS')
        elif region == 'DN':
            sel_dat = self.sel_reg(dat['ra'],dat['dec'],'DN')
            sel_ran = self.sel_reg(random['ra'],random['dec'],'DN')
        elif region == 'all':
            sel_dat = np.ones(len(dat),dtype=np.bool)
            sel_ran = np.ones(len(random),dtype=np.bool)
        self.data = dat[sel_dat]
        self.random = random[sel_ran]
    def sel_reg(self,ra,dec,reg):
        wra = (ra > 100-dec)
        wra &= (ra < 280 +dec)
        if reg == 'DN':
            w = dec < 32.375
            w &= wra
        if reg == 'DS':
            w = ~wra
            w &= dec > -25
        return w