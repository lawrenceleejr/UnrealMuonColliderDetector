import ROOT
# import edm4hep
import uproot
# import bpy
import sys

# muonFile = uproot.open("muonGun_pT_250_1000_reco_3030.edm4hep.root")
# muonTree = muonFile['events']
# electronFile = uproot.open("electronGun_pT_0_50_reco_1360.edm4hep.root")
# electronTree = electronFile['events']
inputFile = uproot.open("nuGun_reco_v0A.edm4hep.root")
inputTree = inputFile['events']
# print(muonTree.keys())

# print([x for x in muonTree.keys() if "EndcapCollection" in x])
# sys.exit()

# branches = muonTree.arrays()
# vertices = branches[]

ievent = 0
xlist = []
ylist = []
zlist = []
elist = []
postScalelist = []



def postScale(postScalelist,thing,iCollection):
    if "Vertex" in iCollection:
        postScalelist += list([0.1]*len(thing))
    elif "Inner" in iCollection:
        postScalelist += list([0.1]*len(thing))
    elif "Outer" in iCollection:
        postScalelist += list([0.1]*len(thing))
    elif "Yoke" in iCollection:
        postScalelist += list([1]*len(thing))
    else:
        postScalelist += list([1.]*len(thing))

    return

def findThreshold(iCollection):
    if "Vertex" in iCollection:
        return 1e-6
    # elif "VertexEndcap" in iCollection:
    #     return 1e-6
    elif "Inner" in iCollection:
        return 1e-6
    elif "Outer" in iCollection:
        return 1e-6
    elif "Cal" in iCollection:
        return 1e-5
    elif "Yoke" in iCollection:
        return 0
    else:
        return 1e-6



# for ievent in []:#[6,7]:

#     for iCollection in [
#             "VertexBarrelCollection",
#             "InnerTrackerBarrelCollection",
#             "OuterTrackerBarrelCollection",
#             "ECalBarrelCollection",
#             "HCalBarrelCollection",
#             "YokeBarrelCollection"
#             ]:
#         x = muonTree[f'{iCollection}/{iCollection}.position.x'].arrays()[ievent]
#         y = muonTree[f'{iCollection}/{iCollection}.position.y'].arrays()[ievent]
#         z = muonTree[f'{iCollection}/{iCollection}.position.z'].arrays()[ievent]

#         try:
#             e = muonTree[f'{iCollection}/{iCollection}.EDep'].arrays()[ievent]
#         except:
#             e = muonTree[f'{iCollection}/{iCollection}.energy'].arrays()[ievent]

#         # if "Yoke" in iCollection:
#         #     e *= 100
#         # print(x,y,z)

#         xlist += list(x[x.fields[0]]/1000.)
#         ylist += list(y[y.fields[0]]/1000.)
#         zlist += list(z[z.fields[0]]/1000.)
#         if "Yoke" in iCollection:
#             elist += list(e[e.fields[0]]/1.)
#         else:
#             elist += list(e[e.fields[0]]/1000.)


# for ievent in [5]:#[7,9]:

#     for iCollection in [
#             "VertexBarrelCollection",
#             "InnerTrackerBarrelCollection",
#             "OuterTrackerBarrelCollection",
#             "ECalBarrelCollection",
#             "HCalBarrelCollection",
#             "YokeBarrelCollection"
#             ]:
#         x = electronTree[f'{iCollection}/{iCollection}.position.x'].arrays()[ievent]
#         y = electronTree[f'{iCollection}/{iCollection}.position.y'].arrays()[ievent]
#         z = electronTree[f'{iCollection}/{iCollection}.position.z'].arrays()[ievent]

#         try:
#             e = electronTree[f'{iCollection}/{iCollection}.EDep'].arrays()[ievent]
#         except:
#             e = electronTree[f'{iCollection}/{iCollection}.energy'].arrays()[ievent]


#         # print(x,y,z)

#         xlist += list(x[x.fields[0]]/1000.)
#         ylist += list(y[y.fields[0]]/1000.)
#         zlist += list(z[z.fields[0]]/1000.)
#         if "Yoke" in iCollection:
#             elist += list(e[e.fields[0]]/1.)
#         else:
#             elist += list(e[e.fields[0]]/1000.)


for ievent in [0]:#[7,9]:

    for iCollection in [
            # "VertexBarrelCollection",
            # "InnerTrackerBarrelCollection",
            # "OuterTrackerBarrelCollection",
            # "ECalBarrelCollection",
            # "HCalBarrelCollection",
            "YokeBarrelCollection",
            # "VertexEndcapCollection",
            # "InnerTrackerEndcapCollection",
            # "OuterTrackerEndcapCollection",
            # "ECalEndcapCollection",
            # "HCalEndcapCollection",
            "YokeEndcapCollection"
            ]:
        print(f"#{iCollection}\nvertices=\\")
        x = inputTree[f'{iCollection}/{iCollection}.position.x'].arrays()[ievent]
        y = inputTree[f'{iCollection}/{iCollection}.position.y'].arrays()[ievent]
        z = inputTree[f'{iCollection}/{iCollection}.position.z'].arrays()[ievent]

        try:
            e = inputTree[f'{iCollection}/{iCollection}.EDep'].arrays()[ievent]
        except:
            e = inputTree[f'{iCollection}/{iCollection}.energy'].arrays()[ievent]



        xlist = []
        ylist = []
        zlist = []
        elist = []
        postScalelist = []
        # print(x,y,z)

        xlist += list(x[x.fields[0]]/1000.)
        ylist += list(y[y.fields[0]]/1000.)
        zlist += list(z[z.fields[0]]/1000.)
        elist += list(e[e.fields[0]]/1000.)
        postScale(postScalelist,e[e.fields[0]],iCollection)
        # if "Yoke" in iCollection:
        #     elist += list(e[e.fields[0]]/1.)
        # elif "Vertex" in iCollection:
        #     elist += list(e[e.fields[0]]/1.)
        # elif "Vertex" in iCollection:
        #     elist += list(e[e.fields[0]]/1.)
        # else:
        #     elist += list(e[e.fields[0]]/1000.)
        # print(len(xlist))

        # biglist = list(zip(xlist,ylist,zlist)) #blender has a different coord system with z up
        biglist = list(zip(xlist,zlist,ylist,elist,postScalelist))

        threshold = findThreshold(iCollection)

        # biglist = list(filter(lambda x: (x[3] > 1e-6), biglist))
        biglist = list(filter(lambda x: (x[3] > threshold), biglist))
        # for thing in biglist:
        #     print(ROOT.TMath.Hypot(thing[0],thing[1]) )

        # biglist = sorted(biglist, key=lambda x: x[0]**2+x[1]**2+x[2]**2, reverse=False)

        with open(f"{iCollection}_rawhits.txt", 'w') as file:
            for item in biglist:
                file.write(str(item)+"\n")
        # print(biglist)
        print(len(biglist))

        print()
        print()

print(len(biglist))
