#!/usr/bin/env python
# coding: utf-8

import os,sys
import lhapdf
import numpy as np
import matplotlib.pyplot as py
from matplotlib import gridspec
from  matplotlib import rc
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
rc('text',usetex=True)
from pylab import *
import scipy
from scipy.integrate import dblquad


#---------------------------------------------------------
#---------------------------------------------------------
print("\n --------\n LO forward-backward asymmetry \n -------------\n")
#---------------------------------------------------------
#---------------------------------------------------------


#---------------------------------------------------------
#---------------------------------------------------------
# General plot settings
q = 5300 # GeV
#q = 500 # GeV
filelabel = "DYlumis-pdfsets-minus-q5p3tev"
sqrts=14000
nx = 2000
xmin = pow(q/sqrts,2.0)
xmax=0.98

#---------------------------------------------------------
#---------------------------------------------------------
# Values of the electroweak coupling constants

# LO parameters from mg5 input card
MZ = 91.1535
MW = 80.352
GW = 2.084
GZ = 2.4943
MZ2 = MZ**2.0
MW2 = MW**2.0
# these are actually complex constants
# cosw2 = (MW2 - 1j*GW*MW) / (MZ2 - 1j*GZ*MZ)
cosw2 = MW2 / MZ2
sinw2 = 1.0 - cosw2
GZ2 = GZ**2.0
el = -1.0  # leptons have negative charge
al = -1.0 / 4.0
vl = -1.0 / 4.0 + sinw2
Gmu = 1.1663788e-5
alpha = np.sqrt(2.0) * Gmu / np.pi * MW2 * (1 - MW2 / MZ2)
# we will use pid%2, so d-like are 1 and up-like are 0
eq = np.array( [ 2.0 / 3.0, -1.0 / 3.0 ] )
aq = np.array( [ 1.0 / 4.0, -1.0 / 4.0 ] )
vq = np.array( [ 1.0 / 4.0 - ( 2.0 / 3.0 ) * sinw2,  -1.0 / 4.0 + ( 1.0 / 3.0 ) * sinw2 ])


print("\n Electroweak couplings \n")
print("sinw2 = ",sinw2)
print("eq( u, d ) = ",eq)
print("aq( u, d ) = ",aq)
print("vq( u, d ) = ",vq)

def pgz(mll2):

    return (
        2.0 * mll2 * (mll2 - MZ2) / (sinw2 * cosw2 * ((mll2 - MZ2) ** 2.0 + GZ2 * MZ2))
    )

def pzz(mll2):

    return (
        mll2**2.0 / ((sinw2 * cosw2) ** 2.0 * ((mll2 - MZ2) ** 2.0 + GZ2 * MZ2))
    )

#mll2 = pow(5000,2)
mll2 = pow(5000,2)
print("pgz(5 TeV) = ",pgz(mll2))
print("pzz(5 TeV) = ",pzz(mll2))

# Symmetric effective charges
# up quark
def s_up(mll2):
    return (
        pow(el,2.0)*pow(eq[0],2.0) + \
        pgz(mll2) * ( el * vl * eq[0] * vq[0] ) + \
        pzz(mll2) * ( pow(vl,2.0) + pow(al,2.0) ) * ( pow(vq[0],2.0) + pow(aq[0],2.0) )
    )
def s_down(mll2):
    return (
        pow(el,2.0)*pow(eq[1],2.0) + \
        pgz(mll2) * ( el * vl * eq[1] * vq[1] ) + \
        pzz(mll2) * ( pow(vl,2.0) + pow(al,2.0) ) * ( pow(vq[1],2.0) + pow(aq[1],2.0) )
    )

# Antisymmetric effective charges
# up quark
def a_up(mll2):
    return (
        pgz(mll2) * 2.0 * el * al * eq[0] * aq[0] + \
        pzz(mll2) * 8.0 * vl * al * vq[0] * aq[0]
    )
# down quark
def a_down(mll2):
    return (
        pgz(mll2) * 2.0 * el * al * eq[1] * aq[1] + \
        pzz(mll2) * 8.0 * vl * al * vq[1] * aq[1]
    )

