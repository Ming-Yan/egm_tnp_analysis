//USAGE plot2D.C\(\"results/runC/passingRECO\"\,5\,9\)
#include "libCpp/tdrstyle.C"
#include "libCpp/CMS_lumi.C"
void ploteff_pt()
{
  setTDRStyle();
  // string fname[12]=
    {
      /*//"pt_16.root",
      "results/runB_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runC_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runD_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runE_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runF_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",*/
      // "results/runBtoF_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      /*"results/runB_high_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runC_high_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runD_high_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runE_high_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runF_high_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",*/
      // "results/runBtoF_high_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root",
      // "results/runBtoH_Legacy16/passingRECO/egammaEffi.txt_EGM2D.root"
      //"Lowpt_16.root",
    };
	 string fname[2]=
    {
      "results/runBtoF_Moriond18/passingRECO/egammaEffi.txt_EGM2D_BtoF.root",
      "results/2018_runA/passingRECO/egammaEffi.txt_EGM2D.root"
      //"Lowpt_16.root",
    };
	 Color_t color[]={kBlack, kRed,kMagenta-7,kOrange+1,kSpring-1,kAzure+7,kBlue,kBlack, kOrange+3, kGray+1,kViolet+1,kPink-9,kBlack, kGray+1, kRed +1, kRed-2, kAzure+2, kAzure-1, 
		   kSpring-1, kYellow -2 , kYellow+1};
  double etabin_phi[] = {-2.5,-1.479,0.0,1.479,2.5};//5
    // double ptbin[] = {10.0,20.0,45.0,75.0,100.0,500.0};//6
    double ptbin[] = {20.0,45.0,75.0,100.0,500.0};//5
  double etabin[] = {-2.5,-2.0,-1.566,-1.444,-1.0,-0.5,0.0,0.5,1.0,1.444,1.566,2.0,2.5};//11
  double absetabin[] = {0.0,0.5,1.0,1.444,1.566,2.0,2.5};//11
  double etabin_lowpt[] = {-2.5,-2.0,-1.566,-1.444,-1.0,0.0,1.0,1.444,1.566,2.0,2.5};//10
  double phibin[] = {-3.5,-2.5,-1.5,-0.5,0.0,0.5,1.5,2.5,3.5};//9
  
  // int run[5] = {302663,305040,305064,305249,305377};
  // string run[5] = {"B","C","D","E","F"};
	
  TLatex tex;
  tex.SetTextSize(0.03);
  int nfiles = 2;
  int nybin = 4;
  int nxbin = 6;
  TH1F* eta[nxbin][nfiles];
  TH1F* etasf[nxbin][nfiles];
  TH1F* etasfratio[nxbin][nfiles-1];
  TH1F* etadataratio[nxbin][nfiles-1];
  // TH1F* phi[10][nfiles];
  // TH1F* phisf[10][nfiles];
  TFile* f[nfiles];
  TFile* flow[nfiles];
  TH2F* hist[nfiles];
  TH2F* histlow[nfiles];
  TH2F* histsf[nfiles];
  TH2F* histsflow[nfiles];
  
  TLegend *leta = new TLegend(0.12,0.12,0.4,0.3);
  leta->SetBorderSize(0);
  leta->SetFillColor(-1);	
  TLegend *lphi = new TLegend(0.12,0.12,0.45,0.3);
  lphi->SetNColumns(2);
  lphi->SetBorderSize(0);
  lphi->SetFillColor(-1);
  TCanvas *c = new TCanvas("c","",800,800);
  TCanvas *c1 = new TCanvas("c1","",800,800);
  /*c->SetTopMargin(0.055);
  c1->SetTopMargin(0.055);
  c->SetLeftMargin(0.12);
  c1->SetLeftMargin(0.12);*/
  // float yUp = 0.45;
  TPad *pad1 = new TPad("pad1","pad1",0, 0.25, 1,   1);
  pad1->SetGridx();
  pad1->SetGridy();
  // TPad *pad2 =new TPad("pad2","pad2", 0,   0, 1, yUp);
  // pad1->SetBottomMargin(0.008);
  // pad1->SetTopMargin(0.055/(1-yUp));
  // pad2->SetTopMargin(0.01);
  // pad2->SetBottomMargin(0.1/yUp);
  // pad1->SetLeftMargin(0.12);
  // pad2->SetLeftMargin(0.12);
  TPad *pad3 = new TPad("pad3","pad3",0, 0.021, 1,   0.33);
  pad3->SetGridx();
  pad3->SetGridy();
   gStyle->SetTextSize(0.04);
  // TPad *pad4 =new TPad("pad4","pad4", 0,   0, 1, yUp);
  // pad3->SetBottomMargin(0.008);
  // pad3->SetTopMargin(0.055/(1-yUp));
  // pad4->SetTopMargin(0.01);
  // pad4->SetBottomMargin(0.1/yUp);
  // pad3->SetLeftMargin(0.12);
  // pad4->SetLeftMargin(0.12);
  gStyle->SetLabelSize(0.04);
  gStyle->SetOptStat(0);
  cout<<"define done"<<endl;
  
  for (int i = 0 ; i < nfiles; i++)
    {
		
      f[i] =  TFile::Open(fname[i].c_str());
      hist[i] = (TH2F*)f[i]->Get("EGamma_EffData2D");
      histsf[i] = (TH2F*)f[i]->Get("EGamma_SF2D");
      // if(i==0)
	// { 
	  // histsflow[i] = (TH2F*)flow[i]->Get("EGamma_SF2D");
	  // flow[i] =  TFile::Open(fname[i+6].c_str());
	  // histlow[i] = (TH2F*)flow[i]->Get("EGamma_EffData2D");
	// }
      c->cd();
      for (int j = 0 ; j< nxbin ; j++)
	{

	  // if(j==0)
	    // {
	      // eta[j][i] = new TH1F(Form("eta[%d][%d]",j,i),"",nybin-2,etabin_lowpt);
	      // etasf[j][i] = new TH1F(Form("etasf[%d][%d]",j,i),"",nybin-2,etabin_lowpt);
	    // }
	  // else
	    // {
	      eta[j][i] = new TH1F(Form("eta[%d][%d]",j,i),"",nybin,ptbin);
	      etasf[j][i] = new TH1F(Form("etasf[%d][%d]",j,i),"",nybin,ptbin);
	    // }
		
	  // if(i<nfiles-1)
	    // {
	      // if(j==0)
		// {
		  // etasfratio[j][i] = new TH1F(Form("etasfratio[%d][%d]",j,i),"",nybin-2,etabin_lowpt);
		  // etadataratio[j][i] = new TH1F(Form("etadataratio[%d][%d]",j,i),"",nybin-2,etabin_lowpt);
		// }
	      // else
		// {
		  // etasfratio[j][i] = new TH1F(Form("etasfratio[%d][%d]",j,i),"",nybin,etabin_pt);
		  // etadataratio[j][i] = new TH1F(Form("etadataratio[%d][%d]",j,i),"",nybin,etabin_pt);
		// }
	    // }
	
	  //fill 
	  for(int jj = 0 ; jj < nybin ; jj++)
	    {
	      // if(jj<2)
		// {	
		  // if(jj>9) continue;
		  eta[j][i]->SetBinContent(jj+1,(hist[i]->GetBinContent(6-j,jj+1)+hist[i]->GetBinContent(j+7,jj+1))/2);//Data efficiency
		  etasf[j][i]->SetBinContent(jj+1,(histsf[i]->GetBinContent(6-j,jj+1)+histsf[i]->GetBinContent(j+7,jj+1))/2);//SF nominal value
		  eta[j][i]->SetBinError(jj+1,sqrt(hist[i]->GetBinError(6-j,jj+1)*hist[i]->GetBinError(6-j,jj+1)+hist[i]->GetBinError(j+7,jj+1)*hist[i]->GetBinError(j+7,jj+1)));
		  etasf[j][i]->SetBinError(jj+1,sqrt(histsf[i]->GetBinError(6-j,jj+1)*histsf[i]->GetBinError(6-j,jj+1)+histsf[i]->GetBinError(j+7,jj+1)*histsf[i]->GetBinError(j+7,jj+1)));
			 
		  // if(i>0)
		    // {
		      // etasfratio[j][i-1]->SetBinContent(jj+1,histsflow[i]->GetBinContent(jj+1,j+1)/histsflow[0]->GetBinContent(jj+1,j+1));//comparison with 2016 SF
		      // etadataratio[j][i-1]->SetBinContent(jj+1,histlow[i]->GetBinContent(jj+1,j+1)/histlow[0]->GetBinContent(jj+1,j+1));//comparison with 2016 Data Eff
		      // etasfratio[j][i-1]->SetBinError(jj+1,sqrt(pow(histsflow[0]->GetBinError(jj+1,j+1),2)+pow(histsflow[i]->GetBinError(jj+1,j+1),2)));
		      // etadataratio[j][i-1]->SetBinError(jj+1,sqrt(pow(histlow[0]->GetBinError(jj+1,j+1),2)+pow(histlow[i]->GetBinError(jj+1,j+1),2)));
		    // }
			// cout<<i<<" "<<j<<" "<<histsflow[i]->GetBinContent(jj+1,j+1)<<" "<<histsflow[0]->GetBinContent(jj+1,j+1)<<" "<<histsflow[i]->GetBinContent(jj+1,j+1)/histsflow[0]->GetBinContent(jj+1,j+1)<<endl;
		// }
	      // else
		// {
		 
		  // eta[j][i]->SetBinContent(jj+1,histlow[i]->GetBinContent(j+7,jj-1));//Data efficiency
		  // etasf[j][i]->SetBinContent(jj+1,histsflow[i]->GetBinContent(j+7,jj-1));//SF nominal value
		  // eta[j][i]->SetBinError(jj+1,histlow[i]->GetBinError(j+7,jj-1));
		  // etasf[j][i]->SetBinError(jj+1,histsflow[i]->GetBinError(j+7,jj-1));
		  // if(i>0)
		    // {
		      // etasfratio[j][i-1]->SetBinContent(jj+1,histsf[i]->GetBinContent(jj+1,j)/histsf[0]->GetBinContent(jj+1,j));//comparison with 2016 SF
			  
		      // etadataratio[j][i-1]->SetBinContent(jj+1,hist[i]->GetBinContent(jj+1,j)/hist[0]->GetBinContent(jj+1,j));//comparison with 2016 Data Eff
		      // etasfratio[j][i-1]->SetBinError(jj+1,sqrt(pow(histsf[0]->GetBinError(jj+1,j),2)+pow(histsf[i]->GetBinError(jj+1,j),2)));
		      // etadataratio[j][i-1]->SetBinError(jj+1,sqrt(pow(hist[0]->GetBinError(jj+1,j),2)+pow(hist[i]->GetBinError(jj+1,j),2)));
		    // }
		// }
		// cout<<i<<" "<<j<<" "<<histlow[i]->GetBinContent(jj+1,j-1)<<" "<<histsflow[i]->GetBinContent(jj+1,j-1)<<endl;
		// cout<<i<<" "<<j<<" "<<hist[i]->GetBinContent(jj+1,j+1)<<" "<<histsf[i]->GetBinContent(jj+1,j+1)<<endl;
	    }
		
	  //set plot info.
	  // eta[j][i]->SetMarkerColor(color[j]);
	  // eta[j][i]->SetMarkerStyle(20);
	  // eta[j][i]->SetLineColor(color[j]);
			
	  // if(i==0)
	  // {
	  // leta->AddEntry(eta[j][i],Form("%.3f<#eta<%.3f",etabin_phi[j],etabin_phi[j+1]),"pl");
	  // }
	  // if(j==0) 
	  // {
	  // c->cd();
	  // eta[j][i]->SetTitle(Form("run%d",run[i]));
	  // eta[j][i]->GetXaxis()->SetTitle("SC #phi");
	  // eta[j][i]->GetYaxis()->SetTitle("Efficiency");
	  // eta[j][i]->SetMinimum(0.4);
	  // eta[j][i]->SetMaximum(1.01);
	  // eta[j][i]->Draw("pl");
	  // }
	  // else if(i!=3) eta[j][i]->Draw("plsame");
	}

     
    }
  // cout<<eta[0][1]->GetBinContent(1)<<endl;
  // eta[0][0]->Draw();
  cout<<"phi, eta done"<<endl;

  TLegend *ltot = new TLegend(0.24,0.36,.97,0.4);
  ltot->SetBorderSize(0);
  ltot->SetNColumns(2);
  ltot->SetTextSize(0.03);
  ltot->SetFillColorAlpha(0,0.01);	
	
  for(int l = 0 ; l < nxbin ; l++)
    {
      for(int i = 0 ; i < nfiles; i++)
	{	
			
		
	  // if(i==4) continue;
	  // phi[l][i]->SetMarkerColor(color[i]);
	  // phi[l][i]->SetMarkerStyle(20);
	  // phi[l][i]->SetLineColor(color[i]);
	  // if(l<4)
	  // {
	  eta[l][i]->SetMarkerColor(color[i]);
	  etasf[l][i]->SetMarkerColor(color[i]);
	  // if(i==0) eta[l][i]->SetMarkerStyle(4);
	  // else 
	  eta[l][i]->SetMarkerStyle(20);
	  // if(i==0)etasf[l][i]->SetMarkerStyle(4);
	  // else 
	  etasf[l][i]->SetMarkerStyle(20);
	  eta[l][i]->SetLineColor(color[i]);
	  etasf[l][i]->SetLineColor(color[i]);
	   // if(i>0)
	   // {
	   // etasfratio[l][i-1]->SetMarkerStyle(20);
	  // etadataratio[l][i-1]->SetMarkerColor(color[i]);
	  // etasfratio[l][i-1]->SetMarkerColor(color[i]);
	  // etadataratio[l][i-1]->SetLineColor(color[i]);
	 // etadataratio[l][i-1]->SetMarkerStyle(20);
	  // etasfratio[l][i-1]->SetLineColor(color[i]);
	// }
	  // }
	  if(l==0&&i==0)
	    {
	      ltot->AddEntry(eta[0][0],"2017 Rereco B-F","pl");
	      ltot->AddEntry(eta[0][1],"2018 runA","pl");
	      // ltot->AddEntry(eta[0][2],"runD","pl");
	      // ltot->AddEntry(eta[0][3],"runE","pl");
	      // ltot->AddEntry(eta[0][4],"runF","pl");
	      // ltot->AddEntry(eta[0][5],"runB-F","pl");
	    }
		
	  (i==0) {
	      // phi[l][i]->GetXaxis()->SetTitle("SC #eta");
	      // phi[l][i]->GetYaxis()->SetTitle("Efficiency");
	      // phi[l][i]->SetMinimum(0.4);
	      // phi[l][i]->SetMaximum(1.01);
	      // phi[l][i]->SetTitle(Form("%.1f<#phi<%.1f",phibin[l],phibin[l+1]));
	      // c->cd();
	      // phi[l][i]->Draw("pl");
					
	      // if(l<4)
	      // {
	      eta[l][i]->GetXaxis()->SetLabelSize(0.04);
	      // etadataratio[l][i]->GetXaxis()->SetLabelSize(0.04);
	      etasf[l][i]->GetXaxis()->SetLabelSize(0.04);
	      // etasfratio[l][i]->GetXaxis()->SetLabelSize(0.04);
	      etasf[l][i]->GetXaxis()->SetTitle("pT");
	      eta[l][i]->GetXaxis()->SetTitle("pT");
	      eta[l][i]->GetYaxis()->SetTitle("Efficiency");
	      etasf[l][i]->GetYaxis()->SetTitle("Scaling Factor");
	      // etasfratio[l][i]->GetYaxis()->SetTitle("2017/2016");
	      // etadataratio[l][i]->GetYaxis()->SetTitle("2017/2016");
	      eta[l][i]->SetMinimum(0.7);
	      etasf[l][i]->SetMinimum(0.85);
	      // etadataratio[l][i]->SetMinimum(0.85);
	      // etasfratio[l][i]->SetMinimum(0.85);
	      eta[l][i]->SetMaximum(1.05);
	      // etadataratio[l][i]->SetMaximum(1.1);
	      etasf[l][i]->SetMaximum(1.1);
	      // etasfratio[l][i]->SetMaximum(1.1);
	      eta[l][i]->SetTitle(Form("%2.0f<|#eta|<%2.0f",ptbin[l],ptbin[l+1]));
	      etasf[l][i]->SetTitle(Form("%2.0f<|#eta|<%2.0f",ptbin[l],ptbin[l+1]));
	      cout<<">__< ?"<<endl;
	      c->cd();
	      pad1->Draw();
	      pad1->cd();
	      gPad->SetLogx();
	      eta[l][i]->Draw("pl");
	      //c1->cd();
	      pad3->Draw();
	      pad3->cd();
	      gPad->SetLogx();
	      etasf[l][i]->Draw("pl");
	  }	  // cout<<eta[l][i]->GetEntries()<<endl;
	  // }
	   else
	    {
	      c->cd();
	      pad3->cd();
	      etasf[l][i]->Draw("plsame");
	      // c1->cd();
	      // pad4->Draw();
	      // pad4->cd();
	      // if(i==1) etasfratio[l][i-1]->Draw("pl");
	      // else etasfratio[l][i-1]->Draw("plsame");
	      //c->cd();
	      pad1->cd();
	      eta[l][i]->Draw("plsame");
	      // c->cd();
	      // pad2->Draw();
	      // pad2->cd();
	      // if(i==1) etadataratio[l][i-1]->Draw("pl");
	      // else etadataratio[l][i-1]->Draw("plsame");
	    }	
	}
		
      extraText  = "Preliminary";
      lumi_13TeV = "5.9 fb^{-1}";
      CMS_lumi(pad1, 4, 0);
      c->cd();
	  
      ltot->Draw();
		
      c->Print(Form("dataeff_pt_%d.png",l));
      // c->Print(Form("dataeff_eta_%d.pdf",l));
      /*c1->cd();
      ltot->Draw();
      c1->Print(Form("SF_pt_%d.png",l));*/
      // c1->Print(Form("SF_%d.pdf",l));
    } 
}
