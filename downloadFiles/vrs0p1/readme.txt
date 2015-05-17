GP software
Version 0.1		Saturday 18 Nov 2006 at 22:10
Copyright (c) 2006 Neil D. Lawrence

The GP toolbox is an implementation of the GPs that uses the Pseudo-Input method of Snelson and Ghahramani (NIPS 2005) for sparsification as well as extensions given by Quinonero-Candela and Rasmussen (JMLR 2005).

Version 0.1
-----------

The first version which is spun out of the FGPLVM toolbox. The corresponding FGPLVM toolbox is 0.15.

MATLAB Files
------------

Matlab files associated with the toolbox are:

gpUpdateKernels.m: Update the kernels that are needed.
gpGradient.m: Gradient wrapper for a GP model.
gpLogLikelihood.m: Compute the log likelihood of a GP.
demSpgp1d1.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1d2.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1d3.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1d4.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpOptimise.m: Optimise the inducing variable based kernel.
gpPosteriorMeanVar.m: Mean and variances of the posterior at points given by X.
gpObjective.m: Wrapper function for GP objective.
gpDisplay.m: Display a Gaussian process model.
gpDataIndices.m: Return indices of present data.
gpCovGradsTest.m: Test the gradients of the likelihood wrt the covariance.
gpComputeM.m: Compute the matrix m given the model.
gpBlockIndices.m: Return indices of given block.
gpPosteriorGradMeanVar.m: Gadient of the mean and variances of the posterior at points given by X.
gpPosteriorGradMeanCovar.m: Gadient of the mean and variances of the posterior at points given by X.
gpPosteriorMeanCovar.m: Mean and covariances of the posterior at points given by X.
gpScaleBiasGradient.m: Compute the log likelihood gradient wrt the scales.
gpExtractParam.m: Extract a parameter vector from a GP model.
gpOut.m: Evaluate the output of an Gaussian process model.
gpLogLikeGradients.m: Compute the gradients for the parameters and X.
demSpgp1dPlot.m: Plot results from 1-D sparse GP.
gpCovGrads.m: Sparse objective function gradients wrt Covariance functions for inducing variables.
gpOptions.m: Return default options for GP model.
gpExpandParam.m: Expand a parameter vector into a GP model.
gpCreate.m: Create a GP model with inducing varibles/pseudo-inputs.
gpPosteriorMeanCovarTest.m: Test the gradients of the mean and covariance.
gpComputeAlpha.m: Update the vector `alpha' for computing posterior mean quickly.
gpUpdateAD.m: Update the representations of A and D associated with the model.
