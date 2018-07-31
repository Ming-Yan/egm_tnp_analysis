from libPython.tnpClassUtils import tnpSample

### qll stat
eos2018Data_V1 = '/eos/cms/store/group/phys_egamma/tnp/ntuples_05122018/2018Data_V1/'
#eosDir1 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v1/'
#eosDir2 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/v2/'
#eosDirREC = 'eos/cms/store/group/phys_egamma/tnp/80X/RecoSF/RECOSFs_2016/'
#eosWinter17 = 'eos/cms/store/group/phys_egamma/tnp/80X/PhoEleIDs/Moriond17_v1/'
eosMoriond18 = '/eos/cms/store/group/phys_egamma/tnp/ntuples_05122018/2018Data_V1/'

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
