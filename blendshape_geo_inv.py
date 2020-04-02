import pymel.core as pm

selection_list = pm.ls(sl = True)

meshShape_list = pm.listRelatives(selection_list, type = 'mesh', ad = True)
mesh_list = pm.listRelatives(meshShape_list, parent = True)
mesh_list = list(set(mesh_list))

for mesh in mesh_list:
    driver = mesh
    try:
        driven = pm.PyNode(mesh.nodeName().replace('_inputFix', '_abc'))
        blendshape = pm.blendShape(driver, driven, o = 'world', w = [0, 1], envelope = 1)[0]
        blendshape.rename(driver.nodeName() + '_bsn')
    except:
        print mesh.nodeName()
