read -p "fit?" fit
read -p "ID?" ID
read -p "sumup?" sumup
read -p "which run:" run
if [ "${fit}" == "y" ] ;then 
    read -p "min:max" min max
    read -p "add criteria:" addcri
    for bin in $(seq ${min} ${max})
    do
	python tnpEGM_fitter.py etc/config/settings_eleReco${run}.py --flag passingRECO${ID} --doFit --iBin ${bin} ${addcri}
    done
    cp -r  results/2018_runA${run}/passingRECO/plots/data_2018_RunA/nominalFit/ /eos/user/m/milee/SFs/2018data/2018_runA${run}
fi

if [ "${sumup}" == "y" ]; then
    read -p "lumi:" lum
    python tnpEGM_fitter.py etc/config/settings_eleReco${run}.py --flag passingRECO${ID} --sumUp --lum ${lum}
    cp   results/2018_runA_${run}/passingRECO/egammaEffi.txt_egammaPlots.pdf /eos/user/m/milee/SFs/2018data/2018_runA_RECO_${run}/egammaEffi.txt_egammaPlots${run}.pdf
    cp   results/2018_runA_${run}/passingRECO/egammaEffi.txt_EGM2D.root /eos/user/m/milee/SFs/2018data/2018_runA_RECO_${run}/egammaEffi.txt_EGM2D${run}.root

    cp results/runBtoH_Legacy16${run}/passingRECO/egammaEffi.txt_EGM2D.root /eos/user/m/milee/SFs/2016Legacy/EGM2D_BtoH${run}.root
fi
