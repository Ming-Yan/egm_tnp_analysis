############################################################
########## General settings
#############################################################
# flag to be Tested
cutpass80 = '(( abs(mc_probe_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(mc_probe_eta) > 0.8 && abs(mc_probe_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(mc_probe_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
cutpass90 = '(( abs(mc_probe_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(mc_probe_eta) > 0.8 && abs(mc_probe_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(mc_probe_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)
#cutpassReco = '( abs(sc_eta) < 2.5 &&  '
# flag to be Tested
flags = {
   #    'passingVeto'   : '(passingVeto   == 1)',
   #    'passingLoose'  : '(passingLoose  == 1)',
   #    'passingMedium' : '(passingMedium == 1)',
   #    'passingTight'  : '(passingTight  == 1)',
   #    'passingMVA80'  : cutpass80,
   #    'passingMVA90'  : cutpass90,
   'passingRECO'    : '(passingRECO == 1)',
   'passingRECOTrackDriven'    : '(passingRECOTrackDriven == 1)'
   }
baseOutDir = 'results/2018_runA_tk'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
#tnpTreeDir = 'GsfElectronToEleID'
tnpTreeDir = 'tnpEleReco'

samplesDef = {
   'data'   : tnpSamples.Data2018_10_1_X['data_2018_RunA'].clone(),
   'mcNom'  : tnpSamples.Data2018_10_1_X['DY_madgraph_15p'].clone(),
   'mcAlt'  : tnpSamples.Data2018_10_1_X['DY_madgraph_15p'].clone(),
   'tagSel'  : tnpSamples.Data2018_10_1_X['DY_madgraph_15p'].clone()
   }
## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.ICHEP2016['data_2016_runD_ele'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
   samplesDef['tagSel'].rename('mcAltSel_DY_madgraph_ele')
   samplesDef['tagSel'].set_cut('tag_Ele_pt > 37')

## set MC weight, simple way (use tree weight) 

weightName = 'weights_2018_runA.totWeight'
#weightName = ''
#weightName = 'puweight.weight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/tnp/ntuples_05122018/2018Data_V1/PU/DY_madgraph1_ele.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/tnp/ntuples_05122018/2018Data_V1/PU/DY_madgraph1_ele.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel' ].set_weight(weightName)
if not samplesDef['tagSel' ] is None: samplesDef['tagSel' ].set_puTree('/eos/cms/store/group/phys_egamma/tnp/ntuples_05122018/2018Data_V1/PU/DY_madgraph1_ele.pu.puTree.root')
#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
   # { 'var' : 'mc_probe_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   # { 'var' : 'mc_probe_et' , 'type': 'float', 'bins': [10,20.0,30,40,50,200] },

   #{ 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   #    { 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   #{ 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.444,-1.0,-0.5,0.0,0.5, 1.0,1.444,1.566,2.0,2.5]},
   #{ 'var' : 'sc_abseta' , 'type': 'float', 'bins': [0.0,0.5,1.0,1.4442,1.566,2.0,2.5]},
   #   { 'var' : 'sc_eta' , 'type': 'float', 'bins': [-2.5,-1.479, 0.0, 1.479, 2.5] },
   #{ 'var' : 'sc_et' , 'type': 'float', 'bins': [20.0,45,75,100,500] },
   #{ 'var' : 'sc_et' , 'type': 'float', 'bins': [75,100,500] },
   #   { 'var' : 'sc_et' , 'type': 'float', 'bins': [10.0,20.0,30,40,50,200] },
   #   { 'var' : 'sc_et' , 'type': 'float', 'bins': [20.0,30,40] },
   { 'var' : 'mc_probe_eta' , 'type': 'float', 'bins': [-2.5,-1.479, 0.0, 1.479, 2.5] },   #####used this for phi
   { 'var' : 'mc_probe_phi' , 'type': 'float', 'bins': [-3.5,-2.5,-1.5,-0.5,0,0.5,1.5,2.5,3.5] }   #####used this for phi
   ]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.5  && abs(sc_eta)<2.5 && tag_Ele_trigMVA > 0.90 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 && sc_et > 20'