print("\n")
mll2 = pow(5000,2)

print("Antisymmetric coefficients")
print("a_up(5 TeV) = ",a_up(mll2))
print("a_down(5 TeV) = ",a_down(mll2))
print( "el * al * eq[0] * aq[0] = ", el * al * eq[0] * aq[0] )
print( "el * al * eq[1] * aq[1] = ", el * al * eq[1] * aq[1] )
print( "pgz(mll2) * 2.0 * el * al * eq[0] * aq[0] = ", pgz(mll2) * 2.0 * el * al * eq[0] * aq[0] )
print( "pgz(mll2) * 2.0 * el * al * eq[1] * aq[1] = ", pgz(mll2) * 2.0 * el * al * eq[1] * aq[1] )
print( "pzz(mll2) * 8.0 * vl * al * vq[0] * aq[0] = ", pzz(mll2) * 8.0 * vl * al * vq[0] * aq[0] )
print( "pzz(mll2) * 8.0 * vl * al * vq[1] * aq[1] = ", pzz(mll2) * 8.0 * vl * al * vq[1] * aq[1] )

print("\nSymmetric coefficients")
print("s_up(5 TeV) = ",s_up(mll2))
print("s_down(5 TeV) = ",s_down(mll2))

print("\n Completed tests of electroweak couplings \n")


#---------------------------------------------------------
#---------------------------------------------------------
    

print("\n------------------------------------------")
print("2D integration for g_{A,q} and g_{S,q}")
print("-------------------------------------------\n")

#scipy.integrate.dblquad(func, a, b, gfun, hfun, args=(), epsabs=1.49e-08, epsrel=1.49e-08)[source]
#Compute a double integral.
#
#Return the double (definite) integral of func(y, x) from x = a..b and y = gfun(x)..hfun(x).

#--------------------------------------------------------------------------------------------
# Asymmetric integrand
def lo_asy(x1,mll):

    mll2 = math.pow(mll,2.0)
    x2 = pow((mll/sqrts),2)/x1
    if(x1 > 1.0 or x1 < 0.0 or x2 > 1.0 or x2 < 0.0):
        print("invalid x1, x2 = ",x1," ",x2)
        exit()
    
    integrand =  a_up(mll2) * ( p.xfxQ(2,x1,mll)/x1 * p.xfxQ(-2,x2,mll)/x2 - \
                                p.xfxQ(-2,x1,mll)/x1 * p.xfxQ(2,x2,mll)/x2 ) + \
                                a_down(mll2) * ( p.xfxQ(1,x1,mll)/x1 * p.xfxQ(-1,x2,mll)/x2 - \
                                                 p.xfxQ(-1,x1,mll)/x1 * p.xfxQ(1,x2,mll)/x2 )
    return integrand
#---------------------------------------------------------------------------------------------
# Symmetric integrand
def lo_symm(x1,mll):

    mll2 = math.pow(mll,2.0)
    x2 = pow((mll/sqrts),2)/x1
    if(x1 > 1.0 or x1 < 0.0 or x2 > 1.0 or x2 < 0.0):
        print("invalid x1, x2 = ",x1," ",x2)
        exit()
    
    integrand =  s_up(mll2) * ( p.xfxQ(2,x1,mll)/x1 * p.xfxQ(-2,x2,mll)/x2 + \
                                p.xfxQ(-2,x1,mll)/x1 * p.xfxQ(2,x2,mll)/x2 ) + \
                                s_down(mll2) * ( p.xfxQ(1,x1,mll)/x1 * p.xfxQ(-1,x2,mll)/x2 + \
                                                 p.xfxQ(-1,x1,mll)/x1 * p.xfxQ(1,x2,mll)/x2 )
    return integrand
#---------------------------------------------------------------------------------------------

# arguments changed
def xmin(mll):
    return mll/sqrts

def xmax(mll):
    return 1.0

npdfset =3
#pdfset_g = [ "NNPDF40_nnlo_as_01180","210701-n3fit-data-016",\
#             "210705-nnfit-meth-002","210701-n3fit-meth-009"]
pdfset_g = [ "NNPDF40_nnlo_as_01180","220910-ern-001","220910-ern-002"]
pdferror = [ "nnpdf", "nnpdf", "nnpdf", "nnpdf" ]

