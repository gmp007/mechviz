# MechViz - Python-based toolkit for analysis and visualization of mechanical properties of materials

**MechViz** is a standalone code for analyzing and visualizing the mechanical properties of crystal systems across different dimensions, including 3D structures, 2D materials, coaxially rolled 2D-based van der Waals nanostructures, and 1D nanotubes. **MechViz** is designed to be able to read in the elastic tensor matrices in Voigt notation (6 by 6 for 3D, 3 by 3 for 2D and 2 by 2 for 1D systems) from any electronic structure code, and them compute the elastic and mechanical properties, including thermal properties of materials. 


##  About MechViz

MechViz offers a flexible approach to determine and visualize the mechanical and related properties of various materials using the elastic constant tensor in Voigt notation from any electronic structure code.


## Capabilities

MechViz offers a comprehensive range of features for analyzing various mechanical and related properties of material. The essential ones are:

- **Young's Modulus**: Evaluates the material's stiffness under uniaxial stress.
- **Poisson Ratio**: Determines the ratio of transverse strain to axial strain.
- **Shear Modulus**: Assesses the material's response to shear stress.
- **Bulk Modulus (3D/1D), Stiffness Constant (2D)**: Measures volume change under pressure and in-plane stiffness, respectively.
- **Pugh Modulus Ratio**:  Provides insights into the material's ductility.
- **Layer Modulus (2D Materials)**: Evaluates in-plane elasticity of layers.
- **Sound Velocities**: Longitudinal, transverse, and average sound velocities.
- **Debye Speed**: Estimates phonon propagation speeds.
- **Linear Compressibility**: Assesses the material's response to linear compressive stress.
- **Debye Temperature**: Evaluates the material's thermal properties.
- **Minimum Thermal Conductivity**: Utilizes Clarke and Cahill equations to estimate thermal conductivity limits.
- **Hardness Estimation**: Employs various empirical equations to predict Vickers hardness.
- **Fracture Toughness Analysis**: Evaluates the material's resistance to crack propagation.
- **Elastic Anisotropy**: Examines directional variations in material properties.
- **and so on**


## MechViz: Advanced Data Visualization and Analysis Toolkit

MechViz has built in visualization capabilities for both spatial and contour plots rendering of key mechanical proerties. It is integrated with the Elate web interface. 


## Installation

MechViz offers straightforward installation options suitable for various user preferences. These methods ensure a hassle-free setup, allowing you to commence your material science investigations with ElasTool promptly. Detailed instructions can be found in the INSTALL file, but here are the general methods:

1. **Using pip**:
   - Quickly install ElasTool with pip by executing: 
     ```
     pip install -U elastool
     ```

2. **From Source Code**:
   - Alternatively, download the source code with:
     ```
     git clone [git@github.com:gmp007/MechViz.git]
     ```
   - Then, install ElasTool by navigating to the master directory and running:
     ```
     pip install .
     ```

3. **Installation via setup.py**:
   - As an alternative, ElasTool can be installed using the `setup.py` script:
     ```
     python setup.py install [--prefix=/path/to/install/]
     ```
   - The optional `--prefix` argument is useful for installations in environments like shared High-Performance Computing (HPC) systems, where administrative privileges might be restricted.
   - Please note that while this method remains supported, its usage is gradually declining in favor of more modern installation practices. It is recommended primarily for specific scenarios where standard installation methods like `pip` are not applicable.


## Running MechViz

Running MechViz is easy. Here are the key steps for using ElasTool effectively:

1. **Create a Calculation Directory**:
   - Start by creating a directory for your calculations.
       - Required files:
	  - `massdensity_dim.dat` for material's dimension and mass density. You do not necessarily need to specify the mass density as it will compute it automatically, but you must specify the dimensionality
	    ```
	    # Mass density in Kg/m^2, Dimension
	    0.00000224 2D
	    ```
	  - `elastic_tensor.dat` for the elastic tensor matrix. This is 6 by 6 for 3D, and 3 by 3 for 2D
	    ```
	    # Elastic tensor in Voigt notation for 2D material
	    52.2849 28.6494 0.0000
	    28.6494 36.5780 0.0000
	    0.0000 0.0000 22.8516
	    ```
	  - `structure file`  for the crystal structure of your system in either .cif or .vasp extension, but not both at the same time. MechViz will automatically detect and read the structure information   
    
