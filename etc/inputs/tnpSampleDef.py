from libPython.tnpClassUtils import tnpSample

### qll stat
eos2018Data_V1 = '/eos/cms/store/group/phys_egamma/tnp/ntuples_05122018/2018Data_V1/'
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/tnp/ntuples_05122018/2018Data_V1/'
eos100X_old = '/eos/cms/store/group/phys_egamma/micheli/TnP/ntuples_20180831/2018Data_1/'
eos100X = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_20180905/2018Data_1/'
eos102X = '/eos/cms/store/group/phys_egamma/soffi/TnP/ntuples_20180920/2018Data_1/'
eleID_94X = '/eos/user/m/milee/TnPEleTree/94X/'
eleID_80X = '/eos/user/m/milee/TnPEleTree/80X/'
eleID_102X = '/eos/user/m/milee/TnPEleTree/102X/'
eos2018rereco = '/eos/cms/store/group/phys_egamma/swmukher/rereco2018/ECAL_NOISE/'
eos2018_autumn = '/eos/cms/store/group/phys_egamma/swmukher/NtupleForRecoSF/Rereco2018Data_Autumn18MC_AOD/'
L1match = '/eos/cms/store/group/phys_egamma/tnpTuples/tomc/2020-03-03/'
new17='/eos/cms/store/group/phys_egamma/asroy/Tag-and-Probe_Tree/ReReco17-17Nov2017_MINIAOD_Nm1/'
Moriond18_94X = {
    ### MiniAOD TnP for IDs scale factors
    'DY_madgraph'          : tnpSample('DY_madgraph',
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_Moriond18' : tnpSample('DY_madgraph_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),
    'DY_amcatnlo_Moriond18' : tnpSample('DY_amcatnlo_Moriond18', 
                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_all.root',
                                       isMC = True, nEvts =  -1 ),

    'data_Run2017B' : tnpSample('data_Run2017B' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunB.root' , lumi = 4.891 ),
    'data_Run2017C' : tnpSample('data_Run2017C' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunC.root' , lumi = 9.9 ),
    'data_Run2017D' : tnpSample('data_Run2017D' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunD.root' , lumi = 4.36 ),
    'data_Run2017E' : tnpSample('data_Run2017E' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunE.root' , lumi = 9.53 ),
    'data_Run2017F' : tnpSample('data_Run2017F' , eosMoriond18 + 'data/TnPTree_17Nov2017_RunF.root' , lumi = 13.96 ),

    }
Data2018_10_1_X = {

    #'DY_madgraph'          : tnpSample('DY_madgraph',
    #                                   eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_all.root',
#                                       isMC = True, nEvts =  -1 ),
    'DY_madgraph_15p' : tnpSample('DY_madgraph_15p',
                                       eos2018Data_V1 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_1.root',
                                       isMC = True, nEvts =  -1 ),
#    'DY_amcatnlo_2018' : tnpSample('DY_amcatnlo_Moriond18',
#                                       eosMoriond18 + 'mc/TnPTree_DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_all.root',
#                                       isMC = True, nEvts =  -1 ),

    'data_2018_RunA' : tnpSample('data_2018_RunA' , eos2018Data_V1 + 'data//TnPTree_Prompt2018_RunA_RunAbove315488.root' , lumi = 5.9 ),
    'data_2018_RunA_nocut' : tnpSample('data_2018_RunA' , eos2018Data_V1 + 'data//TnPTree_Prompt2018_RunA.root' , lumi = 5.9 ),
}
Data2018_100X = {
'DY_madgraph':tnpSample('DY_madgraph',
                                       eos100X_old + 'mc/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8_part012.root',
                                       isMC = True, nEvts =  -1 ),
'data_2018_RunA' : tnpSample('data_2018_RunA' , eos100X + 'data/Prompt2018_RunA_v123.root' , lumi = 5.9 ),
'data_2018_RunB' : tnpSample('data_2018_RunB' , eos100X + 'data/Prompt2018_RunB_v12.root' , lumi = 5.9 ),
'data_2018_RunC' : tnpSample('data_2018_RunC' , eos100X + 'data/Prompt2018_RunC_v12.root' , lumi = 5.9 ),
'data_2018_RunD' : tnpSample('data_2018_RunD' , eos100X + 'data/Prompt2018_RunD_v2.root' , lumi = 5.9 ),
}
'''Data2018_102X = {
#'DY_madgraph':tnpSample('DY_madgraph',
 #                                      eos102X + 'mc/DYToEE_M-50_NNPDF31_TuneCP5_13TeV-powheg-pythia8-AOD-102X_part01.root',
    #                                      isMC = True, nEvts =  -1 ),
 'DY_1j_madgraph'              : tnpSample('DY_1j_madgraph',
                                              eos2017Data_94X + 'mc/DY1JetsToLLM50madgraphMLM_ext.root',
                                              isMC = True, nEvts = -1 ),
 'DY_amcatnloext'                 : tnpSample('DY_amcatnloext',
                                       eos2017Data_94X + 'mc/DYJetsToLLM50amcatnloFXFXext.root',
isMC = True, nEvts = -1 ),
'data_2018_RunA' : tnpSample('data_2018_RunA' , eos100X + 'data/Prompt2018_RunA_v123.root' , lumi = 5.9 ),
'data_2018_RunB' : tnpSample('data_2018_RunB' , eos102X + 'data/Prompt2018_RunB_v12.root' , lumi = 5.9 ),
'data_2018_RunC' : tnpSample('data_2018_RunC' , eos102X + 'data/Prompt2018_RunC_v12.root' , lumi = 5.9 ),
'data_2018_RunD' : tnpSample('data_2018_RunD' , eos102X + 'data/Prompt2018_RunD_v2.root' , lumi = 5.9 ),
}'''
Autumn18 = {
 'DY_madgraph'              : tnpSample('DY_madgraph',
                                              eos2018_autumn + 'mc/DYJetsToLLM50madgraphMLM.root',
                                              isMC = True, nEvts = -1 ),
 'DY_powheg'                 : tnpSample('DY_powheg',
                                         eos2018_autumn + 'mc/DYToEEM50powheg.root',
isMC = True, nEvts = -1 ),
 'data_2018_RunA' : tnpSample('data_2018_RunA' , eos2018_autumn+ 'data/RunA.root' , lumi = 5.9 ),
'data_2018_RunB' : tnpSample('data_2018_RunB' , eos102X + 'data/RunB.root' , lumi = 5.9 ),
'data_2018_RunC' : tnpSample('data_2018_RunC' , eos102X + 'data/RunC.root' , lumi = 5.9 ),
'data_2018_RunD' : tnpSample('data_2018_RunD' , eos102X + 'data/RunD.root' , lumi = 5.9 ),
}
HZg_94X = {
    'DY_madgraph'              : tnpSample('DY_madgraph',
                                              eleID_94X + 'DY1Jet_94X_madgraph_mod.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
                                              eleID_94X + 'DY1Jet_94X_amcatnlo.root',
                                              isMC = True, nEvts = 1000 ),
    'data_94X_RunB'  : tnpSample('data_94X_RunB' , eleID_94X + 'RunB_94XIDv2.root' , lumi = 4.823 ),
    'data_94X_RunC'  : tnpSample('data_94X_RunC' , eleID_94X + 'RunC_94XIDv2.root' , lumi = 9.664 ),
    'data_94X_RunD'  : tnpSample('data_94X_RunD' , eleID_94X + 'RunD_94XIDv2.root' , lumi = 4.252 ),
    'data_94X_RunE'  : tnpSample('data_94X_RunE' , eleID_94X + 'RunE_94XIDv2.root' , lumi = 9.278 ),
    'data_94X_RunF'  : tnpSample('data_94X_RunF' , eleID_94X + 'RunF_94XIDv2.root' , lumi = 13.540 ),
     }


HZg_94X_leg2 = {
    'DY_madgraph'              : tnpSample('DY_madgraph',
                                              eleID_94X + 'DY1Jet_94X_madgraph_leg2.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
                                              eleID_94X + 'DY1Jet_94X_amcatnlo_leg2.root',
                                              isMC = True, nEvts = 1000 ),
    'data_94X_RunB'  : tnpSample('data_94X_RunB' , eleID_94X + 'RunB_94XIDv2_leg2.root' , lumi = 4.823 ),
    'data_94X_RunC'  : tnpSample('data_94X_RunC' , eleID_94X + 'RunC_94XIDv2_leg2.root' , lumi = 9.664 ),
    'data_94X_RunD'  : tnpSample('data_94X_RunD' , eleID_94X + 'RunD_94XIDv2_leg2.root' , lumi = 4.252 ),
    'data_94X_RunE'  : tnpSample('data_94X_RunE' , eleID_94X + 'RunE_94XIDv2_leg2.root' , lumi = 9.278 ),
    'data_94X_RunF'  : tnpSample('data_94X_RunF' , eleID_94X + 'RunF_94XIDv2_leg2.root' , lumi = 13.540 ),
     }

HZg_80X = {
    'DY_madgraph'              : tnpSample('DY_madgraph',
                                              eleID_80X + 'MC_leg1.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
                                              eleID_80X + 'altMC.root',
                                              isMC = True, nEvts = 1000 ),
    'data_80X_RunB'  : tnpSample('data_80X_RunB' , eleID_80X + 'RunB_leg1.root' , lumi = 4.823 ),
    'data_80X_RunC'  : tnpSample('data_80X_RunC' , eleID_80X + 'RunC_leg1.root' , lumi = 9.664 ),
    'data_80X_RunD'  : tnpSample('data_80X_RunD' , eleID_80X + 'RunD_leg1.root' , lumi = 4.252 ),
    'data_80X_RunE'  : tnpSample('data_80X_RunE' , eleID_80X + 'RunE_leg1.root' , lumi = 9.278 ),
    'data_80X_RunF'  : tnpSample('data_80X_RunF' , eleID_80X + 'RunF_leg1.root' , lumi = 13.540 ),
    'data_80X_RunG'  : tnpSample('data_80X_RunG' , eleID_80X + 'RunG_leg1.root' , lumi = 13.540 ),
    'data_80X_RunH'  : tnpSample('data_80X_RunH' , eleID_80X + 'RunH_leg1.root' , lumi = 13.540 ),
     }
HZg_80X_leg2 = {
    'DY_madgraph'              : tnpSample('DY_madgraph',
                                              eleID_80X + 'MC_leg2.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
                                              eleID_80X + 'altMC_leg2.root',
                                              isMC = True, nEvts = 1000 ),
    'data_80X_RunB'  : tnpSample('data_80X_RunB' , eleID_80X + 'RunB_leg2.root' , lumi = 4.823 ),
    'data_80X_RunC'  : tnpSample('data_80X_RunC' , eleID_80X + 'RunC_leg2.root' , lumi = 9.664 ),
    'data_80X_RunD'  : tnpSample('data_80X_RunD' , eleID_80X + 'RunD_leg2.root' , lumi = 4.252 ),
    'data_80X_RunE'  : tnpSample('data_80X_RunE' , eleID_80X + 'RunE_leg2.root' , lumi = 9.278 ),
    'data_80X_RunF'  : tnpSample('data_80X_RunF' , eleID_80X + 'RunF_leg2.root' , lumi = 13.540 ),
    'data_80X_RunG'  : tnpSample('data_80X_RunG' , eleID_80X + 'RunG_leg2.root' , lumi = 13.540 ),
    'data_80X_RunH'  : tnpSample('data_80X_RunH' , eleID_80X + 'RunH_leg2.root' , lumi = 13.540 ),
     }
HZg_L1match = {
    'DY_madgraph_102X'              : tnpSample('DY_madgraph_102X',
                                              L1match + '2018/merged/DY_L1matched.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_powheg_102X'                 : tnpSample('DY_powheg_102X',
                                              L1match  + '2018/merged/DY_pow_L1matched.root',
                                              isMC = True, nEvts = 1000 ),
    'DY_madgraph_94X'              : tnpSample('DY_madgraph_94X',
                                              L1match + '2017/merged/DY1_LO_ext_L1matched.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo_94X'                 : tnpSample('DY_amcatnlo_102X',
                                              L1match  + '2017/merged/DY_NLO_ext_L1matched.root',
                                              isMC = True, nEvts = 1000 ),
    'DY_madgraph_80X'              : tnpSample('DY_madgraph_80X',
                                              L1match + '2016/merged/DY_LO_L1matched.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo_80X'                 : tnpSample('DY_amcatnlo_80X',
                                              L1match  + '2016/merged/DY_NLO_L1matched.root',
                                              isMC = True, nEvts = 1000 ),
    'data_102X'  : tnpSample('data_102X' , L1match + '2018/merged/data_L1matched.root' , lumi = 4.823 ),
    'data_94X'  : tnpSample('data_94X' , L1match + '2017/merged/data_L1matched.root' , lumi = 4.823 ),
    'data_94X_B' : tnpSample('data_94X_B' , L1match+ '2017/merged/Run2017B_leg1Threshold22.root', lumi = 4.823 ),
    'data_94X_C' : tnpSample('data_94X_C' , L1match+ '2017/merged/Run2017C_leg1Threshold22.root', lumi = 4.823 ),
    'data_94X_D' : tnpSample('data_94X_D' , L1match+ '2017/merged/Run2017D_leg1Threshold22.root', lumi = 4.823 ),
    'data_94X_E' : tnpSample('data_94X_E' , L1match+ '2017/merged/Run2017E_leg1Threshold22.root', lumi = 4.823 ),
    'data_94X_F' : tnpSample('data_94X_F' , L1match+ '2017/merged/Run2017F_leg1Threshold22.root', lumi = 4.823 ),
    'data_80X'  : tnpSample('data_80X' , L1match + '2016/merged/data_L1matched.root' , lumi = 4.823 ),
    # 'data_102X_RunB'  : tnpSample('data_102X_RunB' , eleID_102X + 'RunB_leg1.root' , lumi = 4.823 ),
    # 'data_102X_RunC'  : tnpSample('data_102X_RunC' , eleID_102X + 'RunC_leg1.root' , lumi = 9.664 ),
    # 'data_102X_RunD'  : tnpSample('data_102X_RunD' , eleID_102X + 'RunD_leg1.root' , lumi = 4.252 ),
     }
# HZg_102X = {
#     'DY_madgraph'              : tnpSample('DY_madgraph',
#                                               eleID_102X + 'MC_leg1.root',
#                                               isMC = True, nEvts = 100000 ),
#     'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
#                                               eleID_102X + 'altMC_leg1.root',
#                                               isMC = True, nEvts = 1000 ),
#     'data_102X_RunA'  : tnpSample('data_102X_RunA' , eleID_102X + 'RunA_leg1.root' , lumi = 4.823 ),
#     'data_102X_RunB'  : tnpSample('data_102X_RunB' , eleID_102X + 'RunB_leg1.root' , lumi = 4.823 ),
#     'data_102X_RunC'  : tnpSample('data_102X_RunC' , eleID_102X + 'RunC_leg1.root' , lumi = 9.664 ),
#     'data_102X_RunD'  : tnpSample('data_102X_RunD' , eleID_102X + 'RunD_leg1.root' , lumi = 4.252 ),
#      }
HZg_102X_leg2 = {
    'DY_madgraph'              : tnpSample('DY_madgraph',
                                              eleID_102X + 'MC_leg2.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo'                 : tnpSample('DY_amcatnlo',
                                              eleID_102X + 'altMC_leg2.root',
                                              isMC = True, nEvts = 1000 ),
    'data_102X_RunA'  : tnpSample('data_102X_RunA' , eleID_102X + 'RunA_leg2.root' , lumi = 4.823 ),
    'data_102X_RunB'  : tnpSample('data_102X_RunB' , eleID_102X + 'RunB_leg2.root' , lumi = 4.823 ),
    'data_102X_RunC'  : tnpSample('data_102X_RunC' , eleID_102X + 'RunC_leg2.root' , lumi = 9.664 ),
    'data_102X_RunD'  : tnpSample('data_102X_RunD' , eleID_102X + 'RunD_leg2.root' , lumi = 4.252 ),
     }
HZg_HLT = {
    'DY_madgraph_94X'              : tnpSample('DY_madgraph_94X',
                                              new17 + 'DY1JetsToLL_madgraphMLM.root',
                                              isMC = True, nEvts = 100000 ),
    'DY_amcatnlo_94X'                 : tnpSample('DY_amcatnlo_102X',
                                              new17  + 'DYJetsToLL_madgraphMLM.root',
                                              isMC = True, nEvts = 1000 ),
    'data_94X_B' : tnpSample('data_94X_B' , new17+ 'SingleEle_RunB.root', lumi = 4.823 ),
    'data_94X_C' : tnpSample('data_94X_C' , new17+ 'SingleEle_RunC.root', lumi = 4.823 ),
    'data_94X_D' : tnpSample('data_94X_D' , new17+ 'SingleEle_RunD.root', lumi = 4.823 ),
    'data_94X_E' : tnpSample('data_94X_E' , new17+ 'SingleEle_RunE.root', lumi = 4.823 ),
    'data_94X_F' : tnpSample('data_94X_F' , new17+ 'SingleEle_RunF.root', lumi = 4.823 ),
    # 'data_102X_RunB'  : tnpSample('data_102X_RunB' , eleID_102X + 'RunB_leg1.root' , lumi = 4.823 ),
    # 'data_102X_RunC'  : tnpSample('data_102X_RunC' , eleID_102X + 'RunC_leg1.root' , lumi = 9.664 ),
    # 'data_102X_RunD'  : tnpSample('data_102X_RunD' , eleID_102X + 'RunD_leg1.root' , lumi = 4.252 ),
     }