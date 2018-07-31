//USAGE plot2D.C\(\"results/runC/passingRECO\"\,5\,9\)
#include "libCpp/tdrstyle.C"
#include "libCpp/CMS_lumi.C"
void ploteff_eta()
{
  setTDRStyle();
  string fname[2]=
    {
      "results/2018_runA/passingRECO/egammaEffi.txt_EGM2D.root",
      "results/runBtoF_Moriond18/passingRECO/egammaEffi.txt_EGM2D.root"     
      //"Lowpt_16.root",
    };
  // Color_t color[]={kMagenta-7,kOrange+1,kSpring-1,kAzure+7,kBlue,kBlack, kOrange+3, kGray+1,kViolet+1,kPink-9,kBlack, kGray+1, kRed +1, kRed-2, kAzure+2, kAzure-1,   kSpring-1, kYellow -2 , kYellow+1};
  Color_t color[]={kBlack,kRed};
  double etabin_phi[] = {-2.5,-1.479,0.0,1.479,2.5};//5
    // double ptbin[] = {10.0,20.0,45.0,75.0,100.0,500.0};//6
    double ptbin[] = {20.0,45.0,75.0,100.0,500.0};//6
  double etabin_pt[] = {-2.5,-2.0,-1.566,-1.444,-1.0,-0.5,0.0,0.5,1.0,1.444,1.566,2.0,2.5};//11
  double etabin_lowpt[] = {-2.5,-2.0,-1.566,-1.444,-1.0,0.0,1.0,1.444,1.566,2.0,2.5};//10
  double phibin[] = {-3.5,-2.5,-1.5,-0.5,0.0,0.5,1.5,2.5,3.5};//9
  
  // int run[5] = {302663,305040,305064,305249,305377};
  // string run[5] = {"B","C","D","E","F"};

  TLatex tex;
  tex.SetTextSize(0.03);
  const int nfiles = 2;
  const int nybin = 12;
  const int nxbin = 5;
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
  
  TCanvas *c = new TCanvas("c","",800,800);
  TCanvas *c1 = new TCanvas("c1","",800,800);
   c->SetBottomMargin(0.);	
  //c1->SetTopMargin(0.055);
  // c->SetLeftMargin(0.12);
  // c1->SetL	eftMargin(0.12);
  TPad *pad1 = new TPad("pad1","pad1",0, 0.25, 1,   1);
  pad1->SetGridx();
  pad1->SetGridy();
   
  TPad *pad3 = new TPad("pad3","pad3",0, 0.021, 1,   0.33);
  pad3->SetGridx();
  pad3->SetGridy();
 
    // gStyle->SetTitleSize(0.04);
  // gStyle->SetLabelSize(0.04);
  gStyle->SetOptStat(0);
  cout<<"define done"<<endl;
  
  for (int i = 0 ; i < nfiles; i++)
    {
		
      f[i] =  TFile::Open(fname[i].c_str());
      // flow[i] =  TFile::Open(fname[i+6].c_str());
      hist[i] = (TH2F*)f[i]->Get("EGamma_EffData2D");
      // histlow[i] = (TH2F*)flow[i]->Get("EGamma_EffData2D");
      histsf[i] = (TH2F*)f[i]->Get("EGamma_SF2D");
      // histsflow[i] = (TH2F*)flow[i]->Get("EGamma_SF2D");
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
	      eta[j][i] = new TH1F(Form("eta[%d][%d]",j,i),"",nybin,etabin_pt);
	      etasf[j][i] = new TH1F(Form("etasf[%d][%d]",j,i),"",nybin,etabin_pt);
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
	     if(jj==2||jj==9)continue;
		  eta[j][i]->SetBinContent(jj+1,hist[i]->GetBinContent(jj+1,j+1));//Data efficiency
		  etasf[j][i]->SetBinContent(jj+1,histsf[i]->GetBinContent(jj+1,j+1));//SF nominal value
		  eta[j][i]->SetBinError(jj+1,hist[i]->GetBinError(jj+1,j+1));
		  etasf[j][i]->SetBinError(jj+1,histsf[i]->GetBinError(jj+1,j+1));
		  cout<<i<<" "<<j<<" "<<hist[i]->GetBinContent(jj+1,j+1)<<" "<<histsf[i]->GetBinContent(jj+1,j+1)<<endl;
	    }
	}
    }
  // cout<<eta[0][1]->GetBinContent(1)<<endl;
  // eta[0][0]->Draw();
  cout<<"phi, eta done"<<endl;

  TLegend *ltot = new TLegend(0.24,0.36,.97,0.4);
  ltot->SetBorderSize(0);
  ltot->SetNColumns(6);
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
	      ltot->AddEntry(eta[0][0],"2017 RerecoB-F","pl");
	      ltot->AddEntry(eta[0][1],"2018 runA","pl");
	      // ltot->AddEntry(eta[0][2],"runD","pl");
	      // ltot->AddEntry(eta[0][3],"runE","pl");
	      // ltot->AddEntry(eta[0][4],"runF","pl");
	      // ltot->AddEntry(eta[0][5],"runB-F","pl");
	    }
		
	  if(i==0)
	    {
	      // phi[l][i]->GetXaxis()->SetTitle("SC #eta");
	      // phi[l][i]->GetYaxis()->SetTitle("Efficiency");
	      // phi[l][i]->SetMinimum(0.4);
	      // phi[l][i]->SetMaximum(1.01);
	      // phi[l][i]->SetTitle(Form("%.1f<#phi<%.1f",phibin[l],phibin[l+1]));
	      // c->cd();
	      // phi[l][i]->Draw("pl");
					
	      // if(l<4)
	      // {
	      eta[l][i]->GetXaxis()->SetLabelSize(0);
	      // etadataratio[l][i]->GetXaxis()->SetLabelSize(0.04);
	      etasf[l][i]->GetXaxis()->SetLabelSize(0.1);
	      etasf[l][i]->GetYaxis()->SetLabelSize(0.1);
	      eta[l][i]->GetYaxis()->SetLabelSize(0.04);
		  etasf[l][i]->GetXaxis()->SetTitleSize(0.1);
	      etasf[l][i]->GetYaxis()->SetTitleSize(0.1);
	      etasf[l][i]->GetYaxis()->SetTitleOffset(0.6);
	      // etasfratio[l][i]->GetXaxis()->SetLabelSize(0.04);
	      etasf[l][i]->GetXaxis()->SetTitle("SC #eta");
	      // eta[l][i]->GetXaxis()->SetTitle("SC #eta");
	      // etadataratio[l][i]->GetXaxis()->SetTitle("SC #eta");
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
	      eta[l][i]->SetTitle(Form("%2.0f<pT<%2.0f",ptbin[l],ptbin[l+1]));
	      etasf[l][i]->SetTitle(Form("%2.0f<pT<%2.0f",ptbin[l],ptbin[l+1]));
	      c->cd();
	      pad1->Draw();
	      pad1->cd();
	      eta[l][i]->Draw("pl");
	      c->cd();
	      pad3->Draw();
	      pad3->cd();
	      etasf[l][i]->Draw("pl");
	    }
	  // cout<<eta[l][i]->GetEntries()<<endl;
	  // }
	   else
	    {
			c->cd();
	      // c1->cd();
	      pad3->cd();
	      etasf[l][i]->Draw("plsame");
	      // c1->cd();
	      // pad4->Draw();
	      // pad4->cd();
	      // if(i==1) etasfratio[l][i-1]->Draw("pl");
	      // else etasfratio[l][i-1]->Draw("plsame");
	      // c->cd();
	      pad1->cd();
	      eta[l][i]->Draw("plsame");
	      // c->cd();
	      // pad2->Draw();
	      // pad2->cd();
	      // if(i==1) etadataratio[l][i-1]->Draw("pl");
	      // else etadataratio[l][i-1]->Draw("plsame");
	    }	
	}
		
     
      c->cd();
      ltot->Draw();
	extraText  = "Preliminary";
      lumi_13TeV = "5.9 fb^{-1}";
      CMS_lumi(pad1, 4, 0);
      
      // c->Print(Form("dataeff_eta_%d.pdf",l));
      // c1->cd();
	  // extraText  = "2016";
      // lumi_13TeV = "36.3 fb^{-1}";
      // CMS_lumi(pad3, 4, 0);
      // ltot->Draw();
	  c->Print(Form("dataeff_eta_%d.png",l));
      // c1->Print(Form("SF_%d.png",l));
      // c1->Print(Form("SF_%d.pdf",l));
    } 
}