####check eta.phi pt dependence
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.5  && abs(sc_eta)<2.5 && tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45'
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.5  && abs(sc_eta)<2.5 && tag_Ele_trigMVA > 0.90 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 && sc_et > 20'
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.5  && abs(sc_eta)<2.5 && tag_Ele_trigMVA > 0.90 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 60 && sc_et > 25'
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.5  && abs(sc_eta)<2.5'



# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
#    0 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    1 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45  ',
 #   2 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45  ',
  #  3 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45  ',
   # 4 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45  ',
    #5 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
    #6 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   # 7 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   # 8 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   # 9 : 'tag_Ele_trigMVA > 0.95 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   10 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   11 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   12 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   13 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   14 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   15 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   16 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   17 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   18 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 ',
   #   19 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45 '
   }

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
#tnpParNomFit = [
#    "meanP[-0.69,-5.0,5.0]","sigmaP[1,0.25,5.0]",
#    "meanF[-0.46,-5.0,5.0]","sigmaF[1.5,0.1,8.0]",
#    "acmsP[60.,20.,150.]","betaP[0.05,0.01,0.1]","gammaP[0.1, 0, 1]","peakP[90.0]",
#    "acmsF[60.,20.,100.]","betaF[0.05,0.01,0.08]","gammaF[0.1, 0, 1]","peakF[100.0]",
#    ]


###bin 03
#tnpParNomFit = [
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.001,10.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.001,10.0]",
#    "acmsP[60.,50.,100.]","betaP[0.05,0.001,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
#   "acmsF[60.,50.,100.]","betaF[0.05,0.001,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",
#    ]

###bin 04
#tnpParNomFit = [
#    "meanP[0.187,-5.0,5.0]","sigmaP[0.647,0.1,5.0]",
#    "meanF[0.478,-8.0,8.0]","sigmaF[0.518,0.5,10.0]",
#    "acmsP[90.,50.,100.]","betaP[0.001,0.3]","gammaP[0.034 0, 1]","peakP[90.0]",
#    "acmsF[90.,50.,200.]","betaF[0.05,0.001,0.5]","gammaF[0.1, 0, 1]","peakF[90.0]",
#   ]
 #tnpParNomFit = [
 #    "meanP[0.17,-5.0,5.0]","sigmaP[0.521,0.1,5.0]",
 #    "meanF[0.478,-8.0,8.0]","sigmaF[1.42,0.01,10.0]",
 #   "acmsP[60.1.,50.,150.]","betaP[0.001,0.001,0.5]","gammaP[0.05, 0, 0.8]","peakP[90.0]",
 #    "acmsF[60,20.,250.]","betaF[0.01,0.001,1]","gammaF[0.1, 0, 0.8]","peakF[90.0]",
 #  ]

 ##double peak try
 #tnpParNomFit = [
 #   "meanP[0.196,-5.0,5.0]","sigmaP[1.,0.1,5.0]",
 #   "meanF[0.005,-8.0,8.0]","sigmaF[1.5,0.1,10.0]",
 #  "acmsP[80,50.,100.]","betaP[0.057,0.001,0.8]","gammaP[0.05, 0.001, 1]","peakP[90.0]",
 #   "acmsF[70,10.,100.]","betaF[0.01,0.001,1]","gammaF[0.04, 0.001, 1]","peakF[90.0]",
#]

###05 - try again
#tnpParNomFit = [
#    "meanP[0.168,-5.0,5.0]","sigmaP[0.033,0.001,6.0]",
#    "meanF[0.015,-10.0,10.0]","sigmaF[0.028,0.008,10.0]",
#    "acmsP[139.,50.,200.]","betaP[0.024,0.001,0.15]","gammaP[0.1, 0, 0.08]","peakP[90.0]",
#    "acmsF[198.581,100.,200.]","betaF[0.015,0.0001,10]","gammaF[0.064, 0, 5]","peakF[90.0]",
#    ]

