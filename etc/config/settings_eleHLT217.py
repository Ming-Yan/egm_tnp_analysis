#############################################################
########## General settings
#############################################################
# flag to be Tested
#cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)cutpassLoose_low = '(el_et<=20&&(( abs(el_sc_eta) < 0.8 && el_noIsoMVA94X > %f ) ||  ( abs(el_sc_eta) > 0.8 && abs(el_sc_eta) < 1.479&& el_noIsoMVA94X > %f ) || ( abs(el_sc_eta) > 1.479 && el_noIsoMVA94X > %f )) )' % (-0.145237,-0.0315746,-0.032173)
cutpassLoose = '(el_sip<4&&el_dxy<1.0&&el_dz<0.5&&(( abs(el_sc_eta) < 0.8 && el_noIsoMVA94X > %f ) ||  ( abs(el_sc_eta) > 0.8 && abs(el_sc_eta) < 1.479&& el_noIsoMVA94X > %f ) || ( abs(el_sc_eta) > 1.479 && el_noIsoMVA94X > %f ) ))' % (-0.146270871164,-0.0315850882679,-0.0321841194737)
cutpassLoose_low = '(el_sip<4&&el_dxy<1.0&&el_dz<0.5&&(( abs(el_sc_eta) < 0.8 && el_noIsoMVA94X > %f ) ||  ( abs(el_sc_eta) > 0.8 && abs(el_sc_eta) < 1.479&& el_noIsoMVA94X > %f ) || ( abs(el_sc_eta) > 1.479 && el_noIsoMVA94X > %f ) ))' % (-0.145237,-0.0315746,-0.032173)


# flag to be Tested
flags = {
    'passingHLT'          : '(passingHLT ==1 )',
    'passingVeto94XV2'    : '(passingVeto94XV2   == 1)',
    'passingLoose94XV2'   : '(passingLoose94XV2  == 1)',
    'passingMedium94XV2'  : '(passingMedium94XV2 == 1)',
    'passingTight94XV2'   : '(passingTight94XV2  == 1)',
    'passingMVA94Xwp80isoV2' : '(passingMVA94Xwp80isoV2 == 1)',
    'passingMVA94Xwp90isoV2' : '(passingMVA94Xwp90isoV2 == 1)',
    'passingMVA94Xwp80noisoV2' : '(passingMVA94Xwp80noisoV2 == 1)',
    'passingMVA94Xwp90noisoV2' : '(passingMVA94Xwp90noisoV2 == 1)',
    'passingMVA94XwpLisoV2'    : '(passingMVA94XwpLisoV2 == 1)',
    'passingMVA94XwpLnoisoV2'  : '(passingMVA94XwpLnoisoV2 == 1)',
    'passingMVA94XwpHZZisoV2'  : '(passingMVA94XwpHZZisoV2 == 1)',
    }

baseOutDir = 'results/HZgID_94X_trg2_mod/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleTrig'

samplesDef = {
    'data'   : tnpSamples.HZg_94X_leg2['data_94X_RunB'].clone(),
    'mcNom'  : tnpSamples.HZg_94X_leg2['DY_madgraph'].clone(),
    'mcAlt'  : tnpSamples.HZg_94X_leg2['DY_amcatnlo'].clone(),
    'tagSel' : tnpSamples.HZg_94X_leg2['DY_madgraph'].clone(),
}

## can add data sample easily

