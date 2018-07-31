void egammaEffi.txt_egammaPlots()
{
//=========Macro generated from canvas: totopT/totopT
//=========  (Thu May 10 08:25:14 2018) by ROOT version6.02/05
   TCanvas *totopT = new TCanvas("totopT", "totopT",0,0,800,800);
   gStyle->SetOptFit(1);
   gStyle->SetOptStat(0);
   gStyle->SetOptTitle(0);
   totopT->SetHighLightColor(2);
   totopT->Range(0,0,1,1);
   totopT->SetFillColor(0);
   totopT->SetBorderMode(0);
   totopT->SetBorderSize(2);
   totopT->SetTickx(1);
   totopT->SetTicky(1);
   totopT->SetLeftMargin(0.12);
   totopT->SetRightMargin(0.02);
   totopT->SetTopMargin(0.055);
   totopT->SetFrameFillStyle(0);
   totopT->SetFrameBorderMode(0);
  
// ------------>Primitives in pad: totopT_up
   TPad *totopT_up = new TPad("totopT_up", "totopT_up",0,0.4,1,1);
   totopT_up->Draw();
   totopT_up->cd();
   totopT_up->Range(1.105969,0.8077922,2.73148,1.132468);
   totopT_up->SetFillColor(0);
   totopT_up->SetBorderMode(0);
   totopT_up->SetBorderSize(2);
   totopT_up->SetLogx();
   totopT_up->SetGridx();
   totopT_up->SetGridy();
   totopT_up->SetTickx(1);
   totopT_up->SetTicky(1);
   totopT_up->SetLeftMargin(0.12);
   totopT_up->SetRightMargin(0.02);
   totopT_up->SetBottomMargin(0.13);
   totopT_up->SetFrameFillStyle(0);
   totopT_up->SetFrameBorderMode(0);
   totopT_up->SetFrameFillStyle(0);
   totopT_up->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1001[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph0_fy1001[4] = {
   0.955,
   0.979105,
   0.982,
   0.9645};
   Double_t Graph0_fex1001[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph0_fey1001[4] = {
   0.004527704,
   0.004587699,
   0.01234909,
   0.00229131};
   TGraphErrors *gre = new TGraphErrors(4,Graph0_fx1001,Graph0_fy1001,Graph0_fex1001,Graph0_fey1001);
   gre->SetName("Graph0");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   Int_t ci;      // for color index setting
   TColor *color; // for color definition with alpha
   ci = TColor::GetColor("#999999");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#999999");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1001 = new TH1F("Graph_Graph1001","Graph",100,20,500);
   Graph_Graph1001->SetMinimum(0.85);
   Graph_Graph1001->SetMaximum(1.1);
   Graph_Graph1001->SetDirectory(0);
   Graph_Graph1001->SetStats(0);
   Graph_Graph1001->SetLineStyle(0);
   Graph_Graph1001->SetMarkerStyle(20);
   Graph_Graph1001->GetXaxis()->SetLabelFont(42);
   Graph_Graph1001->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1001->GetXaxis()->SetLabelSize(0);
   Graph_Graph1001->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1001->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1001->GetXaxis()->SetTitleFont(42);
   Graph_Graph1001->GetYaxis()->SetTitle("Data efficiency");
   Graph_Graph1001->GetYaxis()->SetLabelFont(42);
   Graph_Graph1001->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1001->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph1001->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1001->GetYaxis()->SetTitleFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelFont(42);
   Graph_Graph1001->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1001->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1001->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1001->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1001);
   
   gre->Draw("ap");
   
   Double_t Graph1_fx1002[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph1_fy1002[4] = {
   0.9405,
   0.967,
   0.9749724,
   0.9535};
   Double_t Graph1_fex1002[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph1_fey1002[4] = {
   0.004717001,
   0.01121384,
   0.01830701,
   0.004092689};
   gre = new TGraphErrors(4,Graph1_fx1002,Graph1_fy1002,Graph1_fex1002,Graph1_fey1002);
   gre->SetName("Graph1");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   ci = TColor::GetColor("#cc0000");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#cc0000");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1002 = new TH1F("Graph_Graph1002","Graph",100,20,500);
   Graph_Graph1002->SetMinimum(0.85);
   Graph_Graph1002->SetMaximum(1.1);
   Graph_Graph1002->SetDirectory(0);
   Graph_Graph1002->SetStats(0);
   Graph_Graph1002->SetLineStyle(0);
   Graph_Graph1002->SetMarkerStyle(20);
   Graph_Graph1002->GetXaxis()->SetLabelFont(42);
   Graph_Graph1002->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1002->GetXaxis()->SetLabelSize(0);
   Graph_Graph1002->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1002->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1002->GetXaxis()->SetTitleFont(42);
   Graph_Graph1002->GetYaxis()->SetTitle("Data efficiency");
   Graph_Graph1002->GetYaxis()->SetLabelFont(42);
   Graph_Graph1002->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1002->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph1002->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1002->GetYaxis()->SetTitleFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelFont(42);
   Graph_Graph1002->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1002->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1002->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1002->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1002);
   
   gre->Draw("p");
   
   Double_t Graph2_fx1003[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph2_fy1003[4] = {
   0.9605,
   0.979,
   0.984,
   0.967};
   Double_t Graph2_fex1003[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph2_fey1003[4] = {
   0.00223609,
   0.005003222,
   0.01905256,
   0.003605565};
   gre = new TGraphErrors(4,Graph2_fx1003,Graph2_fy1003,Graph2_fex1003,Graph2_fey1003);
   gre->SetName("Graph2");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   ci = TColor::GetColor("#993333");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#993333");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1003 = new TH1F("Graph_Graph1003","Graph",100,20,500);
   Graph_Graph1003->SetMinimum(0.85);
   Graph_Graph1003->SetMaximum(1.1);
   Graph_Graph1003->SetDirectory(0);
   Graph_Graph1003->SetStats(0);
   Graph_Graph1003->SetLineStyle(0);
   Graph_Graph1003->SetMarkerStyle(20);
   Graph_Graph1003->GetXaxis()->SetLabelFont(42);
   Graph_Graph1003->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1003->GetXaxis()->SetLabelSize(0);
   Graph_Graph1003->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1003->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1003->GetXaxis()->SetTitleFont(42);
   Graph_Graph1003->GetYaxis()->SetTitle("Data efficiency");
   Graph_Graph1003->GetYaxis()->SetLabelFont(42);
   Graph_Graph1003->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1003->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph1003->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1003->GetYaxis()->SetTitleFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelFont(42);
   Graph_Graph1003->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1003->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1003->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1003->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1003);
   
   gre->Draw("p");
   
   Double_t Graph3_fx1004[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph3_fy1004[4] = {
   0.9575,
   0.9823719,
   0.984,
   0.966};
   Double_t Graph3_fex1004[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph3_fey1004[4] = {
   0.007314376,
   0.01440604,
   0.02169101,
   0.003427842};
   gre = new TGraphErrors(4,Graph3_fx1004,Graph3_fy1004,Graph3_fex1004,Graph3_fey1004);
   gre->SetName("Graph3");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   ci = TColor::GetColor("#0066cc");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#0066cc");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1004 = new TH1F("Graph_Graph1004","Graph",100,20,500);
   Graph_Graph1004->SetMinimum(0.85);
   Graph_Graph1004->SetMaximum(1.1);
   Graph_Graph1004->SetDirectory(0);
   Graph_Graph1004->SetStats(0);
   Graph_Graph1004->SetLineStyle(0);
   Graph_Graph1004->SetMarkerStyle(20);
   Graph_Graph1004->GetXaxis()->SetLabelFont(42);
   Graph_Graph1004->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1004->GetXaxis()->SetLabelSize(0);
   Graph_Graph1004->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1004->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1004->GetXaxis()->SetTitleFont(42);
   Graph_Graph1004->GetYaxis()->SetTitle("Data efficiency");
   Graph_Graph1004->GetYaxis()->SetLabelFont(42);
   Graph_Graph1004->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1004->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph1004->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1004->GetYaxis()->SetTitleFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelFont(42);
   Graph_Graph1004->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1004->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1004->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1004->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1004);
   
   gre->Draw("p");
   
   Double_t Graph4_fx1005[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph4_fy1005[4] = {
   0.9495,
   0.9825,
   0.9815,
   0.962};
   Double_t Graph4_fex1005[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph4_fey1005[4] = {
   0.006557446,
   0.003464116,
   0.01059481,
   0.00229131};
   gre = new TGraphErrors(4,Graph4_fx1005,Graph4_fy1005,Graph4_fex1005,Graph4_fey1005);
   gre->SetName("Graph4");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetLineWidth(2);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1005 = new TH1F("Graph_Graph1005","Graph",100,20,500);
   Graph_Graph1005->SetMinimum(0.85);
   Graph_Graph1005->SetMaximum(1.1);
   Graph_Graph1005->SetDirectory(0);
   Graph_Graph1005->SetStats(0);
   Graph_Graph1005->SetLineStyle(0);
   Graph_Graph1005->SetMarkerStyle(20);
   Graph_Graph1005->GetXaxis()->SetLabelFont(42);
   Graph_Graph1005->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1005->GetXaxis()->SetLabelSize(0);
   Graph_Graph1005->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1005->GetXaxis()->SetTitleOffset(0.9);
   Graph_Graph1005->GetXaxis()->SetTitleFont(42);
   Graph_Graph1005->GetYaxis()->SetTitle("Data efficiency");
   Graph_Graph1005->GetYaxis()->SetLabelFont(42);
   Graph_Graph1005->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1005->GetYaxis()->SetLabelSize(0.05);
   Graph_Graph1005->GetYaxis()->SetTitleSize(0.06);
   Graph_Graph1005->GetYaxis()->SetTitleFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelFont(42);
   Graph_Graph1005->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1005->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1005->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1005->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1005);
   
   gre->Draw("p");
   totopT_up->Modified();
   totopT->cd();
  
// ------------>Primitives in pad: totopT_do
   TPad *totopT_do = new TPad("totopT_do", "totopT_do",0,0,1,0.45);
   totopT_do->Draw();
   totopT_do->cd();
   totopT_do->Range(1.105969,0.7736641,2.73148,1.117176);
   totopT_do->SetFillColor(0);
   totopT_do->SetBorderMode(0);
   totopT_do->SetBorderSize(2);
   totopT_do->SetLogx();
   totopT_do->SetTickx(1);
   totopT_do->SetTicky(1);
   totopT_do->SetLeftMargin(0.12);
   totopT_do->SetRightMargin(0.02);
   totopT_do->SetTopMargin(0.05);
   totopT_do->SetBottomMargin(0.2222222);
   totopT_do->SetFrameFillStyle(0);
   totopT_do->SetFrameBorderMode(0);
   totopT_do->SetFrameFillStyle(0);
   totopT_do->SetFrameBorderMode(0);
   
   Double_t Graph0_fx1006[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph0_fy1006[4] = {
   0.9744898,
   0.9874464,
   0.9944304,
   0.9791878};
   Double_t Graph0_fex1006[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph0_fey1006[4] = {
   0.004620106,
   0.004626784,
   0.01250541,
   0.002326203};
   gre = new TGraphErrors(4,Graph0_fx1006,Graph0_fy1006,Graph0_fex1006,Graph0_fey1006);
   gre->SetName("Graph0");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   ci = TColor::GetColor("#999999");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#999999");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1006 = new TH1F("Graph_Graph1006","Graph",100,20,500);
   Graph_Graph1006->SetMinimum(0.85);
   Graph_Graph1006->SetMaximum(1.1);
   Graph_Graph1006->SetDirectory(0);
   Graph_Graph1006->SetStats(0);
   Graph_Graph1006->SetLineStyle(0);
   Graph_Graph1006->SetMarkerStyle(20);
   Graph_Graph1006->GetXaxis()->SetTitle("p_{T}  [GeV]");
   Graph_Graph1006->GetXaxis()->SetMoreLogLabels();
   Graph_Graph1006->GetXaxis()->SetNoExponent();
   Graph_Graph1006->GetXaxis()->SetLabelFont(42);
   Graph_Graph1006->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1006->GetXaxis()->SetLabelSize(0.065);
   Graph_Graph1006->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1006->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1006->GetXaxis()->SetTitleFont(42);
   Graph_Graph1006->GetYaxis()->SetTitle("Data / MC ");
   Graph_Graph1006->GetYaxis()->SetLabelFont(42);
   Graph_Graph1006->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1006->GetYaxis()->SetLabelSize(0.065);
   Graph_Graph1006->GetYaxis()->SetTitleSize(0.065);
   Graph_Graph1006->GetYaxis()->SetTitleFont(42);
   Graph_Graph1006->GetZaxis()->SetLabelFont(42);
   Graph_Graph1006->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1006->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1006->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1006->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1006);
   
   gre->Draw("ap");
   
   Double_t Graph1_fx1007[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph1_fy1007[4] = {
   0.9695876,
   0.9842239,
   0.9984102,
   0.9764465};
   Double_t Graph1_fex1007[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph1_fey1007[4] = {
   0.004862888,
   0.01141357,
   0.0187471,
   0.004191181};
   gre = new TGraphErrors(4,Graph1_fx1007,Graph1_fy1007,Graph1_fex1007,Graph1_fey1007);
   gre->SetName("Graph1");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   ci = TColor::GetColor("#cc0000");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#cc0000");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1007 = new TH1F("Graph_Graph1007","Graph",100,20,500);
   Graph_Graph1007->SetMinimum(0.85);
   Graph_Graph1007->SetMaximum(1.1);
   Graph_Graph1007->SetDirectory(0);
   Graph_Graph1007->SetStats(0);
   Graph_Graph1007->SetLineStyle(0);
   Graph_Graph1007->SetMarkerStyle(20);
   Graph_Graph1007->GetXaxis()->SetTitle("p_{T}  [GeV]");
   Graph_Graph1007->GetXaxis()->SetMoreLogLabels();
   Graph_Graph1007->GetXaxis()->SetNoExponent();
   Graph_Graph1007->GetXaxis()->SetLabelFont(42);
   Graph_Graph1007->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1007->GetXaxis()->SetLabelSize(0.065);
   Graph_Graph1007->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1007->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1007->GetXaxis()->SetTitleFont(42);
   Graph_Graph1007->GetYaxis()->SetTitle("Data / MC ");
   Graph_Graph1007->GetYaxis()->SetLabelFont(42);
   Graph_Graph1007->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1007->GetYaxis()->SetLabelSize(0.065);
   Graph_Graph1007->GetYaxis()->SetTitleSize(0.065);
   Graph_Graph1007->GetYaxis()->SetTitleFont(42);
   Graph_Graph1007->GetZaxis()->SetLabelFont(42);
   Graph_Graph1007->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1007->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1007->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1007->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1007);
   
   gre->Draw("p");
   
   Double_t Graph2_fx1008[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph2_fy1008[4] = {
   0.9806023,
   0.9900369,
   0.9989848,
   0.9822245};
   Double_t Graph2_fex1008[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph2_fey1008[4] = {
   0.00228289,
   0.005059627,
   0.0193427,
   0.003662331};
   gre = new TGraphErrors(4,Graph2_fx1008,Graph2_fy1008,Graph2_fex1008,Graph2_fey1008);
   gre->SetName("Graph2");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   ci = TColor::GetColor("#993333");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#993333");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1008 = new TH1F("Graph_Graph1008","Graph",100,20,500);
   Graph_Graph1008->SetMinimum(0.85);
   Graph_Graph1008->SetMaximum(1.1);
   Graph_Graph1008->SetDirectory(0);
   Graph_Graph1008->SetStats(0);
   Graph_Graph1008->SetLineStyle(0);
   Graph_Graph1008->SetMarkerStyle(20);
   Graph_Graph1008->GetXaxis()->SetTitle("p_{T}  [GeV]");
   Graph_Graph1008->GetXaxis()->SetMoreLogLabels();
   Graph_Graph1008->GetXaxis()->SetNoExponent();
   Graph_Graph1008->GetXaxis()->SetLabelFont(42);
   Graph_Graph1008->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1008->GetXaxis()->SetLabelSize(0.065);
   Graph_Graph1008->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1008->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1008->GetXaxis()->SetTitleFont(42);
   Graph_Graph1008->GetYaxis()->SetTitle("Data / MC ");
   Graph_Graph1008->GetYaxis()->SetLabelFont(42);
   Graph_Graph1008->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1008->GetYaxis()->SetLabelSize(0.065);
   Graph_Graph1008->GetYaxis()->SetTitleSize(0.065);
   Graph_Graph1008->GetYaxis()->SetTitleFont(42);
   Graph_Graph1008->GetZaxis()->SetLabelFont(42);
   Graph_Graph1008->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1008->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1008->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1008->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1008);
   
   gre->Draw("p");
   
   Double_t Graph3_fx1009[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph3_fy1009[4] = {
   0.9785386,
   0.990724,
   1,
   0.9837067};
   Double_t Graph3_fex1009[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph3_fey1009[4] = {
   0.007475091,
   0.01452852,
   0.02204371,
   0.003490674};
   gre = new TGraphErrors(4,Graph3_fx1009,Graph3_fy1009,Graph3_fex1009,Graph3_fey1009);
   gre->SetName("Graph3");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);

   ci = TColor::GetColor("#0066cc");
   gre->SetLineColor(ci);
   gre->SetLineWidth(2);

   ci = TColor::GetColor("#0066cc");
   gre->SetMarkerColor(ci);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1009 = new TH1F("Graph_Graph1009","Graph",100,20,500);
   Graph_Graph1009->SetMinimum(0.85);
   Graph_Graph1009->SetMaximum(1.1);
   Graph_Graph1009->SetDirectory(0);
   Graph_Graph1009->SetStats(0);
   Graph_Graph1009->SetLineStyle(0);
   Graph_Graph1009->SetMarkerStyle(20);
   Graph_Graph1009->GetXaxis()->SetTitle("p_{T}  [GeV]");
   Graph_Graph1009->GetXaxis()->SetMoreLogLabels();
   Graph_Graph1009->GetXaxis()->SetNoExponent();
   Graph_Graph1009->GetXaxis()->SetLabelFont(42);
   Graph_Graph1009->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1009->GetXaxis()->SetLabelSize(0.065);
   Graph_Graph1009->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1009->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1009->GetXaxis()->SetTitleFont(42);
   Graph_Graph1009->GetYaxis()->SetTitle("Data / MC ");
   Graph_Graph1009->GetYaxis()->SetLabelFont(42);
   Graph_Graph1009->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1009->GetYaxis()->SetLabelSize(0.065);
   Graph_Graph1009->GetYaxis()->SetTitleSize(0.065);
   Graph_Graph1009->GetYaxis()->SetTitleFont(42);
   Graph_Graph1009->GetZaxis()->SetLabelFont(42);
   Graph_Graph1009->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1009->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1009->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1009->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1009);
   
   gre->Draw("p");
   
   Double_t Graph4_fx1010[4] = {
   32.5,
   300,
   87.5,
   60};
   Double_t Graph4_fy1010[4] = {
   0.9703628,
   0.9934277,
   0.9939241,
   0.9786368};
   Double_t Graph4_fex1010[4] = {
   12.5,
   200,
   12.5,
   15};
   Double_t Graph4_fey1010[4] = {
   0.006701529,
   0.003502645,
   0.01072893,
   0.002330936};
   gre = new TGraphErrors(4,Graph4_fx1010,Graph4_fy1010,Graph4_fex1010,Graph4_fey1010);
   gre->SetName("Graph4");
   gre->SetTitle("Graph");
   gre->SetFillColor(1);
   gre->SetLineWidth(2);
   gre->SetMarkerStyle(20);
   
   TH1F *Graph_Graph1010 = new TH1F("Graph_Graph1010","Graph",100,20,500);
   Graph_Graph1010->SetMinimum(0.85);
   Graph_Graph1010->SetMaximum(1.1);
   Graph_Graph1010->SetDirectory(0);
   Graph_Graph1010->SetStats(0);
   Graph_Graph1010->SetLineStyle(0);
   Graph_Graph1010->SetMarkerStyle(20);
   Graph_Graph1010->GetXaxis()->SetTitle("p_{T}  [GeV]");
   Graph_Graph1010->GetXaxis()->SetMoreLogLabels();
   Graph_Graph1010->GetXaxis()->SetNoExponent();
   Graph_Graph1010->GetXaxis()->SetLabelFont(42);
   Graph_Graph1010->GetXaxis()->SetLabelOffset(0.007);
   Graph_Graph1010->GetXaxis()->SetLabelSize(0.065);
   Graph_Graph1010->GetXaxis()->SetTitleSize(0.06);
   Graph_Graph1010->GetXaxis()->SetTitleOffset(1.2);
   Graph_Graph1010->GetXaxis()->SetTitleFont(42);
   Graph_Graph1010->GetYaxis()->SetTitle("Data / MC ");
   Graph_Graph1010->GetYaxis()->SetLabelFont(42);
   Graph_Graph1010->GetYaxis()->SetLabelOffset(0.007);
   Graph_Graph1010->GetYaxis()->SetLabelSize(0.065);
   Graph_Graph1010->GetYaxis()->SetTitleSize(0.065);
   Graph_Graph1010->GetYaxis()->SetTitleFont(42);
   Graph_Graph1010->GetZaxis()->SetLabelFont(42);
   Graph_Graph1010->GetZaxis()->SetLabelOffset(0.007);
   Graph_Graph1010->GetZaxis()->SetLabelSize(0.05);
   Graph_Graph1010->GetZaxis()->SetTitleSize(0.06);
   Graph_Graph1010->GetZaxis()->SetTitleFont(42);
   gre->SetHistogram(Graph_Graph1010);
   
   gre->Draw("p");
   TLine *line = new TLine(20,1,500,1);
   line->SetLineStyle(2);
   line->SetLineWidth(2);
   line->Draw();
   totopT_do->Modified();
   totopT->cd();
   
   TLegend *leg = new TLegend(0.65,0.48,0.95,0.6,NULL,"brNDC");
   leg->SetBorderSize(0);
   leg->SetTextFont(62);
   leg->SetTextSize(0.025);
   leg->SetLineColor(1);
   leg->SetLineStyle(1);
   leg->SetLineWidth(1);
   leg->SetFillStyle(1001);
   TLegendEntry *entry=leg->AddEntry("Graph4","0.000 #leq | #eta | #leq  0.500","PL");
   entry->SetLineColor(1);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);
   entry->SetMarkerColor(1);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph0","0.500 #leq | #eta | #leq  1.000","PL");

   ci = TColor::GetColor("#999999");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);

   ci = TColor::GetColor("#999999");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph1","1.000 #leq | #eta | #leq  1.444","PL");

   ci = TColor::GetColor("#cc0000");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);

   ci = TColor::GetColor("#cc0000");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph2","1.566 #leq | #eta | #leq  2.000","PL");

   ci = TColor::GetColor("#993333");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);

   ci = TColor::GetColor("#993333");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   entry=leg->AddEntry("Graph3","2.000 #leq | #eta | #leq  2.500","PL");

   ci = TColor::GetColor("#0066cc");
   entry->SetLineColor(ci);
   entry->SetLineStyle(1);
   entry->SetLineWidth(2);

   ci = TColor::GetColor("#0066cc");
   entry->SetMarkerColor(ci);
   entry->SetMarkerStyle(20);
   entry->SetMarkerSize(1);
   entry->SetTextFont(62);
   leg->Draw();
   TLatex *   tex = new TLatex(0.98,0.956,"36.3 fb^{-1} (13 TeV) 2017");
tex->SetNDC();
   tex->SetTextAlign(31);
   tex->SetTextFont(42);
   tex->SetTextSize(0.033);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.1587,0.915425,"CMS");
tex->SetNDC();
   tex->SetTextAlign(13);
   tex->SetTextFont(61);
   tex->SetTextSize(0.04125);
   tex->SetLineWidth(2);
   tex->Draw();
      tex = new TLatex(0.1587,0.865925,"Preliminary");
tex->SetNDC();
   tex->SetTextAlign(13);
   tex->SetTextFont(52);
   tex->SetTextSize(0.03135);
   tex->SetLineWidth(2);
   tex->Draw();
   totopT->Modified();
   totopT->cd();
   totopT->SetSelected(totopT);
}
