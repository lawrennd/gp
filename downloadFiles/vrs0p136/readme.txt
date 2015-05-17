GP software
Version 0.136		Tuesday 08 Jun 2010 at 19:29

The GP toolbox is an implementation of the GPs that uses the
Pseudo-Input method of Snelson and Ghahramani (NIPS 2005) for
sparsification as well as extensions given by Quinonero-Candela and
Rasmussen (JMLR 2005). Since version 0.132 it also provides an
implementation of Titsias's sparse variational approximation published
in AISTATS 2009.

Version 0.136
-------------

Changes to gpReadFromFID for compatibility with C++ release.

Version 0.135
-------------

Modifications by Carl Henrik Ek for compatability with the SGPLVM
toolbox.

Version 0.134
-------------

Updates to allow deconstruction of model files when writing to disk
(gpWriteResult, gpLoadResult, gpDeconstruct, gpReconstruct).

Version 0.133
-------------

Updates for running a GPLVM/GP using the data's inner product matrix
for Interspeech synthesis demos.

Version 0.132
-------------

Remove bug in gpExtractParam for sparse models where scale parameters
were in the wrong place. Moved in some examples from the oxford
toolbox. Added Titsias's variational sparse approximation.

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
demGpCov2D.m: Simple demonstration of sampling from a covariance function.
gpOptions.m: Return default options for GP model.
gpUpdateKernels.m: Update the kernels that are needed.
gpComputeAlpha.m: Update the vector `alpha' for computing posterior mean quickly.
gpCovGrads.m: Sparse objective function gradients wrt Covariance functions for inducing variables.
gpPosteriorSample.m: Create a plot of samples from a posterior covariance.
gpToolboxes.m: Load in the relevant toolboxes for GP.
gpBlockIndices.m: Return indices of given block.
demSilhouetteLinear1.m: Model silhouette data with independent linear models.
gpLogLikelihood.m: Compute the log likelihood of a GP.
gpMeanFunctionGradient.m: Compute the log likelihood gradient wrt the scales.
demOptimiseGpTutorial.m: Shows that there is an optimum for the covariance function length scale.
gpTest.m: Test the gradients of the gpCovGrads function and the gp models.
gpOut.m: Evaluate the output of an Gaussian process model.
gpSubspaceExtractParam.m:
gpPosteriorMeanCovar.m: Mean and covariances of the posterior at points given by X.
gpWriteResult.m: Write a GP result.
gpOptimise.m: Optimise the inducing variable based kernel.
gpPosteriorGradMeanVar.m: Gadient of the mean and variances of the posterior at points given by X.
demSilhouettePlotTrue.m: Plot the true poses for the silhouette data.
demSpgp1dGp1.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpCreate.m: Create a GP model with inducing varibles/pseudo-inputs.
demStickGp1.m: Demonstrate Gaussian processes for regression on stick man data.
demSpgp1dGp3.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSilhouetteAverage.m: Shows the average of the poses.
gpWriteToFile.m: Write a file to be read by the C++ implementation.
gpSample.m: Create a plot of samples from a GP.
gpPosteriorVar.m: Variances of the posterior at points given by X.
demOptimiseGp.m: Shows that there is an optimum for the covariance function length scale.
gpSubspaceOut.m:
gpSubspaceOptimise.m:
gpSubspaceCreate.m: 
demRegression.m: Demonstrate Gaussian processes for regression.
demSpgp1dPlot.m: Plot results from 1-D sparse GP.
gpDataIndices.m: Return indices of present data.
gpPosteriorMeanCovarTest.m: Test the gradients of the mean and covariance.
demGpSample.m: Simple demonstration of sampling from a covariance function.
gpExtractParam.m: Extract a parameter vector from a GP model.
gpPosteriorMeanVar.m: Mean and variances of the posterior at points given by X.
demSilhouetteGp1.m: Model silhouette data with independent RBF GPs.
gpPointLogLikelihood.m: Log-likelihood of a test point for a GP.
gpExpandParam.m: Expand a parameter vector into a GP model.
gpUpdateAD.m: Update the representations of A and D associated with the model.
demGpCovFuncSample.m: Sample from some different covariance functions.
gpDeconstruct.m: break GP in pieces for saving.
gpObjectiveGradient.m: Wrapper function for GP objective and gradient.
gpReadFromFID.m: Load from a FID produced by the C++ implementation.
demSpgp1dGp5.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpCovGradsTest.m: Test the gradients of the likelihood wrt the covariance.
demInterpolation.m: Demonstrate Gaussian processes for interpolation.
gpObjective.m: Wrapper function for GP objective.
gpLoadResult.m: Load a previously saved result.
demSpgp1dGp2.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSilhouettePlot.m:
demSilhouetteGp2.m: Model silhouette data with independent MLP GPs.
gpComputeObservationLogLikelihood.m:  
gpComputeTranslationLogLikelihood.m:  
gpComputeM.m: Compute the matrix m given the model.
gpGradient.m: Gradient wrapper for a GP model.
gpLogLikeGradients.m: Compute the gradients for the parameters and X.
demSpgp1dGp4.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpSubspaceExpandParam.m: 
