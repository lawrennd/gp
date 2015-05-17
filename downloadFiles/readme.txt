GP software
Version 0.137		Friday 22 Jul 2011 at 16:22

The GP toolbox is an implementation of the GPs that uses the
Pseudo-Input method of Snelson and Ghahramani (NIPS 2005) for
sparsification as well as extensions given by Quinonero-Candela and
Rasmussen (JMLR 2005). Since version 0.132 it also provides an
implementation of Titsias's sparse variational approximation published
in AISTATS 2009.

Version 0.137
-------------

Minor updates to gpLoadResult for allowing different functions for loading in data.

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

gpScaleBiasGradient.m: Compute the log likelihood gradient wrt the scales.
gpComputeM.m: Compute the matrix m given the model.
demSpgp1dGp3.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
gpObjectiveGradient.m: Wrapper function for GP objective and gradient.
gpToolboxes.m: Load in the relevant toolboxes for GP.
gpOptimise.m: Optimise the inducing variable based kernel.
gpPosteriorVar.m: Variances of the posterior at points given by X.
demStickGp1.m: Demonstrate Gaussian processes for regression on stick man data.
gpUpdateKernels.m: Update the kernels that are needed.
gpLoadResult.m: Load a previously saved result.
gpReadFromFile.m: Load a file produced by the C++ implementation.
demSilhouetteGp2.m: Model silhouette data with independent MLP GPs.
gpGradient.m: Gradient wrapper for a GP model.
demSpgp1dPlot.m: Plot results from 1-D sparse GP.
gpDeconstruct.m: break GP in pieces for saving.
demGpTwoSampleLifsh.m: Run GP two sample code on LifSh.
gpObjective.m: Wrapper function for GP objective.
gpMeanFunctionGradient.m: Compute the log likelihood gradient wrt the scales.
gpSubspaceExpandParam.m: 
gpSubspaceCreate.m: 
gpExtractParam.m: Extract a parameter vector from a GP model.
demGpSample.m: Simple demonstration of sampling from a covariance function.
gpComputeTranslationLogLikelihood.m:  
demOptimiseGp.m: Shows that there is an optimum for the covariance function length scale.
demSilhouetteLinear1.m: Model silhouette data with independent linear models.
gpPointLogLikelihood.m: Log-likelihood of a test point for a GP.
demOptimiseGpTutorial.m: Shows that there is an optimum for the covariance function length scale.
demSpgp1dGp2.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demInterpolation.m: Demonstrate Gaussian processes for interpolation.
demSpgp1dGp4.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demSpgp1dGp5.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demGpCovFuncSample.m: Sample from some different covariance functions.
gpUpdateAD.m: Update the representations of A and D associated with the model.
demSilhouettePlotTrue.m: Plot the true poses for the silhouette data.
demSilhouettePlot.m:
gpComputeObservationLogLikelihood.m:  
gpExpandParam.m: Expand a parameter vector into a GP model.
gpSubspaceOut.m:
gpDisplay.m: Display a Gaussian process model.
gpDataIndices.m: Return indices of present data.
gpPosteriorGradMeanVar.m: Gadient of the mean and variances of the posterior at points given by X.
gpPosteriorMeanVar.m: Mean and variances of the posterior at points given by X.
demGpTwoSampleLif.m: Run GP two sample code on LIF.
gpWriteResult.m: Write a GP result.
demGpCov2D.m: Simple demonstration of sampling from a covariance function.
gpPosteriorSample.m: Create a plot of samples from a posterior covariance.
gpCovGrads.m: Sparse objective function gradients wrt Covariance functions for inducing variables.
gpLogLikeGradients.m: Compute the gradients for the parameters and X.
demSpgp1dGp1.m: Do a simple 1-D regression after Snelson & Ghahramani's example.
demGpTwoSampleEB.m: Run GP two sample code on EB.
gpOut.m: Evaluate the output of an Gaussian process model.
gpBlockIndices.m: Return indices of given block.
gpCovGradsTest.m: Test the gradients of the likelihood wrt the covariance.
demGpTwoSample.m: Test GP two sample code.
gpTwoSample.m: Do Oliver Stegles simple two sample test on a data set.
gpSubspaceExtractParam.m:
demSilhouetteGp1.m: Model silhouette data with independent RBF GPs.
gpReadFromFID.m: Load from a FID produced by the C++ implementation.
demRegression.m: Demonstrate Gaussian processes for regression.
gpCreate.m: Create a GP model with inducing varibles/pseudo-inputs.
gpComputeAlpha.m: Update the vector `alpha' for computing posterior mean quickly.
gpLogLikelihood.m: Compute the log likelihood of a GP.
gpPosteriorGradMeanCovar.m: Gadient of the mean and variances of the posterior at points given by X.
gpTest.m: Test the gradients of the gpCovGrads function and the gp models.
gpWriteToFile.m: Write a file to be read by the C++ implementation.
gpSample.m: Create a plot of samples from a GP.
gpReconstruct.m: Reconstruct an GP form component parts.
gpPosteriorMeanCovar.m: Mean and covariances of the posterior at points given by X.
gpPosteriorMeanCovarTest.m: Test the gradients of the mean and covariance.
demSilhouetteAverage.m: Shows the average of the poses.
gpSubspaceOptimise.m:
gpOptions.m: Return default options for GP model.