###06, ##08
#tnpParNomFit = [ 
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[1.,0.5,8.0]",
#   "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.5]","gammaP[0.1, 0, 1]","peakP[90.0]",
#    "acmsF[144.5,20.,250.]","betaF[0.1,0.01,1]","gammaF[0.1, 0, 1]","peakF[90.0]",
#    ]
tnpParNomFit = [ 
   "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
   "meanF[-0.0,-10.0,10.0]","sigmaF[1.,0.5,8.0]",
   "acmsP[120.,40.,180.]","betaP[0.1,0.001,.1]","gammaP[0.1, 0, 1]","peakP[80,90.0]",
   "acmsF[120,50.,180.]","betaF[0.01,0.001,0.1]","gammaF[0.1, 0.001, 1]","peakF[80.0,90.0]",
   ]

###14
#tnpParNomFit = [
#    "meanP[-5.0,5.0]","sigmaP[1.,0.1,5.0]",
#    "meanF[-5.0,5.0]","sigmaF[1.2,0.1,5.0]",
#    "acmsP[79.,40.,80.]","betaP[0.057,0.01,0.08]","gammaP[0.042, 0, 1]","peakP[90.0]",
#    "acmsF[55.50.,80.]","betaF[0.05,0.1,1]","gammaF[0.803, 0, 1]","peakF[90.0]",
#    ]
##tnpParNomFit = [
#    "meanP[0.31,-5.0,5.0]","sigmaP[1.,0.6,10.0]",
#    "meanF[0.803,-5.0,5.0]","sigmaF[1.,0.1,10.0]",
#   "acmsP[40.,10.,80.]","betaP[0.057,0.02,1]","gammaP[0.042, 0.01, 1]","peakP[80,90.0]",
#    "acmsF[40.,10.,80.]","betaF[0.026,0.02,1]","gammaF[0.803, 0.01, 1]","peakF[80,90.0]",
##   ]

##16
#tnpParNomFit = [
#    "meanP[0.274,-5.0,5.0]","sigmaP[1.474,0.1,5.0]",
#    "meanF[1.826,-5.0,5.0]","sigmaF[1.931,0.1,5.0]",
#    "acmsP[84.22.,50.,85.]","betaP[0.03,0.01,0.08]","gammaP[0.003, 0, 1]","peakP[90.0]",
#    "acmsF[60,40.,70.]","betaF[0.01,0.008,0.5]","gammaF[0.1, 0, 1]","peakF[90.0]",
#    ]

##17
#tnpParNomFit = [
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
#    "meanF[-0.0,-10.0,10.0]","sigmaF[0.5,0.1,15.0]",
#    "acmsP[50.,10.,200]","betaP[0.05,0.01,0.08]","gammaP[0.1, 0, .1]","peakP[90.0]",
#   "acmsF[20.,10,200]","betaF[0.01,0.0001,0.08]","gammaF[0.04,0.0,.1]","peakF[90.0]",
#   ]

###35
#tnpParNomFit = [
##    "meanP[0.585,-5.0,10.0]","sigmaP[0.028,0.001,10.0]",
#    "meanF[-0.004,-5.0,5.0]","sigmaF[0.5,0.001,10.0]",
#    "acmsP[80.,50.,200.]","betaP[0.016,0.01,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
#    "acmsF[80.,50.,200.]","betaF[0.03,0.01,0.1]","gammaF[0.1, 0, 1]","peakF[90.0]",
#    ]




####36
##tnpParNomFit = [
##    "meanP[-0.0,-10.0,10.0]","sigmaP[0.5,0.1,5.0]",
#    "meanF[-0.0,-10.0,10.0]","sigmaF[0.5,0.1,10.0]",
#    "acmsP[90.,20.,200.]","betaP[0.05,0.01,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
#    "acmsF[25.,20.,100.]","betaF[0.08,0.01,0.5]","gammaF[0.1, 0, 1]","peakF[90.0]",
#    ]

#tnpParNomFit = [
#    "meanP[0.349,-5.0,5.0]","sigmaP[0.789,0.1,1.]",
#    "meanF[0.698,-5.0,5.0]","sigmaF[0.5,0.001,1.]",
#    "acmsP[180,100.,200.]","betaP[0.001,0.08]","gammaP[0.0512, 0, 0.5]","peakP[90.0,95.0]",
#    "acmsF[40.,20.,90.]","betaF[0.01,1.0]","gammaF[0.1, -0.01, 0.8]","peakF[115,90.0,130.0]",
#    ]


