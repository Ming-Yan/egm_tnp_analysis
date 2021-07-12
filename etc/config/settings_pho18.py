#############################################################
########## General settings
#############################################################
# flag to be Tested

#tightId = '(ph_abseta < 1.4442 && ph_sieie < 0.00996 && ph_chIso<0.65 && ph_neuIso<(0.317 + 0.01512*ph_et + 0.00002259*ph_et*ph_et) && ph_phoIso < (2.044 + 0.004017*ph_et)) || (ph_abseta > 1.566 && ph_sieie < 0.0271 && ph_chIso<0.517 && ph_neuIso<(2.716 + 0.0117*ph_et + 0.000023*ph_et*ph_et) && ph_phoIso < (3.032 + 0.0037*ph_et))'c

tightId = '(ph_abseta < 1.4442 && ph_sieie < 0.00996 && ph_chIso<0.65 && ph_neuIso < (0.01512*ph_et +0.00002259*ph_et*ph_et +0.317) && ph_phoIso < (2.044 +0.004017*ph_et)) || (ph_abseta > 1.566 && ph_sieie < 0.0271 && ph_chIso<0.517 && ph_neuIso<(0.0117*ph_et +0.000023*ph_et*ph_et +2.716) && ph_phoIso <(0.0037*ph_et +3.302))'
cut1 = "(ph_neuIso - 0.2*ph_chIso*ph_chIso) < 0.2*ph_et"


flags = {
    'passingLoose100XV2'   : '(passingLoose100XV2  == 1)',
    'passingMedium100XV2'  : '(passingMedium100XV2 == 1)',
    'passingTight100XV2'   : '(passingTight100XV2  == 1)',
    'passingMVA94XV2wp80'  : '(passingMVA94XV2wp80 == 1)',
    'passingMVA94XV2wp90'  : '(passingMVA94XV2wp90 == 1)',
    'passingMVA94XV2wp90'  : '(passingMVA94XV2wp90 == 1)',
    'passingHZg94V2'       : '((ph_corr_mva94XV2>-0.4&&ph_sc_abseta<1.4442)||(ph_corr_mva94XV2>-0.58&&ph_sc_abseta>1.56))',
    'passingnocorr94V2'       : '((ph_mva94XV2>-0.4&&ph_sc_abseta<1.4442)||(ph_mva94XV2>-0.58&&ph_sc_abseta>1.56))',
    'passingTightNoHoE'    :  tightId,
    'passingTightTowerHoE'    :  'passingTight100XV2PhoSingleTowerHadOverEmCut==1'
    }

baseOutDir = 'results/HZgphoID18_nocorr90/'
#baseOutDir = 'results/Data2018/tnpPhoID/runD/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef18 as tnpSamples
tnpTreeDir = 'tnpPhoIDs'

samplesDef = {
    'data'   : tnpSamples.Data2018_102X['data_Run2018A'].clone(),
    'mcNom'  : tnpSamples.Data2018_102X['DY_MG'].clone(),
    'mcAlt'  : tnpSamples.Data2018_102X['DY_powheg'].clone(),
    'tagSel' : tnpSamples.Data2018_102X['DY_MG'].clone(),
}
## can add data sample easily
samplesDef['data'].add_sample( tnpSamples.Data2018_102X['data_Run2018B'] )
samplesDef['data'].add_sample( tnpSamples.Data2018_102X['data_Run2018C'] )
samplesDef['data'].add_sample( tnpSamples.Data2018_102X['data_Run2018D'] )
#samplesDef['data'].add_sample( tnpSamples.Moriond18_94X['data_Run2017F'] )

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
    samplesDef['tagSel'].set_cut('tag_Ele_pt > 38')

## set MC weight, simple way (use tree weight) 
#weightName = 'totWeight'
#if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)

## set MC weight, can use several pileup rw for different data taking 

weightName = 'weights_2018_runABCD.totWeight'
#weightName = 'weights_2018_runD.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/rereco2018/ECAL_NOISE/DY_MG_pho.pu.puTree.root')
if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/rereco2018/ECAL_NOISE/DY_powheg_pho.pu.puTree.root')
if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/rereco2018/ECAL_NOISE/DY_MG_pho.pu.puTree.root')


#############################################################
########## bining definition  [can be nD bining]
#############################################################
biningDef = [
    # { 'var' : 'ph_sc_abseta' , 'type': 'float', 'bins': [ 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   # { 'var' : 'ph_et' , 'type': 'float', 'bins': [15,20]},
  { 'var' : 'ph_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
  { 'var' : 'ph_et' , 'type': 'float', 'bins': [20,25,35,50,100,200,500] },
]

#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 35 && abs(tag_sc_eta) < 2.17'

# can add addtionnal cuts for some bins (first check bin number using tnpEGM --checkBins)
additionalCuts = { 
#   0 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   1 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   2 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   3 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   4 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   5 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   6 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   7 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   8 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
#   9 : 'sqrt( 2*event_met_pfmet*tag_Ele_pt*(1-cos(event_met_pfphi-tag_Ele_phi))) < 45',
}

#### or remove any additional cut (default)
#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[0.0,-5.0,5.0]","sigmaP[0.5,0.1,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "meanF[0.288,-5.0,5.0]","sigmaF[1.7, 0.02, 5.]",
    "acmsP[60.,50.,150.]","betaP[0.05,0.01,0.1]","gammaP[0.1, 0., 2]","peakP[90.0]",
    "acmsF[60.,55.,150.]","betaF[0.05,0.01,0.1]","gammaF[0.1, 0, 2]","peakF[90.0]",
    ]

tnpParAltSigFit = [
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[0.9,0.001,8.0]",
    #"meanF[0.4,-5.0,5.0]","sigmaF[2,0.7,15.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[0.3,0.01,8.0]",
    "acmsP[60.,5 0.,90.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[70.,60.,100.]","betaF[0.04,0.01,0.06]","gammaF[0.1, -0.5, 0.08]","peakF[90.0]",
    "meanP[-0.0,-5.0,5.0]","sigmaP[1.0,0.1,6.0]","alphaP[-1.0,0.,2.5.]" ,'nP[3,-10,50]',"sigmaP_2[1.5,0.5,6.0]","sosP[1.,0.001,8.0]",
    "meanF[-0.01,-5.0,5.0]","sigmaF[1.0,0.1,3.]","alphaF[-1.0,0.,2.5.]" ,'nF[3,0.,5]',"sigmaF_2[2.2,0.5,6.0]","sosF[1.5,0.01,5.5]",
    #"acmsP[60.,45.,75.]","betaP[0.04,0.01,0.08]","gammaP[0.1, -0.5, 1]","peakP[90.0]",
    #"acmsF[60.,45.,85.]","betaF[0.04,0.01,0.08]","gammaF[0.1, -0.5, 1]","peakF[90.0]",

    ]
     
tnpParAltBkgFit = [
    #"meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    #"meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.3,0.005,5.0]",
    "meanF[0.,-5.0,5.0]","sigmaF[2.0, 0.5, 6.0]",
    # "alphaP[0.,-5.,5.]",
    # "alphaF[0.,-5.,5.]",
   "p0P[0.4, -5., 10.]", "p1P[-0.25, -5., 0.5]", "p2P[0.1, -1., 2.5]",
   "p0F[-0.3, -5., 0..]", "p1F[-0.25, -5., 0.1]", "p2F[0.1, 0., 2.5]",
    ]
        
