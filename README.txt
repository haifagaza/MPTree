Setting up
	* OS: Linux
	* Java: java 1.8.0_161
	* R: R 3.4.3

Dataset:
	* We created a python script that randomly took 30 datasets from PhyML containing 5000 datasets  with 40 taxa of 500bp length each
	* We took a real data alignment from RAxML conatining 10 000 taxa with 1217bp length

Testing:
	* R provides a package to obtain Robinson-Foulds distance.
	* Packages: treespace, ape, phangorn

Directory
1. distance_comparison: R files for RF distance
2. ptree_eclipse: working code for modification, setup eclipse worspace to obtain ptree.jar file
3. PTreeRelease_1_2: move modified ptree.jar here for test run, 
					Input datasets: 10000_arb_mod and phyml_30 
4. scripts: code used for parsing input and all other input output manipulation

