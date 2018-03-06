library(treespace)
library(phangorn)
library(ape)

tree1 <- rtree(100, rooted=FALSE)
tree2 <- rSPR(tree1, 3)
RF.dist(tree1, tree2)
treedist(tree1, tree2)

setwd("/home/mptree/Documents/Datasets/PhyML_30")
getwd()

true_trees <- read.tree("all_tree")
names(true_trees) <- paste("tree", 1:30, sep = "")

comp_trees <- read.tree("test_run1.newick")
names(comp_trees) <- paste("tree", 1:30, sep = "")

for (tree_no in 1:30){
  true_trees[[tree_no]]
  hi <- RF.dist(true_trees[[tree_no]], comp_trees[[tree_no]])
  print(hi)
  #treedist(true_trees[[tree_no]], comp_trees[[tree_no]])
}



#RAXML_ARB

setwd("/home/mptree/Documents/Datasets/RAxML_ARB/")
getwd()

true_trees <- read.tree("10000_ARB_TREE_5")
comp_trees <- read.tree("test_run1.newick")
RF.dist(true_trees, comp_trees)
#treedist(true_trees, comp_trees)


setwd("/home/mptree/Documents/Datasets/PhyML_30")

true_trees <- read.tree("test_tree")
comp_trees <- read.tree("test_seq.newick")
RF.dist(true_trees, comp_trees)
treedist(true_trees, comp_trees)