import treePlotter
import trees

fr = open('lenses.txt')
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
lenseTree = trees.createTree(lenses, lensesLabels)

print lenseTree