nmll = 30
mllmin = np.linspace(800,8000,nmll)

# Make the plot
ncols,nrows=1,1
py.figure(figsize=(ncols*5,nrows*3.5))
gs = gridspec.GridSpec(nrows,ncols)
rescolors = py.rcParams['axes.prop_cycle'].by_key()['color']
ax = py.subplot(gs[0])

for iset in range (npdfset):
    
    p=lhapdf.getPDFSet( pdfset_g[iset] )
    nrep= int(p.get_entry("NumMembers"))-1
    lhapdf.setVerbosity(0)

    print("\n PDF set = ",pdfset_g[iset])

    gtotR_low_mll = np.zeros(nmll)
    gtotR_high_mll = np.zeros(nmll)
    gtotR_mid_mll = np.zeros(nmll)
    
    # Run over mll values
    for imll in range(nmll):

        print("\nimll, mllmin[imll] = ", imll, mllmin[imll] )
    
        gtotA = np.zeros(nrep)
        gtotS = np.zeros(nrep)
        gtotR = np.zeros(nrep)
        for irep in range(1,nrep+1):
            p=lhapdf.mkPDF(pdfset_g[iset],irep)
            gtotA[irep-1], error = dblquad(lo_asy,
                                           mllmin[imll],
                                           sqrts,
                                           lambda mll: mll / sqrts,
                                           lambda mll: 1.0,
                                           epsrel=1e-3)
            gtotS[irep-1], error = dblquad(lo_symm,
                                           mllmin[imll],
                                           sqrts,
                                           lambda mll: mll / sqrts,
                                           lambda mll: 1.0,
                                           epsrel=1e-3)
            gtotR[irep-1] = gtotA[irep-1] / gtotS[irep-1]

        if(pdferror[iset]=="nnpdf"):
            gtotA_high = round(np.nanpercentile(gtotA,84,axis=0),3)
            gtotA_low = round(np.nanpercentile(gtotA,16,axis=0),3)
            gtotS_high = round(np.nanpercentile(gtotS,84,axis=0),3)
            gtotS_low = round(np.nanpercentile(gtotS,16,axis=0),3)
            gtotR_high = round(np.nanpercentile(gtotR,84,axis=0),3)
            gtotR_low = round(np.nanpercentile(gtotR,16,axis=0),3)

        if(pdferror[iset]=="ct" or pdferror[iset]=="msht" ):

        # First compute the central values
            p=lhapdf.mkPDF(pdfset_g[iset],0)
            gtotA_cv, error = dblquad(lo_asy,
                                      mllmin[imll],
                                      sqrts,
                                      lambda mll: mll / sqrts,
                                      lambda mll: 1.0,
                                      epsrel=1e-3)
            gtotS_cv, error = dblquad(lo_symm,
                                      mllmin[imll],
                                      sqrts,
                                      lambda mll: mll / sqrts,
                                      lambda mll: 1.0,
                                      epsrel=1e-3)
            gtotR_cv = gtotA_cv / gtotS_cv

            # Now compute Hessian errors
            gtotR_err = 0.0
            for irep in range(int(nrep/2)):
                gtotR_err = gtotR_err  + ( gtotR[2*irep+1] - gtotR[2*irep] )**2.0
            gtotR_err = math.sqrt(gtotR_err)/ 2
            if(pdferror[iset]=="ct") : 
                gtotR_err = gtotR_err / 1.642
            gtotR_low = round(gtotR_cv-gtotR_err,3)
            gtotR_high = round(gtotR_cv+gtotR_err,3)

        if(pdferror[iset]=="symmhessian"):

        # First compute the central values
            p=lhapdf.mkPDF(pdfset_g[iset],0)
            gtotA_cv, error = dblquad(lo_asy,
                                      mllmin[imll],
                                      sqrts,
                                      lambda mll: mll / sqrts,
                                      lambda mll: 1.0,
                                      epsrel=1e-3)
            gtotS_cv, error = dblquad(lo_symm,
                                      mllmin[imll],
                                      sqrts,
                                      lambda mll: mll / sqrts,
                                      lambda mll: 1.0,
                                      epsrel=1e-3)
            gtotR_cv = gtotA_cv / gtotS_cv

            # Now compute Hessian errors
            gtotR_err = 0.0
            for irep in range(nrep):
                gtotR_err = gtotR_err  + ( gtotR[irep] - gtotR_cv)**2.0
            gtotR_err = math.sqrt(gtotR_err)
            gtotR_low = round(gtotR_cv-gtotR_err,3)
            gtotR_high = round(gtotR_cv+gtotR_err,3)      
               
        print("\nmll_min = ",mllmin[imll]," GeV ")
        print("[gtotR_min, gtotR_max ] =  [ ", gtotR_low , " , ",gtotR_high, " ] " )
        print("\n")

        gtotR_low_mll[imll] = gtotR_low
        gtotR_high_mll[imll] = gtotR_high
        gtotR_mid_mll[imll] = (gtotR_high + gtotR_low)/2

        # End loop over mll
        
    if(iset==0):
        p1=ax.plot(mllmin/1000,gtotR_mid_mll,ls="solid")
        ax.fill_between(mllmin/1000,gtotR_high_mll,gtotR_low_mll,color=rescolors[0],alpha=0.2)
        p2=ax.fill(np.NaN,np.NaN,color=rescolors[0],alpha=0.2)
    if(iset==1):
        p3=ax.plot(mllmin/1000,gtotR_mid_mll,ls="dashed")
        ax.fill_between(mllmin/1000,gtotR_high_mll,gtotR_low_mll,color=rescolors[1],alpha=0.2)
        p4=ax.fill(np.NaN,np.NaN,color=rescolors[1],alpha=0.2)
    if(iset==2):
        p5=ax.plot(mllmin/1000,gtotR_mid_mll,ls="dashdot")
        ax.fill_between(mllmin/1000,gtotR_high_mll,gtotR_low_mll,color=rescolors[2],alpha=0.2)
        p6=ax.fill(np.NaN,np.NaN,color=rescolors[2],alpha=0.2)
    if(iset==3):
        p7=ax.plot(mllmin/1000,gtotR_mid_mll,ls="dotted")
        ax.fill_between(mllmin/1000,gtotR_high_mll,gtotR_low_mll,color=rescolors[3],alpha=0.2)
        p8=ax.fill(np.NaN,np.NaN,color=rescolors[3],alpha=0.2)

