GP software
Version 0.131		Saturday 11 Oct 2008 at 20:59

The GP toolbox is an implementation of the GPs that uses the Pseudo-Input method of Snelson and Ghahramani (NIPS 2005) for sparsification as well as extensions given by Quinonero-Candela and Rasmussen (JMLR 2005).

Version 0.131
-------------

Changes to allow compatibility with SGPLVM and NCCA toolboxes.

Version 0.13
------------

Changes to allow more flexibility in optimisation of beta.

Version 0.12
------------

Various minor changes for enabling back constraints in hierarchical
GP-LVM models.

Version 0.11
------------

Changes include the use of the optimiDefaultConstraint('positive') to
obtain the function to constrain beta to be positive (which now
returns 'exp' rather than 'negLogLogit' which was previously the
default). Similarly default optimiser is now given by a command in
optimiDefaultOptimiser.

Version 0.1
-----------

The first version which is spun out of the FGPLVM toolbox. The
corresponding FGPLVM toolbox is 0.15.


MATLAB Files
------------

Matlab files associated with the toolbox are:

gpReconstruct.m: Reconstruct an GP form component parts.
gpPosteriorGradMeanCovar.m: Gadient of the mean and variances of the posterior at points given by X.
gpDisplay.m: Display a Gaussian process model.
gpReadFromFile.m: Load a file produced by the C++ implementation.
gpScaleBiasGradient.m: Compute the log likelihood gradient wrt the scales.
gpOptions.m: Return default options for GP model.
gpUpdateKernels.m: Update the kernels that are needed.
gpComputeAlpha.m: Update the vector `alpha' for computing posterior mean quickly.
gpCovGrads.m: Sparse objective function gradients wrt Covariance functions for inducing variables.
gpToolboxes.m: Load in the relevant toolboxes for GP.
gpBlockIndices.m: Return indices of given block.
gpLogLikelihood.m: Compute the log likelihood of a GP.
demSpgp1d1.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpMeanFunctionGradient.m: Compute the log likelihood gradient wrt the scales.
gpTest.m: Test the gradients of the gpCovGrads function and the gp models.
gpOut.m: Evaluate the output of an Gaussian process model.
gpSubspaceExtractParam.m:
gpPosteriorMeanCovar.m: Mean and covariances of the posterior at points given by X.
gpOptimise.m: Optimise the inducing variable based kernel.
gpPosteriorGradMeanVar.m: Gadient of the mean and variances of the posterior at points given by X.
demSpgp1d2.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpCreate.m: Create a GP model with inducing varibles/pseudo-inputs.
gpWriteToFile.m: Write a file to be read by the C++ implementation.
gpSubspaceOut.m:
gpSubspaceOptimise.m:
gpSubspaceCreate.m: 
demSpgp1dPlot.m: Plot results from 1-D sparse GP.
gpDataIndices.m: Return indices of present data.
gpPosteriorMeanCovarTest.m: Test the gradients of the mean and covariance.
gpExtractParam.m: Extract a parameter vector from a GP model.
gpPosteriorMeanVar.m: Mean and variances of the posterior at points given by X.
gpPointLogLikelihood.m: Log-likelihood of a test point for a GP.
gpExpandParam.m: Expand a parameter vector into a GP model.
gpUpdateAD.m: Update the representations of A and D associated with the model.
demSpgp1d3.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpDeconstruct.m: break GP in pieces for saving.
gpObjectiveGradient.m: Wrapper function for GP objective and gradient.
gpReadFromFID.m: Load from a FID produced by the C++ implementation.
gpCovGradsTest.m: Test the gradients of the likelihood wrt the covariance.
demSpgp1d4.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpObjective.m: Wrapper function for GP objective.
gpComputeM.m: Compute the matrix m given the model.
gpGradient.m: Gradient wrapper for a GP model.
gpLogLikeGradients.m: Compute the gradients for the parameters and X.
gpSubspaceExpandParam.m: 
