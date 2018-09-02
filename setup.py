#!/usr/bin/python3
from setuptools import setup

setup(name='spectra_reduction', version='0.0.0', 
      packages=['spectra_reduction'],
      description='Module for reducing the dimensionality of spectral data.',
      author='Nikolskii D. N.', author_email='nikolskydn@mail.ru',
      entry_points={'console_scripts':
                    ['reduce_spectra=spectra_reduction.reduce:main',
                     'view_spectra=spectra_reduction.view_spectra:main',
                     'view_spectra_images3d=spectra_reduction.view_spectra_images3d:main']}
)