####07 possible - check again
#tnpParNomFit = [
#    "meanP[-0.0,-10.0,10.0]","sigmaP[0.5,0.01,10.0]",
#    "meanF[-0.0,-10.0,10.0]","sigmaF[0.5,0.01,10.0]",
#    "acmsP[60.,50.,100.]","betaP[0.02,0.01,0.08]","gammaP[0.1, 0, 1]","peakP[90.0]",
#   "acmsF[60.,50.,100.]","betaF[0.02,0.01,0.08]","gammaF[0.1, 0, 1]","peakF[90.0]",
#   ]
####04, 05 
#tnpParNomFit = [
#    "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.01,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.01,5.0]",
#    "acmsP[60.,50.,100.]","betaP[0.02,0.001,0.1]","gammaP[0.1, 0, 1]","peakP[90.0]",
#    "acmsF[60.,50.,100.]","betaF[0.02,0.001,0.1]","gammaF[0.1, 0, 1]","peakF[90.0]",
#    ]
###14
#tnpParNomFit = [
#    "meanP[-0.0,-10.0,10.0]","sigmaP[0.9,0.01,10.0]",
#    "meanF[-0.0,-10.0,10.0]","sigmaF[0.9,0.01,10.0]",
#    "acmsP[60.,50.,100.]","betaP[0.02,0.001,0.1]","gammaP[0.1, 0, 1]","peakP[90.0]",
#    "acmsF[60.,50.,100.]","betaF[0.02,0.001,0.1]","gammaF[0.1, 0, 1]","peakF[90.0]",
#    ]


###bin 07
#tnpParNomFit = [
#    "meanP[-0.0,-10.0,10.0]","sigmaP[0.9,0.01,10.0]",
#    "meanF[-0.0,-10.0,10.0]","sigmaF[0.9,0.01,10.0]",
#    "acmsP[60.,40.,100.]","betaP[0.01,0.0001,0.8]","gammaP[0.1, 0, 1.0]","peakP[90.0]",
#    "acmsF[60.,40.,100.]","betaF[0.01,0.0001,2.0]","gammaF[0.1, 0, 0.5]","peakF[90.0]",
#    ]

###bin 14
#tnpParNomFit = [
#   "meanP[0.41,-10.0,10.0]","sigmaP[0.8,0.01,5.0]",
#   "meanF[0.447,-3.0,3.0]","sigmaF[0.8,0.1,5.0]",
#   "acmsP[71.,50.,100.]","betaP[0.113,0.001,0.8]","gammaP[0.055, 0, 1]","peakP[90.0]",
#   "acmsF[147,50.,200.]","betaF[0.022,0.001,0.8]","gammaF[0.03, 0, 1]","peakF[80.0,110.0]",
#    ]

#tnpParNomFit = [
#   "meanP[0.41,-2.0,2.0]","sigmaP[0.8,0.1,5.0]",
#   "meanF[0.447,-3.0,3.0]","sigmaF[0.8,0.05,10.0]",
#   "acmsP[50.,200.]","betaP[0.03,0.005,1]","gammaP[0.055, 0, 0.1]","peakP[90.0]",
#  "acmsF[20.,90.]","betaF[0.01,0.001,0.5]","gammaF[0.03, 0, 0.1]","peakF[80.0,110.0]",
#   ]
###bin 12
tnpParAltSigFit = [
   "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
   "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
   "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
   "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
   ]

tnpParAltBkgFit = [
   "meanP[-0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
   "meanF[-0.0,-5.0,5.0]","sigmaF[0.5,0.1,2.0]",
   #"p0P[0.1, -5., 10.]", "p1P[-0.25, -5., 0.5]", "p2P[0.1, -1., 2.5]",
   #"p0F[0.1, -5., 10.]", "p1F[-0.25, -5., 0.5]", "p2F[0.1, -1., 2.5]"
   "alphaP[0.,-5.,5.]",
   "alphaF[0.,0.,5.]",
   ]