samplesDef['data'].add_sample( tnpSamples.HZg_94X_leg2['data_94X_RunC'] )
samplesDef['data'].add_sample( tnpSamples.HZg_94X_leg2['data_94X_RunD'] )
samplesDef['data'].add_sample( tnpSamples.HZg_94X_leg2['data_94X_RunE'] )
samplesDef['data'].add_sample( tnpSamples.HZg_94X_leg2['data_94X_RunF'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
if not samplesDef['tagSel'] is None:
    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut

## set MC weight, simple way (use tree weight) 
weightName = 'totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
'''
## set MC weight, can use several pileup rw for different data taking periods
weightName = 'weights_2017_runBCDEF.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017/PU/DY_1j_madgraph_ele.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017/PU/DY_amcatnloext_ele.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/ntuple_2017/PU/DY_1j_madgraph_ele.pu.puTree.root')
'''

#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    { 'var' : 'el_sc_abseta' , 'type': 'float', 'bins': [0.,0.8,1.4442,1.566,2.5] },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [ 5, 7, 12, 15, 17, 20, 25, 27, 30, 40, 50, 80, 120, 200, 1000 ] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'


cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.5 && el_q*tag_Ele_q < 0&& (el_dxy<1.0&&el_dz<0.5&&(( abs(el_sc_eta) < 0.8 && el_IsoMVA94XV2 > %f ) ||  ( abs(el_sc_eta) > 0.8 && abs(el_sc_eta) < 1.479&& el_IsoMVA94XV2 > %f ) || ( abs(el_sc_eta) > 1.479 && el_IsoMVA94XV2 > %f ) ))' % (-0.146270871164,-0.0315850882679,-0.0321841194737)

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
    0 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    1 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    2 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    3 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    4 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    5 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    6 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    7 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    8 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    9 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    10 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    11 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    12 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    13 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    14 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    15 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    16 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    17 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    18 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    19 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
    20 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#    21 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
 #   22 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
 #   23 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[0,-1.0,1.0]","sigmaP[2.5,1.8,5.0]",
    "meanF[0.1,-1.0,1.0]","sigmaF[2.0,.1,10.]",
    "acmsP[60.,40.,70.]","betaP[0.04,0.01,0.1]","gammaP[0.01, 0.001, 0.8]","peakP[90.0]",
    "acmsF[60,50,100]","betaF[0.05,0.001, 0.1]","gammaF[0.1,0.01, 0.8]","peakF[90.0]",
#    "acmsP[60.,50.,150.]","betaP[0.05,0.01,0.1]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[50.,30.,70.]","betaF[0.01,1.0]","gammaF[0.05, 0.001,1.0]","peakF[90.0]",
    ]
tnpParAltSigFit = [
    "meanP[-1.,1]","sigmaP[0.5,0.3,3.0]","alphaP[2.0,-5,5.]" ,'nP[0.08,0.01,10.0]',"sigmaP_2[0.8,0.1,6.0]","sosP[1,0.01,5.0]",
    "meanF[-5,5]","sigmaF[1.7,0.1,5.0]","alphaF[2.0,-4,4]",'nF[0.08,0.01,10.0]',"sigmaF_2[2.0,1.,4.0]","sosF[1,0.01,5.0]",
    "acmsP[60.,50.,120.]","betaP[0.01,0.001,0.05]","gammaP[0.01, 0.001, .1]","peakP[90.0]",
    "acmsF[60.,50., 90.]","betaF[0.01,0.001,0.05]","gammaF[0.01, 0.001, 0.1]","peakF[90.0]",
   ]

'''tnpParAltSigFit = [
    "meanP[-0.0,-3.0,3.0]","sigmaP[1,0.1,4.0]","alphaP[2.0,0.1,3.5]" ,'nP[3,-5,6]',"sigmaP_2[1.5,0.5,5.0]","sosP[1,0.1,5.0]",
    "meanF[-0.0,-3.0,3.0]","sigmaF[1.6,1.0,5.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,6]',"sigmaF_2[5.0,1.5,10.0]","sosF[1,0.1,5.]",
    "acmsP[60.,50.,175.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.001, 1]","peakP[90.0]",
    "acmsF[60.,50.,175.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.001, 1]","peakF[90.0]",
    ]'''
     
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[4.5,1.0,8.0]",
    "meanF[0.0,-5.0,5.0]","sigmaF[3.2,1.,5.]",
    "alphaP[-0.2,0.1]",
    "alphaF[-0.5,0.1]",
    ]

