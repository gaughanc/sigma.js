import random
from create_lin_list import create_lin_list

#create or define all needed lists
lins = create_lin_list()
genera = ['Bacteroides', 'Prevotella', 'Akkermansia', 'Anaerostripes', 'Anaerotruncas', 'Barnesiella', 'Blautia', 'Roseburia', 'Alloprevotella', 'Porphyromonas', 'Paraprevotella', 'Parabacteroides', 'Oscillibacter', 'Odoribacter', 'Faecalibacterium', 'Enterobacter', 'Shuttleworthia', 'Sediminibacterium', 'Peptoniphilus', 'Moryella', 'Holdemania', 'Gordonibacter', 'Dorea', 'Sutterella', 'Sporobacter', 'Pseudoflavonifractor', 'Flavonifractor', 'Achromobacter', 'Aerococcus', 'Catenibacterium', 'Collinsella', 'Aggregatibacter', 'Anaerococcus', 'Succinivibrio', 'Lachnospira', 'Parasutterella', 'Paralactobacillus', 'Oribacterium', 'Ochrobactrum', 'Murdochiella', 'Mogibacterium', 'Megasphaera', 'Hallella', 'Johnsonella', 'Granulicatella', 'Gemmiger', 'Gardnerella', 'Facklamia', 'Enterococcus', 'Dialister', 'Delftia', 'Cronobacter', 'Citrobacter', 'Chryseobacterium', 'Centipeda', 'Butyricicoccus', 'Bulleidia', 'Brevundimonas', 'Anaeroglobus', 'Arthrobacter', 'Atopobium', 'Bacillus', 'Butyricimonas', 'Deinococcus', 'Helicobacter', 'Microbacterium', 'Pseudobutyrivibrio', 'Schwartzia', 'Succiniclasticum', 'Tannerella', 'Alistipes', 'Catonella', 'Kingella', 'Eremococcus', 'Variovorax', 'Slackia', 'Pyramidobacter', 'Abiotrophia', 'Bordetella', 'Parascardovia', 'Olsenella', 'Jonquetella', 'Xylanibacter', 'Eikenella', 'Christensenella', 'Acidaminococcus', 'Oribaculum', 'Oribaculum', 'Cellulosimicrobium', 'Enterorhabdus', 'Anarosalibacter', 'Murimonas', 'Terrisporobacter', 'Intestinimonas', 'Stenotrophomonas', 'Aminobacter', 'Bradyrhizobium', 'Curvibacter', 'Curvibacter', 'Herbaspirillum', 'Turicibacter', 'Rothia', 'Pedobacter', 'Parvibacter', 'Acidovorax', 'Aeromicrobium', 'Afipia', 'Aquabacterium', 'Aurantimonas', 'Azoarcus', 'Xanthomonas', 'Papillibacter', 'Lachnobacterium', 'Azospira', 'Beutenbergia', 'Micrococcus', 'Polaromonas', 'Pseudoxanthomonas', 'Psychrobacter', 'Sphingobium', 'Sphingomonas', 'Sphingopyxis', 'Sulfuritalea', 'Tsukamurella', 'Undibacterium', 'Bosea', 'Brevibacillus', 'Caulobacter', 'Comamonas', 'Craurococcus', 'Cupriavidus', 'Devosia', 'Dietzia', 'Duganella', 'Dyadobacter', 'Enhydrobacter', 'Hoeflea', 'Hydrotalea', 'Janthinobacterium', 'Bifidobacterium', 'Kocuria', 'Limnobacter', 'Mesorhizobium', 'Methylophilus', 'Methyloversatilis', 'Microlunatus', 'Niastella', 'Novosphingobium', 'Olivibacter', 'Paracoccus', 'Patulibacter', 'Wautersiella', 'Actinobaculum', 'Anaerotruncus']
species = [['Bacteroides vulgatus', 'Bacteroides acidifaciens', 'Bacteroides caecimuris', 'Bacteroides ovatus', 'Bacteroides xylanisolvens', 'Bacteroides amylophilus', 'Bacteroides barnesiae', 'Bacteroides bivius', 'Bacteroides buccae', 'Bacteroides caccae', 'Bacteroides caecicola', 'Bacteroides caecigallinarum', 'Bacteroides cellulosilyticus', 'Bacteroides cellulosolvens', 'Bacteroides chinchillae', 'Bacteroides clarus', 'Bacteroides coagulans', 'Bacteroides coprocola', 'Bacteroides coprophilus', 'Bacteroides coprosuis', 'Bacteroides corporis', 'Bacteroides disiens', 'Bacteroides distasonis', 'Bacteroides dorei', 'Bacteroides eggerthii', 'Bacteroides faecichinchillae', 'Bacteroides faecis', 'Bacteroides finegoldii', 'Bacteroides fluxus', 'Bacteroides forsythus', 'Bacteroides gallinaceum', 'Bacteroides gallinarum', 'Bacteroides gingivalis', 'Bacteroides gracilis', 'Bacteroides graminisolvens', 'Bacteroides heparinolyticus', 'Bacteroides intermedius', 'Bacteroides intestinalis', 'Bacteroides levii', 'Bacteroides loescheii', 'Bacteroides luti', 'Bacteroides massiliensis', 'Bacteroides microfusus', 'Bacteroides multiacidus', 'Bacteroides oleiciplenus', 'Bacteroides oralis', 'Bacteroides oris', 'Bacteroides oulorum'], ['Prevotella amnii', 'Prevotella copri'], ['Akkermansia muciniphila'], ['Anaerostripes butyraticus'], [], ['Barnesiella viscericola'], ['Blautia faecis', 'Blautia wexlerae', 'Blautia caecimuris', 'Blautia coccoides', 'Blautia stercoris', 'Blautia wexlerae'], ['Roseburia cecicola', 'Roseburia faecis', 'Roseburia hominis', 'Roseburia inulinivorans'], ['Alloprevotella tannerae', 'Alloprevotella rava'], ['Porphyromonas asaccharolytica', 'Porphyromonas gingivalis'], ['Paraprevotella clara'], ['Parabacteroides distasonis', 'Parabacteroides goldsteinii', 'Parabacteroides merdae', 'Parabacteroides johnsonii'], ['Oscillibacter valericigenes', 'Oscillibacter ruminantium'], ['Odoribacter denticanis'], ['Faecalibacterium prausnitzii'], [], ['Shuttleworthia satelles'], ['Sediminibacterium salmoneum'], ['Peptoniphilus asaccharolyticus'], ['Moryella indoligenes'], ['Holdemania filiformis'], ['Gordonibacter pamelaeae'], ['Dorea formicigenerans', 'Dorea longicatena'], ['Sutterella wadsworthensis'], ['Sporobacter termitidis'], ['Pseudoflavonifractor capillosus'], ['Flavonifractor plautii'], ['Achromobacter xylosoxidans'], ['Aerococcus christensenii'], ['Catenibacterium mitsuokai'], ['Collinsella aerofaciens'], ['Aggregatibacter actinomycetemcomitans'], ['Anaerococcus prevotii', 'Anaerococcus tetradius', 'Anaerococcus hydrogenalis', 'Anaerococcus lactolyticus', 'Anaerococcus octavius', 'Anaerococcus vaginalis'], ['Succinivibrio dextrinosolvens'], ['Lachnospira multipara'], ['Parasutterella excrementihominis'], ['Paralactobacillus selangorensis'], ['Oribacterium sinus'], ['Ochrobactrum anthropi'], ['Murdochiella asaccharolytica'], ['Mogibacterium pumilum', 'Mogibacterium vescum'], ['Megasphaera micronuciformis'], ['Hallella seregens'], ['Johnsonella ignava'], ['Granulicatella adiacens', 'Granulicatella elegans', 'Granulicatella balaenopterae'], [], ['Gardnerella vaginalis'], ['Facklamia hominis'], ['Enterococcus faecalis', 'Enterococcus faecium', 'Enterococcus gallinarum', 'Enterococcus hirae'], ['Dialister pneumosintes'], ['Delftia acidovorans'], [], [], [], ['Centipeda periodontii'], ['Butyricicoccus pullicaecorum'], ['Bulleidia extructa'], ['Brevundimonas diminuta', 'Brevundimonas vesicularis'], ['Anaeroglobus geminatus'], ['Arthrobacter agilis'], ['Atopobium deltae'], ['Bacillus thermoamylovorans'], ['Butyricimonas synergistica', 'Butyricimonas virosa'], [], ['Helicobacter pylori', 'Helicobacter mustelae'], ['Microbacterium immunditiarum'], ['Pseudobutyrivibrio ruminis'], ['Schwartzia succinivorans'], ['Succiniclasticum ruminis'], ['Tannerella forsythia'], ['Alistipes indistinctus', 'Alistipes inops', 'Alistipes onderdonkii', 'Alistipes shahii'], ['Catonella morbi'], ['Kingella orale'], ['Eremococcus coleocola'], ['Variovorax paradoxus'], [], ['Pyramidobacter piscolens'], [], ['Bordetella petrii'], [], ['Olsenella uli'], ['Jonquetella antrhopi'], ['Xylanibacter oryzae'], ['Eikenella corrodens'], ['Christensenella minuta'], ['Acidaminococcus fermentans'], ['Oribaculum catoniae'], ['Oribaculum catoniae'], ['Cellulosimicrobium cellulans'], ['Enterorhabdus mucosicola', 'Enterorhabdus caecimuris'], [], ['Murimonas intestini'], [], ['Intestinimonas butyriciproducens'], ['Stenotrophomonas maltophilia'], ['Aminobacter aminovorans', 'Aminobacter aganoensis'], ['Bradyrhizobium japonicum'], ['Curvibacter gracilis', 'Curvibacter gracilis'], ['Curvibacter gracilis', 'Curvibacter gracilis'], ['Herbaspirillum seropedicae'], ['Turicibacter sanguinis'], ['Rothia aeria', 'Rothia nasimurium'], ['Pedobacter heparinus'], ['Parvibacter caecicola'], ['Acidovorax  facilis'], ['Aeromicrobium'], ['Afipia felis'], ['Aquabacterium commune'], ['Aurantimonas coralicida'], ['Azoarcus indigens'], [], ['Papillibacter cinnamivorans'], ['Lachnobacterium bovis'], ['Azospira oryzae'], ['Beutenbergia cavernae'], [], ['Polaromonas vacuolata'], [], ['Psychrobacter immobilis'], ['Sphingobium yanoikuyae'], [], ['Sphingopyxis macrogoltabida'], ['Sulfuritalea hydrogenivorans'], ['Tsukamurella paurometabolum'], ['Undibacterium pigrum'], ['Bosea thiooxidans'], [], [], ['Comamonas terrigena'], ['Craurococcus roseus'], [], ['Devosia riboflavina'], ['Dietzia maris'], ['Duganella zoogloeoides'], ['Dyadobacter fermentans'], ['Enhydrobacter aerosaccus'], ['Hoeflea marina'], ['Hydrotalea flava'], [], ['Bifidobacterium dentium', 'Bifidobacterium animalis'], ['Kocuria rosea'], ['Limnobacter thiooxidans'], [], ['Methylophilus methylotrophus'], ['Methyloversatilis universalis'], ['Microlunatus phosphovorus'], ['Niastella koreensis'], [], ['Olivibacter sitiensis'], [], ['Patulibacter minatonensis'], ['Wautersiella falsenii'], ['Actinobaculum suis'], ['Anaerotruncus colihominis', 'Anaerotruncus colihominis']]
catalase = [['not indicated', 'not indicated', 'not indicated', 'not indicated', 'catalase negative', 'not indicated', 'catalase negative', 'not indicated', 'not indicated', 'not indicated', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'not indicated', 'not indicated', 'catalase negative', 'not indicated', 'catalase negative', 'not indicated', 'not indicated', 'not indicated', 'not indicated', 'not indicated', 'catalase negative', 'catalase negative', 'not indicated', 'not indicated', 'not indicated', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'not indicated', 'catalase negative', 'not indicated', 'not indicated', 'catalase negative', 'not indicated', 'catalase negative', 'catalase negative', 'catalase negative', 'not indicated', 'not indicated', 'catalase negative', 'not indicated', 'not indicated'], ['not indicated', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'not indicated', 'catalase negative', 'not indicated', 'catalase negative', 'catalase negative', 'catalase negative', 'not indicated', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'not indicated', 'catalase negative', 'not indicated', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative', 'catalase negative'], ['not indicated'], ['not indicated'], [], ['catalase negative', 'catalase negative'], ['catalase negative', 'catalase negative', 'not indicated', 'not indicated', 'catalase negative', 'catalase negative'], ['catalase negative', 'catalase negative', 'catalase negative', 'catalase negative'], ['not indicated', 'not indicated'], ['not indicated', 'not indicated'], ['not indicated'], ['catalase positive', 'not indicated', 'catalase negative', 'catalase positive'], ['catalase negative', 'catalase negative'], ['catalase positive'], ['not indicated'], [], ['catalase negative'], ['catalase positive'], ['not indicated'], ['catalase negative'], ['catalase negative'], ['catalase positive'], ['not indicated', 'catalase negative'], ['not indicated'], ['not indicated'], ['not indicated'], ['not indicated'], ['catalase positive'], ['catalase negative'], ['not indicated'], ['not indicated'], ['catalase positive'], ['not indicated', 'not indicated', 'not indicated', 'not indicated', 'not indicated', 'not indicated'], ['not indicated'], ['catalase negative'], ['catalase negative'], ['catalase negative'], ['catalase negative'], ['catalase positive'], ['catalase negative'], ['catalase negative', 'catalase negative'], ['catalase negative'], ['not indicated'], ['catalase negative'], ['catalase negative', 'catalase negative', 'catalase negative'], [], ['not indicated'], ['catalase negative'], ['not indicated', 'not indicated', 'not indicated', 'catalase negative'], ['not indicated', 'not indicated', 'not indicated'], ['catalase positive'], [], [], [], ['not indicated'], ['not indicated'], ['catalase negative'], ['not indicated', 'not indicated'], ['catalase negative'], ['catalase positive'], ['not indicated'], ['catalase positive'], ['catalase negative', 'catalase positive'], [], ['catalase positive', 'catalase positive'], ['catalase positive'], ['not indicated'], ['catalase negative'], ['catalase negative'], ['catalase negative'], ['catalase positive', 'catalase negative', 'catalase negative', 'catalase negative'], ['not indicated'], ['catalase negative'], ['catalase negative'], ['catalase positive'], [], ['catalase negative'], [], ['not indicated'], [], ['catalase negative'], ['catalase negative'], ['catalase negative'], ['catalase negative'], ['catalase negative'], ['not indicated'], ['not indicated'], ['not indicated'], ['catalase positive'], ['catalase negative', 'not indicated'], [], ['not indicated'], [], ['not indicated'], ['not indicated'], ['catalase positive', 'catalase positive'], ['not indicated'], ['catalase positive', 'catalase positive'], ['catalase positive', 'catalase positive'], ['catalase positive'], ['catalase negative'], ['not indicated', 'catalase positive'], ['catalase positive'], ['not indicated'], ['not indicated'], ['catalase positive'], ['catalase positive'], ['catalase negative'], ['catalase positive'], ['catalase positive'], [], ['not indicated'], ['not indicated'], ['catalase positive'], ['catalase positive'], [], ['catalase positive'], [], ['catalase positive'], ['catalase positive'], [], ['catalase positive'], ['catalase negative'], ['catalase positive'], ['not indicated'], ['catalase positive'], [], [], ['catalase positive'], ['catalase positive'], [], ['catalase positive'], ['catalase positive'], ['catalase positive'], ['catalase positive'], ['catalase positive'], ['catalase positive'], ['catalase positive'], [], ['catalase negative', 'catalase negative'], ['catalase positive'], ['not indicated'], [], ['catalase positive'], ['catalase positive'], ['catalase positive'], ['not indicated'], [], ['not indicated'], [], ['catalase positive'], ['not indicated'], ['catalase negative'], ['catalase negative', 'catalase negative']]
catcount = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
nodes = []
edges = []

#define colors
red = "#ec5148"
orange = "#ffce96"
grey = "#e0d8d5"
salmon = "#f28f8a"

#for each genus
for i, genus in enumerate(genera):
    for j, spec in enumerate(species[i]):
        if catalase[i][j] == "catalase positive":
            color = orange
            catcount[i][0] += 1
        elif catalase[i][j] == "catalase negative":
            color = red
            catcount[i][1] += 1
        else:
            color = grey
        #create a node for each of its species
        nodes.append({"id":"sn"+str(i)+str(j), "label":spec, "x":10*i-10+j, "y":random.randint(850,1000), "size":5, "color":color})
        #create an edge from the genus to each of its species
        edges.append({"id":"e"+str(i)+str(j), "source":"gn"+str(i), "target":"sn"+str(i)+str(j),"size":20,"color":salmon})
    if catcount[i][0] > catcount[i][1]:
        color = orange
    if catcount[i][0] < catcount[i][1]:
        color = red
    else:
        color = grey
    #create a node for the genus
    nodes.append({"id":"gn"+str(i), "label":genus, "x":10*i, "y":random.randint(500,800), "size":15, "color":color})
    #for each lineadge
    for lin in lins:
        if len(lin) == 6:
            #if the genus appears
            if lin[5] == genus:
                #if its family does not have a node, create one
                if not any(node["label"] == lin[4] for node in nodes):
                    nodes.append({"id":"fn"+str(i), "label":lin[4], "x":10*i, "y":random.randint(200,400), "size":25, "color":grey})
                #if its order does not have a node, create one
                if not any(node["label"] == lin[3] for node in nodes):
                    nodes.append({"id":"on"+str(i), "label":lin[3], "x":10*i, "y":random.randint(0,150), "size":30, "color":grey})               
                #for each node
                for node in nodes:
                    #if its label is the genus' family, connect the node to the genus
                    if node["label"] == lin[4]:
                        edges.append({"id":"fe"+str(i), "source":"gn"+str(i), "target":node["id"],"size":20,"color":salmon})
                    #if its label is the genus' order, connect the node to the order
                    if node["label"] == lin[3]:
                        edges.append({"id":"oe"+str(i), "source":"gn"+str(i), "target":node["id"],"size":20,"color":salmon})
                break

scripta = """<!-- START SIGMA IMPORTS -->
<script src="../src/sigma.core.js"></script>
<script src="../src/conrad.js"></script>
<script src="../src/utils/sigma.utils.js"></script>
<script src="../src/utils/sigma.polyfills.js"></script>
<script src="../src/sigma.settings.js"></script>
<script src="../src/classes/sigma.classes.dispatcher.js"></script>
<script src="../src/classes/sigma.classes.configurable.js"></script>
<script src="../src/classes/sigma.classes.graph.js"></script>
<script src="../src/classes/sigma.classes.camera.js"></script>
<script src="../src/classes/sigma.classes.quad.js"></script>
<script src="../src/classes/sigma.classes.edgequad.js"></script>
<script src="../src/captors/sigma.captors.mouse.js"></script>
<script src="../src/captors/sigma.captors.touch.js"></script>
<script src="../src/renderers/sigma.renderers.canvas.js"></script>
<script src="../src/renderers/sigma.renderers.webgl.js"></script
<script src="../src/renderers/sigma.renderers.svg.js"></script>
<script src="../src/renderers/sigma.renderers.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.nodes.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.nodes.fast.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.def.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.fast.js"></script>
<script src="../src/renderers/webgl/sigma.webgl.edges.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.labels.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.hovers.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.nodes.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.curve.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edges.curvedArrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.def.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.curve.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.arrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.edgehovers.curvedArrow.js"></script>
<script src="../src/renderers/canvas/sigma.canvas.extremities.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.utils.js"></script>
<script src="../src/renderers/svg/sigma.svg.nodes.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.edges.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.edges.curve.js"></script>
<script src="../src/renderers/svg/sigma.svg.labels.def.js"></script>
<script src="../src/renderers/svg/sigma.svg.hovers.def.js"></script>
<script src="../src/middlewares/sigma.middlewares.rescale.js"></script>
<script src="../src/middlewares/sigma.middlewares.copy.js"></script>
<script src="../src/misc/sigma.misc.animation.js"></script>
<script src="../src/misc/sigma.misc.bindEvents.js"></script>
<script src="../src/misc/sigma.misc.bindDOMEvents.js"></script>
<script src="../src/misc/sigma.misc.drawHovers.js"></script>
<!-- END SIGMA IMPORTS -->
<div id="container">
  <style>
    #graph-container {
      top: 0;
      bottom: 0;
      left: 0;
      right: 0;
      position: absolute;
    }
  </style>
  <div id="graph-container"></div>
</div>

<script>
var g = {
      nodes: [],
      edges: []
    };

// Generate a graph:"""
scriptb = "g.nodes.push(" + str(nodes)[1:-1] + ")"

scriptc = ""

scriptd = "g.edges.push(" + str(edges)[1:-1] + ")"

scripte = """
// Instantiate sigma:
s = new sigma({
  graph: g,
  container: 'graph-container',
});
</script>"""

print(scripta, scriptb, scriptc, scriptd, scripte, sep="\n")