2. **Initialize a Calculation**:
   - Execute `mechviz` to begin the calculation process.

3. ***Optional Arguments**
   - Execute `MechViz` with any of the following optional arguments, all or one at a time, in no particular order
	  - `plot` to plot the mechanical and related properties for visualization
	  - `-plotly` to interact with some of the properties on the web browser using the powerful plotly program
	  - `-elate` to automically plot the mechanical properties on the web browser of your chosen leveraging the Elate program

## Citing MechViz

The MechViz architecture is derived from our ElasTool toolkit. If you have used MechViz in your research, please cite the following:
  - [MechViz: Analysis and visualization toolkit of mechanical properties of materials](Under review) - C.E. Ekuma and Z.L. Liu 2024
  - [MechViz - Python-based toolkit for analysis and visualization of mechanical properties of materials](https://github.com/gmp007/mechviz) - C.E. Ekuma


Additionally, please cite original papers of ElasTool as described below:

### Main ElasTool Implementation
- Please cite for ElasTool's primary implementation:
  - [ElasTool: An automated toolkit for elastic constants calculation](https://doi.org/10.1016/j.cpc.2021.108180) - Liu et al., 2022

@article{Liu2020elastool,
  title = {ElasTool: An automated toolkit for elastic constants calculation},
  journal = {Computer Physics Communications},
  volume = {270},
  pages = {108180},
  year = {2022},
  issn = {0010-4655},
  doi = {https://doi.org/10.1016/j.cpc.2021.108180},
  url = {https://www.sciencedirect.com/science/article/pii/S0010465521002927},
  author = {Zhong-Li Liu and C.E. Ekuma and Wei-Qi Li and Jian-Qun Yang and Xing-Ji Li}
}

  - [Efficient prediction of temperature-dependent elastic and mechanical properties of 2D materials](https://www.nature.com/articles/s41598-022-07819-8) - Kastuar et al., 2022
  
@article{Kastuar2022efficient,
  title={Efficient prediction of temperature-dependent elastic and mechanical properties of 2D materials},
  author={Kastuar, SM and Ekuma, CE and Liu, Z-L},
  journal={Scientific Reports},
  volume={12},
  number={1},
  pages={3776},
  year={2022},
  url = {https://www.nature.com/articles/s41598-022-07819-8},
  publisher={Nature Publishing Group UK London}
}

  - [Elastool V2.0: An Automated Toolkit for Elastic and Mechanical Properties of Tubular 2D-Based Nanostructures and Nanotubes](#) - Ekuma and Liu (under review)

@article{Ekuma2023,
  title = {Elastool V2.0: An Automated Toolkit for Elastic and Mechanical Properties of Tubular 2D-Based Nanostructures and Nanotubes},
  journal = {Computer Physics Communications},
  volume = {xx},
  pages = {xx},
  year = {2024},
  issn = {xxx},
  doi = {xx},
  url = {xx},
  author = {Chinedu E. Ekuma and Zhong-Li Liu }
}

### Work Related to 2D Materials
- For work specifically on 2D materials, refer to:
  - [Efficient prediction of temperature-dependent elastic and mechanical properties of 2D materials](https://www.nature.com/articles/s41598-022-06650-1) - Kastuar et al., 2022

### Work Related to Tubular 2D-Based Nanostructures and Nanotubes
- For studies on tubular 2D-based nanostructures and nanotubes, cite:
  - [Elastool V2.0: An Automated Toolkit for Elastic and Mechanical Properties of Tubular 2D-Based Nanostructures and Nanotubes](#) - Ekuma and Liu (under review)

### Other Related Works
- For related research, cite:
  - [Calculations of single-crystal elastic constants made simple](https://doi.org/10.1016/j.cpc.2009.11.017) - Yu et al., 2010
  - [Mechanical properties and hardness of boron pnicogens BX](https://doi.org/10.1016/j.mtla.2020.100904) - Ekuma and Liu, 2020


## Contact Information

We welcome your interest in extending MechViz capabilities and are happy to assist with integrating it with other electronic structure codes. If you have queries about MechViz, need help using it, or wish to share suggestions for its improvement, please reach out to us.

Feel free to contact us via email:
- [cekuma1@gmail.com](mailto:cekuma1@gmail.com)

Your feedback and questions are invaluable to us, and we look forward to hearing from you.
