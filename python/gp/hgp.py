import numpy as np
import pylab as pb
import sys
import kern
from simple_GP import GP 
from ndlutil.utilities import pdinv, gpplot
from ndlutil import model, Tango, prior
from scipy import optimize
import pdb


class hgp(GP):
	def __init__(self,X,Y,pdata,kerntype=kern.rbf):
		"""A  hierarchical GP for data fusion, using the new and shiny python tools

		Arguments
		----------
		X : a N x 1 numpy array (floats) (higher dimensional inputs will not plot)
		Y : a N x 1 numpy array (floats)
		pdata: a N x C numpy array (strings)

		Notes
		-----
		pdata should have the same number of rows as X and Y. 
		Each column of pdata defines one level of connectivity:

		"""

		assert len(X.shape)==2
		assert len(Y.shape)==2
		assert len(pdata.shape)==2
		assert pdata.shape[0] == X.shape[0]
		assert pdata.shape[0] == Y.shape[0]

		self.X = X
		self.Y = Y
		self.pdata = pdata
		self.Ndata,self.Nlevels = pdata.shape

		#build connectivity, work out which parameters to tie
		con = np.ones((self.Ndata, 2),dtype=np.bool) # underlying function and noise
		kerns = [kerntype(self.X), kern.white(self.X)]
		ties = []
		for l in pdata.T:
			ul = np.unique(l)
			Nl = ul.size
			tie = '|'.join([str(i) for i in range(con.shape[1],con.shape[1]+ul.size)])
			con = np.hstack((con,l[:,None]==ul[None,:]))
			kerns += [kerntype(self.X) for i in ul]
			ties.append(tie)

		#build the kernel
		self.kern = kern.hierarchical(self.X,con,kerns)
		self.connectivity=con

		#tie and constrain the kernel parameters
		for tie in ties:
			self.kern.tie_param('_('+tie+')_alpha')
			self.kern.tie_param('_('+tie+')_gamma')
			#self.kern.constrain_bounded('_('+tie+')_gamma',2e-1,0.3)

		#constrain kernel_params
		#self.kern.constrain_positive('alpha')
		#self.kern.constrain_bounded('_0_gamma',1e-6,0.15)

		GP.__init__(self,self.X,self.Y,self.kern)

	def predict(self, pdata_new, Xnew):
		"""
		Make a prediction for the GP function. 

		Arguments
		--------
		experiment and replicate should be integers or match self.experiment_names, self.replicate_names. 
		"""
		con = np.ones((Xnew.shape[0],2),dtype=np.bool) #connectivity with the underlying function and noise function
		for lnew,l in zip(pdata_new.T,self.pdata.T):
			con = np.hstack((con,lnew[:,None]==np.unique(l)[None,:]))
			#pdb.set_trace()

		Kxxn = self.kern.cross_compute(Xnew,con)
		Kxnxn = self.kern.compute_new(Xnew,con)
		mu = np.dot(Kxxn.T, np.dot(self.Ki,self.Y))
		var = Kxnxn - np.dot(Kxxn.T,np.dot(self.Ki,Kxxn))
		return mu,var
	
	def plot(self,colour=True,xsize=3,ysize=3):
		if self.Nlevels==1:

			if colour:
				c = Tango.coloursHex['mediumRed']
				cf = Tango.coloursHex['lightRed']
				cp = 'k'
			else:
				c = Tango.coloursHex['Aluminium6']
				cf = Tango.coloursHex['Aluminium1']
				cp = Tango.coloursHex['Aluminium6']

			nrow = 1
			ncol = np.unique(self.pdata).size + 1
			pb.figure(figsize=(ysize*ncol,xsize*nrow))
			rownames = np.unique(self.pdata[:,0])
			xmin,xmax = self.X.min(),self.X.max()
			xmin,xmax = xmin-0.2*(xmax-xmin),xmax+0.2*(xmax-xmin)
			ymin,ymax = self.Y.min(),self.Y.max()
			ymin,ymax = ymin-0.2*(ymax-ymin),ymax+0.2*(ymax-ymin)
			Xplot = np.linspace(xmin,xmax,100)[:,None]

			# do mean predictions first
			pb.subplot(nrow,ncol,1)
			pd = np.array([[''] for foo in range(100)],dtype=np.str) # pdata for prediction
			gpplot(Xplot,*self.predict(pd,Xplot),edgecol=c,fillcol=cf,alpha=.3)
			pb.xticks([])
			pb.xlim(xmin,xmax)
			pb.ylim(ymin,ymax)

			if colour:
				c = Tango.coloursHex['mediumBlue']
				cf = Tango.coloursHex['lightBlue']
			colnames = np.unique(self.pdata[:,0])
			for j,cn in enumerate(colnames):
				pb.subplot(nrow,ncol,2+j)
				pd = np.array([[cn] for foo in range(100)],dtype=np.str)
				gpplot(Xplot,*self.predict(pd,Xplot),edgecol=c,fillcol=cf,alpha=0.3)
				index = np.nonzero(self.pdata[:,0]==cn)[0]
				pb.plot(self.X[index,0],self.Y[index,0],'kx',mew=2,markersize=5)
				pb.title(cn,size='small')
				pb.xticks([])
				pb.yticks([])
				pb.xlim(xmin,xmax)
				pb.ylim(ymin,ymax)


		if self.Nlevels==2:
			nrow = np.unique(self.pdata[:,0]).size  + 1
			ncol = np.max([np.unique(self.pdata[i,1]).size for i in [np.nonzero(self.pdata[:,0]==ui)[0] for ui in np.unique(self.pdata[:,0])]]) + 1
			pb.figure(figsize=(ysize*ncol,xsize*nrow))
			rownames = np.unique(self.pdata[:,0])
			xmin,xmax = self.X.min(),self.X.max()
			xmin,xmax = xmin-0.2*(xmax-xmin),xmax+0.2*(xmax-xmin)
			ymin,ymax = self.Y.min(),self.Y.max()
			ymin,ymax = ymin-0.2*(ymax-ymin),ymax+0.2*(ymax-ymin)
			Xplot = np.linspace(xmin,xmax,100)[:,None]
			if colour:
				c = Tango.coloursHex['mediumRed']
				cf = Tango.coloursHex['lightRed']
				cp = 'k'
			else:
				c = Tango.coloursHex['Aluminium6']
				cf = Tango.coloursHex['Aluminium1']
				cp = Tango.coloursHex['Aluminium6']
			# do mean predictions first
			for i,rn in enumerate(rownames):
				pb.subplot(nrow,ncol,1+i*ncol)
				pd = np.array([[rn,''] for foo in range(100)],dtype=np.str)
				gpplot(Xplot,*self.predict(pd,Xplot),edgecol=c,fillcol=cf,alpha=0.3)
				pb.xticks([])
				pb.ylabel(rn)
				pb.xlim(xmin,xmax)
				pb.ylim(ymin,ymax)
				Tango.removeRightTicks()

			if colour:
				c = Tango.coloursHex['mediumBlue']
				cf = Tango.coloursHex['lightBlue']
			for i,rn in enumerate(rownames):
				index = np.nonzero(self.pdata[:,0]==rn)[0]
				colnames = np.unique(self.pdata[index][:,1])
				for j,cn in enumerate(colnames):
					pb.subplot(nrow,ncol,2+i*ncol+j)
					pd = np.array([[rn,cn] for foo in range(100)],dtype=np.str)
					gpplot(Xplot,*self.predict(pd,Xplot),edgecol=c,fillcol=cf,alpha=0.3)
					index = np.nonzero((self.pdata[:,0]==rn)&(self.pdata[:,1]==cn))[0]
					pb.plot(self.X[index,0],self.Y[index,0],'kx',mew=2,markersize=5)
					pb.title(cn,size='small')
					pb.xticks([])
					pb.yticks([])
					pb.xlim(xmin,xmax)
					pb.ylim(ymin,ymax)
			if colour:
				c = Tango.coloursHex['mediumOrange']
				cf = Tango.coloursHex['lightOrange']
			pb.subplot(nrow,ncol,1+nrow*ncol-ncol)
			pd = np.array([['',''] for foo in range(100)],dtype=np.str)
			gpplot(Xplot,*self.predict(pd,Xplot),edgecol=c,fillcol=cf,alpha=0.3)
			pb.xlim(xmin,xmax)
			pb.ylim(ymin,ymax)
			Tango.removeUpperTicks()
			Tango.removeRightTicks()

			#prediction for new functions
			if colour:
				c = Tango.coloursHex['mediumGreen']
				cf = Tango.coloursHex['lightGreen']
			for i in range(1,ncol):
				pb.subplot(nrow,ncol,(nrow-1)*ncol+1+i)
				mu,var = self.predict(pd,Xplot)
				var += self.kern.kerns[2].alpha
				gpplot(Xplot,mu,var,edgecol=c,fillcol=cf,alpha=0.3)
				pb.xlim(xmin,xmax)
				pb.ylim(ymin,ymax)
				pb.yticks([])
				Tango.removeUpperTicks()







if __name__=='__main__':
	data = np.loadtxt('../data/data_normed.csv',delimiter=',',skiprows=1,usecols=range(1,265))
	pdata = np.loadtxt('../data/all_pdata.csv',dtype=np.str,delimiter=',',skiprows=1)
	times = np.loadtxt('../data/all_pdata.csv',dtype=np.float32,delimiter=',',skiprows=1,usecols=[3])
	genenames = np.loadtxt('../data/data_normed.csv',delimiter=',',skiprows=1,usecols=[0],dtype=np.str)
	#ik = np.nonzero(pdata[:,0]=='kalinka09')[0]
	ik = np.nonzero(pdata[:,1]=='me')[0]
	ih = np.nonzero(genenames=='"Acer"')[0][0]
	dh = data[ih,:][ik][:,None]
	times = times[ik][:,None]
	pdata = pdata[ik,:][:,[0,2]]
	pdata = np.vstack((pdata[:,0],np.asarray(['_'.join(e) for e in pdata]))).T

	m = hhgp(times,dh,pdata)
	m.optimize(maxfun=200)
	m.plot()



			
