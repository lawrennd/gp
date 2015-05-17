GP software
Version 0.11		Saturday 13 Jan 2007 at 01:20
Copyright (c) 2007 Neil D. Lawrence

The GP toolbox is an implementation of the GPs that uses the Pseudo-Input method of Snelson and Ghahramani (NIPS 2005) for sparsification as well as extensions given by Quinonero-Candela and Rasmussen (JMLR 2005).

Version 0.11
------------

Changes include the use of the optimiDefaultConstraint('positive') to obtain the function to constrain beta to be positive (which now returns 'exp' rather than 'negLogLogit' which was previously the default). Similarly default optimiser is now given by a command in optimiDefaultOptimiser.

Version 0.1
-----------

The first version which is spun out of the FGPLVM toolbox. The corresponding FGPLVM toolbox is 0.15. 

MATLAB Files
------------

Matlab files associated with the toolbox are:

demSpgp1d1.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1d2.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1d3.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1d4.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1dPlot.m: Plot results from 1-D sparse GP.
gpBlockIndices.m: Return indices of given block.
gpComputeAlpha.m: Update the vector `alpha' for computing posterior mean quickly.
gpComputeM.m: Compute the matrix m given the model.
gpCovGrads.m: Sparse objective function gradients wrt Covariance functions for inducing variables.
gpCovGradsTest.m: Test the gradients of the likelihood wrt the covariance.
gpCreate.m: Create a GP model with inducing varibles/pseudo-inputs.
gpDataIndices.m: Return indices of present data.
gpDisplay.m: Display a Gaussian process model.
gpExpandParam.m: Expand a parameter vector into a GP model.
gpExtractParam.m: Extract a parameter vector from a GP model.
gpGradient.m: Gradient wrapper for a GP model.
gpLogLikeGradients.m: Compute the gradients for the parameters and X.
gpLogLikelihood.m: Compute the log likelihood of a GP.
gpMeanFunctionGradient.m: Compute the log likelihood gradient wrt the scales.
gpObjective.m: Wrapper function for GP objective.
gpObjectiveGradient.m: Wrapper function for GP objective and gradient.
gpOptimise.m: Optimise the inducing variable based kernel.
gpOptions.m: Return default options for GP model.
gpOut.m: Evaluate the output of an Gaussian process model.
gpPointLogLikelihood.m: Log-likelihood of a test point for a GP.
gpPosteriorGradMeanCovar.m: Gadient of the mean and variances of the posterior at points given by X.
gpPosteriorGradMeanVar.m: Gadient of the mean and variances of the posterior at points given by X.
gpPosteriorMeanCovar.m: Mean and covariances of the posterior at points given by X.
gpPosteriorMeanCovarTest.m: Test the gradients of the mean and covariance.
gpPosteriorMeanVar.m: Mean and variances of the posterior at points given by X.
gpScaleBiasGradient.m: Compute the log likelihood gradient wrt the scales.
gpTest.m: Test the gradients of the gpCovGrads function and the gp models.
gpToolboxes.m: Load in the relevant toolboxes for GP.
gpUpdateAD.m: Update the representations of A and D associated with the model.
gpUpdateKernels.m: Update the kernels that are needed.
