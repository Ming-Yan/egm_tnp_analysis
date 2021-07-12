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
    'passleg1' : 'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match==1',
    'passleg2' :'passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2==1'
    }

baseOutDir = 'results/HZgID_94X_trg1_wpL_F/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleTrig'

samplesDef = {
    'data'   : tnpSamples.HZg_L1match['data_94X_F'].clone(),
    'mcNom'  : tnpSamples.HZg_L1match['DY_madgraph_94X'].clone(),
#    'mcAlt'  : tnpSamples.HZg_L1match['DY_powheg_94X'].clone(),
#    'mcAlt'  : tnpSamples.HZg_L1match['DY_amcatnlo_94X'].clone(),
#    'tagSel' : tnpSamples.HZg_L1match['DY_madgraph_94X'].clone(),
}

## can add data sample easily



## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
#if not samplesDef['tagSel'] is None:
#    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
#    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
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
    #{ 'var' : 'el_pt' , 'type': 'float', 'bins': [ 5, 7, 12, 15, 17, 20, 25, 27, 30, 40, 50, 80, 120, 200, 1000 ]},
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [10, 15, 17, 20, 25, 27, 30, 40, 50, 80, 120, 200, 1000 ]},
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
#cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0'

#cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.5 && el_q*tag_Ele_q < 0&& (el_dxy<1.0&&el_dz<0.5&&passingMVA94Xwp90isoV2==1)&&passHltEle32WPTightGsf==1'#18
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.5 && el_q*tag_Ele_q < 0&& (el_dxy<1.0&&el_dz<0.5&&passingMVA94XwpLisoV2==1)'#17
#cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.5 && el_q*tag_Ele_q < 0&& (passingMVA94XwpHZZisoV2 == 1)&&el_sip<4&&el_dxy<1.0&&el_dz<0.5'#17
#cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.5 && el_q*tag_Ele_q < 0&& (passingCutBasedMedium94XV2==1)'


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
    #20 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   # 21 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
   # 22 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',    
   # 23 : 'tag_Ele_trigMVA > 0.92 && sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-1.,1]","sigmaP[1.0,0.1,2.1]",
    "meanF[-1,1.]","sigmaF[0.1,5.0]",
    "acmsP[60,0,120]","betaP[0.,0.08] ","gammaP[0.1, 0.001, 1.0]","peakP[90.0]",
    "acmsF[60.,30.,120.]","betaF[0.05,0.001, 0.08]","gammaF[0.1, 0.001, 1.0]","peakF[90.0]",
    ]
tnpParAltSigFit = [
    "meanP[0.,-2,2]","sigmaP[0.5,0.1,3.0]","alphaP[2.0,-5,5.]" ,'nP[1.,-4,4]',"sigmaP_2[0.8,0.1,3.0]","sosP[1,0.1,5.0]",
    "meanF[-0.1,-8.,8.]","sigmaF[0.5,2.0]","alphaF[2.0,-5,5]",'nF[1.,-2,2]',"sigmaF_2[2.0,1.5,8.0]","sosF[1,0.1,5.0]",
    "acmsP[60.,50.,120.]","betaP[0.04,0.001,0.1]","gammaP[0.1, 0.001, 1.0]","peakP[90.0]",
    "acmsF[60.,50,120]","betaF[0.04,0.001,0.1]","gammaF[0.1, 0.001, 1.0]","peakF[90.0]",
   ]

#tnpParAltSigFit = [
#    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
#    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
#    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
#    "acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
 #   ]
     
tnpParAltBkgFit = [
    "meanP[-5,5]","sigmaP[1.5,1.0,2.2]",
    "meanF[0,-5,5]","sigmaF[0.5,0.1,3.]",
    #"meanF[-0.0,-6.0,6.0]","sigmaF[0.01,5.0]",
    "alphaP[-0.01,-0.1,0.]",
    "alphaF[-0.31,-0.5,0.]",
#    "p0P[-0.1, -5., 0.5]", "p1P[-0.25, -10., 0.5]", "p2P[0.1, -0.5, 2.5]",
 #   "p0F[-0.1, -5., 0.5]", "p1F[-0.25, -5., 0.5]", "p2F[0.1, -0.5, 2.5]"

    ]
        
