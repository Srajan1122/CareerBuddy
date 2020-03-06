import anytree
from anytree import Node, RenderTree,search
from anytree import AsciiStyle, PreOrderIter
from anytree.exporter import DotExporter
from anytree.dotexport import RenderTreeGraph


sixth = Node("Sixth")
seventh = Node("Seventh",avgTime = 1, parent=sixth)
eigth = Node("Eigth",avgTime = 1, parent=seventh)
ninth = Node("Ninth",avgTime = 1, parent=eigth)
tenth = Node("Tenth",avgTime = 1, parent=ninth)
diploma = Node("Diploma",avgTime = 3, parent=tenth)
licAgent = Node("L.I.C Agent",avgTime = -1, parent=tenth)
defence = Node("Defence",avgTime = 5, parent=tenth)
iti = Node("I.T.I",avgTime = 2, parent=tenth)
hsc = Node("H.S.C",avgTime = 2, parent=tenth)
music = Node("Diploma in Music",avgTime = 2, parent=tenth)
mscit = Node("MS-CIT",avgTime = 3, parent=tenth)
dataEntry = Node("Data Entry Operator",avgTime = -1 , parent=mscit)

commerce = Node("Commerce",avgTime = -1 , parent=hsc)
science = Node("Science",avgTime = -1 , parent=hsc)
arts = Node("Arts",avgTime = -1 , parent=hsc)
dipTravel = Node("Diploma in Travel and Tourism",avgTime = 2 , parent=hsc)
licAgent = Node("L.I.C Agent",avgTime = 2 , parent=hsc)
pilot = Node("Pilot",avgTime = -1 , parent=hsc)
hotelMgmt = Node("Hotel Management",avgTime = 3 , parent=hsc)

#Commerce
cA = Node("C.A.",avgTime = -1 , parent=commerce)
bcom = Node("B.Com",avgTime = 3 , parent=commerce)
bba = Node("B.B.A",avgTime = 3 , parent=commerce)
csFoundation = Node("C.S Foundation",avgTime = 3 , parent=commerce)

# commerce bcom
mba = Node("M.B.A",avgTime = 2, parent=bcom)
bankExam = Node("Bank Exam",avgTime = 2, parent=bcom)
llb = Node("L.L.B",avgTime = 2, parent=bcom)
ima = Node("Indian Military Academy",avgTime = 2, parent=bcom)

mba = Node("M.B.A",avgTime = 2,parent = bba)

# science
pcmb = Node("PCMB",avgTime = -1 , parent = science)
pcb = Node("PCB",avgTime = -1 , parent = science)
pcm = Node("PCM",avgTime = -1 , parent = science)
dEd = Node("D.Ed",avgTime = 2 , parent = science)

# science pcmb
bscAgri = Node("B.Sc Agriculture",avgTime = 3 , parent = pcmb)
bscBio = Node("B.Sc Biotech",avgTime = 3 , parent = pcmb)

# science pcm
nda = Node("N.D.A", avgTime = 3 , parent = pcm)
barch = Node("B.Arch", avgTime = 3 , parent = pcm)
be = Node("B.E. / B.Tech", avgTime = 4 , parent = pcm)
bscPhy = Node("B.Sc Physics" , avgTime = 3 , parent = pcm)
bca = Node("B.C.A" , avgTime = 3 , parent = pcm)

# science pcb
bams =  Node("B.A.M.S", avgTime = 5 , parent = pcb)
bhms =  Node("B.H.M.S", avgTime = 5 , parent = pcb)
mbbs =  Node("M.B.B.S", avgTime = 5 , parent = pcb)
bscNursing =  Node("B.Sc Nursing", avgTime = 4 , parent = pcb)
bmlt =  Node("B.M.L.T", avgTime = 5 , parent = pcb)

# arts
dEd = Node("D.Ed" , avgTime = 2 , parent = arts)
bsw = Node("B.S.W" , avgTime = 3 , parent = arts)
llb = Node("L.L.B" , avgTime = 2 , parent = arts)
bba = Node("B.B.A" , avgTime = 2 , parent = arts)
callCenter = Node("Call Centre" , avgTime = 2 , parent = arts)
# path = os.path.join(settings.MODEL_ROOT, 'rf')
# with open(path, 'wb') as file:
#     joblib.dump(rf, 'rf.pkl')
#     joblib.dump(data, 'data.pkl')
# many nodes
mba = Node("M.B.A", avgTime = 2 , prt = 'bba bscAgri bscBio' , parent = bba)

a =[sixth,seventh,eigth,ninth,tenth,diploma,licAgent,defence,iti,hsc,music,mscit,dataEntry,commerce,science,arts,dipTravel,licAgent,pilot,hotelMgmt,cA,bcom,csFoundation,bankExam,ima,pcmb,pcb,pcm,dEd,bscAgri,bscBio,nda,barch,be,bscPhy,bca,bams,bhms,mbbs,bscNursing,bmlt,bsw,callCenter,mba,bba,llb ]
# a = [be,bca]
for pre, fill, node in RenderTree(sixth):
    print("%s%s" % (pre, node.name))