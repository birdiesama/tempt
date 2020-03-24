import pymel.core as pm

find = 'polyAverageVertex'
name = 'latissimus_pav_1'

selection = pm.ls(sl = True)[0]

shape_list = selection.getShapes()

shape = None
for s in  shape_list:
    if not s.isIntermediate():
        shape = s

pav_list =  pm.listConnections(shape, type = find)

pav_list.sort()
for each in pav_list:
    if 'polyAverageVertex' in each.nodeName():
        each.rename(name)
