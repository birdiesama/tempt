import pymel.core as pm

def softMod_group_create():
    selection_list = pm.ls(sl = True)
    softMod_list = pm.listRelatives(selection_list, type = 'softModHandle', ad = True)
    softMod_list = pm.listRelatives(softMod_list, parent = True)
    softMod_list = list(set(softMod_list))

    group = pm.group(em = True, w = True)
    frame = pm.currentTime(query = True)
    frame = int(frame)
    group.rename('softMod_f{0}_1'.format(frame))
    pm.addAttr(group, ln = 'enable', at = 'double', min = 0, max = 2, dv = 1, keyable = True)
    for attr in ('t', 'r', 's'):
        for axis in ('x', 'y', 'z'):
            pm.setAttr('{0}.{1}{2}'.format(group.nodeName(), attr, axis), lock = True, keyable = False, channelBox = False)

    pm.parent(selection_list, group)
    
    for softMod in softMod_list:
        group.enable >> softMod.Envelope

softMod_group_create()
