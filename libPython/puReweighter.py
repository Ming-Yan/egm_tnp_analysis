import ROOT as rt
import numpy as np
import sys
import argparse
import os


print '** puReweighter requires root_numpy.'
print '** To install on lxplus: '
print 'pip install --user root_numpy'
from root_numpy import  tree2array, array2tree


puMC = {
    'Spring2016MC_PUscenarioV1' : [ 0.000829312873542, 0.00124276120498, 0.00339329181587, 0.00408224735376, 0.00383036590008, 
                                    0.00659159288946,  0.00816022734493, 0.00943640833116, 0.0137777376066,  0.017059392038,
                                    0.0213193035468,   0.0247343174676,  0.0280848773878,  0.0323308476564,  0.0370394341409,  
                                    0.0456917721191,   0.0558762890594,  0.0576956187107,  0.0625325287017,  0.0591603758776,
                                    0.0656650815128,   0.0678329011676,  0.0625142146389,  0.0548068448797,  0.0503893295063,  
                                    0.040209818868,    0.0374446988111,  0.0299661572042,  0.0272024759921,  0.0219328403791,
                                    0.0179586571619,   0.0142926728247,  0.00839941654725, 0.00522366397213, 0.00224457976761, 
                                    0.000779274977993, 0.000197066585944,7.16031761328e-05,0.0             , 0.0,
                                    0.0,        0.0,        0.0,        0.0,        0.0,    
                                    0.0,        0.0,        0.0,        0.0,        0.0],
}

### MC pu scenario to be used
puMCscenario = 'Spring2016MC_PUscenarioV1'


#### Compute weights for all data epoch specified below
puDataEpoch = {
    '2016_runB'   : 'etc/inputs/pileup_runB_2016.root',
    '2016_runC'   : 'etc/inputs/pileup_runC_2016.root',
    '2016_runD'   : 'etc/inputs/pileup_runD_2016.root',
    '2016_runBCD' : 'etc/inputs/pileup_runBCD_2016.root'
}




def reweight( sample ):
    if sample.path is None:
        print '[puReweighter]: Need to know the MC tree (option --mcTree or sample.path)'
        sys.exit(1)
    

### create a tree with only weights that will be used as friend tree for reweighting different lumi periods
    print 'Opening mc file: ', sample.path
    fmc = rt.TFile(sample.path,'read')
    dirs = fmc.GetListOfKeys()
    tmc = None
    for d in dirs:
        if (d.GetName() == "sampleInfo"): continue
        tmc = fmc.Get("%s/fitter_tree" % d.GetName())

#### can reweight vs nVtx but better to reweight v truePU
#    print 'Opening data file: ',info['filedata']
#    fdata = rt.TFile(info['filedata'],'read')
#    tdata = fdata.Get("%s/fitter_tree" % info['tnpTreeDir'])

        #    hmc   = rt.TH1F('hMC_nPV'  ,'MC nPV'  , 51,-0.5,50.5)
#    hdata = rt.TH1F('hdata_nPV','Data nPV', 51,-0.5,50.5)
#    tmc.Draw('event_nPV>>hMC_nPV','','goff')
#    tdata.Draw('event_nPV>>hdata_nPV','','goff')
#    hmc.Scale(1/hmc.Integral())
#    hdata.Scale(1/hdata.Integral())
#    hdata.Divide(hmc)
#    for i in xrange(51):
#        print "w[nPV =%d ] =  %1.3f"% ( i,hdata.GetBinContent(i+1) )
#    fmc.cd()
    
    puDataDist = {}
    puDataArray= {}
    weights = {}
    for pu in puDataEpoch.keys():
        fpu = rt.TFile(puDataEpoch[pu],'read')
        puDataDist[pu] = fpu.Get('pileup').Clone('puHist_%s' % pu)
        puDataDist[pu].Scale(1./puDataDist[pu].Integral())
        puDataDist[pu].SetDirectory(0)
        puDataArray[pu] = []
        for ipu in range(len(puMC[puMCscenario])):
            ibin_pu  = puDataDist[pu].GetXaxis().FindBin(ipu+0.00001)
            puDataArray[pu].append(puDataDist[pu].GetBinContent(ibin_pu))
        fpu.Close()
        weights[pu] = []

    mcEvts = tree2array( tmc, branches = ['weight','truePU'] )


    pumc = puMC[puMCscenario]
    print '-> nEvtsTot ', len(mcEvts)
    for ievt in xrange(len(mcEvts)):
        if ievt%1000000 == 0 :            print 'iEvt:',ievt
        evt = mcEvts[ievt]
        for pu in puDataEpoch.keys():
            puw  = puDataArray[pu][evt['truePU']] /  pumc[evt['truePU']]
            totw = evt['weight']*puw
            weights[pu].append( ( puw,totw) )

    newFile    = rt.TFile( sample.puTree, 'recreate')

    for pu in puDataEpoch.keys():
        treeWeight = rt.TTree('weights_%s'%pu,'tree with weights')
        wpuarray = np.array(weights[pu],dtype=[('PUweight',float),('totWeight',float)])
        array2tree( wpuarray, tree = treeWeight )
        treeWeight.Write()

    newFile.Close()    
    fmc.Close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='tnp EGM pu reweighter')
    parser.add_argument('--mcTree'  , dest = 'path',  default = None, help = 'MC tree to compute weights for')
    parser.add_argument('puTree'    , default = None                , help = 'output puTree')

    args = parser.parse_args()
    reweight(args)