# End loop over iset
ax.set_xlim(0.8,8)
ax.set_ylim(-1.3,1.8) 

ax.tick_params(which='both',direction='in',labelsize=12,right=True)
ax.tick_params(which='major',length=7)
ax.tick_params(which='minor',length=4)
ax.set_ylabel(r"$(\sum_q g_{A,q}) / (\sum_{q'} g_{S,{q'}})$",fontsize=13)
ax.set_xlabel(r"$m_{\ell\bar{\ell}}^{\rm (min)}~{\rm (TeV)}$",fontsize=13)
ax.set_xticks([1.0,2.0,3.0,4.0, 5.0,6.0,7.0,8.0])
ax.axhline(y=0,color="black",ls="dotted")
#ax.grid(True)

#ax.legend([ (p1[0],p2[0]), (p3[0],p4[0]), (p5[0],p6[0]), (p7[0],p8[0]) ],\             [ r"${\rm NNPDF4.0}$", r"${\rm preHERA\,data}$", r"${\rm 3.1meth+4.0pos}$",r"${\rm 4.0~(3.1pos)}$" ], \ frameon=True,loc=3,prop={'size':10})

ax.legend([ (p1[0],p2[0]), (p3[0],p4[0]) , (p5[0],p6[0]) ],\
          [ r"${\rm NNPDF4.0}$", r"${\rm HERA\,only}$", r"$W^2 \ge 20~{\rm GeV}$" ],\
          frameon=True,loc=3,prop={'size':10})

py.tight_layout(pad=1, w_pad=1, h_pad=1.0)
py.savefig('asym_coeff_mlldep_variations.pdf')
print('asym_coeff_mlldep_variations.pdf')
    
exit()
