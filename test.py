import trees
import treePlotter
myMat, labels = trees.createDataSet()
# print(trees.calcShannonEnt(myMat))


# treePlotter.createPlot()

mytree = treePlotter.retrieveTree(0)
treePlotter.createPlot(mytree)