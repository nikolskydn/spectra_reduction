# Spectra Reduction


[![Platform](https://img.shields.io/badge/platform-Linux,%20OS%20X,%20Windows-green.svg?style=flat)](https://github.com/nikolskydn)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg?style=flat)](https://opensource.org/licenses/mit-license.php)


## Install

For install `spectra_reduction` perform commands:

 1. `./setup.py sdist` or `python3 setup.py sdist`

 2.  `cd dist` and `sudo python3 -m pip install spectra-reduction-X.Y.Z.tar.gz` 

## Programs list:

1. `view_spectra` Viewing raw spectra.

1. `reduce_spectra` Compression spectra.

1. `view_spectra_images3d` Viewing images.


## Usage

Illustrate by example.

From catalog `spectra-reduction` go to catalog with examples.

```cd ./examples/petrols```

## Result

The raw spectra of petrols are difficult to differ (see Figure 1).

![PetrolsSpectra](./doc/pspectra "Figure 1. Petrols Spectra.")

After compression by the algorithm HGSC we obtain a 3D image for petrols spectra (see Figure 2). The effect of clustering is well visible.

![HGSCImage](./doc/phgsc3d.png "Figure 2. HGSC Image.")
