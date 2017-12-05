#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = "Ahirton Lopes & Rodrigo Pasti"
__copyright__ = "Copyright 2015/2016, Mackenzie University"
__credits__ = ["Ahirton Lopes", "Rodrigo Pasti", "Leandro de Castro"]
__license__ = "None"
__version__ = "1.0"
__maintainer__ = "Ahirton Lopes"
__email__ = "ahirton.xd@gmail.com"
__status__ = "Beta"
"""

import re
import nltk
import math
import numpy
import text_processing as tp

class MetaAttributes(object):
    def __init__(self, text):

        '''
        -----------------------------------------------------------------------------------------------------------------------
        DEFINICAO DOS PARAMETROS DE CONTROLE
        -----------------------------------------------------------------------------------------------------------------------
        '''        

        self.nMaxLengthFreq = 16 
#       OBS1: Tamanho maximo de palavra a ser considerado na frequencia do tamanho de palavras       
        
        tagged = tp.tagging([tp.tokenize([text])[0]])[0]
        text = re.sub("http","", text)
        self.raw = text
        
#        print tagged

        self.PARAGRAPHS = []
        self.SENTENCES = []
        self.WORDS = []
        delimiters = '\n','. \n', '! \n', '?\n', '.\n', '!\n', '?\n', '... \n' #, '... \n'#, ' \n ' #, " .\n", " !\n", ' ?\n'
        regexPattern = '|'.join(map(re.escape, delimiters))
        for paragraph in re.split(regexPattern,self.raw):        
            p = []
#            print ""
#            print paragraph            
#            raw_input(".----------------.FIM DE PARÁGRAFO----------------.")
            #sentences = tp.tokenize_sentence([paragraph])[0]
            for sentence in tp.tokenize_sentence([paragraph])[0]: 
#                print ""
#                print sentence
#                print tp.tagging(tp.tokenize([sentence]))
#                raw_input(".---------------..FIM DE FRASE...------.")
                words = tp.tokenize([sentence])[0]
                words = tp.remove_punctuation([words])[0]
                self.WORDS.extend(words)
                self.SENTENCES.append(sentence)
                p.append(words)
#                print paragraph
#                print sentence
#                print words
#                print self.WORDS
#                raw_input('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            self.PARAGRAPHS.append(p)
            self.C = len(text)
            self.LOWER = MetaAttributes._count_char(text, "^[a-z_-]*$")
            self.UPPER = MetaAttributes._count_char(text, "^[A-Z_-]*$")
            self.NUMBERS = MetaAttributes._count_char(text, "^[\d]*$")
            self.WHITE = MetaAttributes._count_char(text, "^[ ]*$")
            self.TAB = MetaAttributes._count_char(text, "^[\t]*$")
            self.N = len(self.WORDS)
            self.SIZES = []
            self.FREQ = {}
        
        for w in self.WORDS:            
            self.SIZES.append(len(w))
            self.FREQ = dict(nltk.FreqDist(self.WORDS))
            self.V = dict(nltk.FreqDist(self.FREQ.values())) 
            self.VRICH = self.N - len(self.V)
            self.HXLEGO = []
            self.HXDISLEGO = []

        for w, t in self.FREQ.viewitems():
            if t == 1:
                self.HXLEGO.append(w)
            elif t == 2:
                self.HXDISLEGO.append(w)
                
            self.TAGGED = tagged
            self.S = len(self.SENTENCES)
            
            self.pwdictionary = ["abencoada","abencoadas","abencoado","abencoados","abrilhantada",
        "abrilhantadas","abrilhantado","abrilhantados","abundancia","abundante",
        "acertada","acertadas","acertados","aclamada","aclamado","adequada",
        "adequadamente","adequado","admiraveis","admiravel","adorada","adoradas",
        "adorado","adorados","adoranda","adorandas","adorando","adorandos",
        "adoraveis","adoravel","adorei","afortunada","afortunadas","afortunado",
        "afortunados","agradavel","agradavelmente","alcanca","alcancar","alcancou",
        "alegre","alegremente","amada","amadas","amado","amados","amadurecida",
        "amadurecidas","amadurecido","amadurecidos","amaveis","amavel","amigavel",
        "amigavelmente","amorosa","amoroso","amparada","amparado","animada",
        "animadas","animado","animados","animador","animadora","animadoras",
        "animadores","animados","apaixonante","apaixonantes","apaziguador",
        "apaziguadora","apaziguadoras","apaziguadores","aperfeicoa","aperfeicoada",
        "aperfeicoado","aperfeicoar","apreciada","apreciadas","apreciado","apreciador",
        "apreciadora","apreciadoras","apreciadores","apreciados","apreciando",
        "aprimorada","aprimoradas","aprimorado","aprimorados","aprimoramento",
        "apropriada","apropriadas","apropriado","apropriados","aprovada","aprovadas",
        "aprovado","aprovados","arrasou","arrojada","arrojadas","arrojado",
        "arrojados","assertiva","assertivas","assertivo","assertivos","atenciosa",
        "atenciosas","atencioso","atenciosos","atento","atenta","ativada","ativado",
        "ativo","ativa","atraente","atraentes","atrativa","atrativas","atratividade",
        "atrativo","atrativos","aumentar","aumento","auspiciosa","auspiciosas",
        "auspicioso","auspiciosos","autentica","autenticas","autentico","autenticos",
        "autoconfiante","autoconfiantes","autorizado","autorizar","avancando",
        "avanco","avancos","avantajada","avantajado","avantajar","bacana","bacanas",
        "bacano","bacanos","bela","belas","belissima","belissimas","belissimo",
        "belissimos","belo","belos","beneficamente","beneficiado","beneficiando",
        "beneficio","benefico","boa","bom","bondosa","bondosas","bondoso","bondosos",
        "bonita","bonitas","bonito","bonitos","brilhante","brilhantes","briosa",
        "briosas","brioso","briosos","calmo","calma","calorosa","calorosas",
        "caloroso","calorosos"	,"capacitada"	,"capacitadas","capacitado","capacitados",
        "capacitando","capaz","capazes","cariciosa","cariciosas","caricioso",
        "cariciosos","caridosa","caridosas","caridoso","caridosos","carinhosa",
        "carinhosas"	,"carinhoso","carinhosos","carismatica","carismaticas",
        "carismatico","carismaticos","cativante","cativantes","cavalheiresca",
        "cavalheirescas","cavalheiresco","cavalheirescos","cavalheiro","cavalheiros",
        "celebre","celebres","certa","certeira","certeiro","certissimo","certo",
        "charmosa","charmosas","charmoso","charmosos","chefia","cheirosa","cheirosas",
        "cheiroso","cheirosos","chique","chiques","civilizada"	,"civilizadas",
        "civilizado","civilizados","celebre","coerente","coerentes","colabora",
        "colaboracao","colaboracoes","colaborado","colaborador","colaboradora",
        "colaboradores","colaboradoras","colaborando","colaborar","colaborativa",
        "competente","competentes","complementados","compreensiva","compreensivo",
        "conceituada","conceituadas","conceituado","conceituados","conclusivamente",
        "conclusivo","conducente","confianca","confiante","confiantes","confiaveis",
        "confiavel","confortador","confortadora","confortadoras","confortadores",
        "confortante","confortantes","conquistamos","conquistas","consagrada",
        "consagradas",	"consagrado",	"consagrados","consecucao","conseguida",
        "construtiva",	"construtivamente","construtivas","construtivo","construtivo",
        "construtivos","contente","convidativa","convidativas","convidativo",
        "convidativos","convincente","convincentes","convivente","conviventes",
        "corajosa","corajosas",	"corajoso","corajosos","cortes","cortesia","criador",	
        "criativa","criativamente","criativas","criatividade","criativo","criativos",	
        "cuidadosa","cuidadosas","cuidadoso","cuidadosos","culta","cultas",
        "cumprimentos","curti",	"curtida","curtidas","curtido",	"curtidos","dedicada",
        "dedicadas","dedicado","dedicados","delicia","delicias","deliciosamente",
        "deliciosa","deliciosas","delicioso","deliciosos","demais","desejado",
        "desejada","desejavel","desfrutado","desfrutar","deslumbrante","deslumbrantes",
        "despachada","despachadas","despachado","despachados","destemido","destinado",
        "destinada","determinado","diligente","diligentemente","disciplinada",
        "disciplinadas","disciplinado","disciplinados","discreta","discretas",
        "discreto","discretos","distincao","distincoes","distinto","distinta",
        "distintamente","distintivo","divertida","divertidas","divertido",
        "divertido","divertidos","divina","divinais","divinal","divinas","divino",
        "divinos","doce","educado","educada"	,"educados","educadas","educativa",
        "educativas","educativo","educativos","efetivo","eficaz","eficazes",
        "eficiente","eficientes","eficientemente","efusiva","efusivas","efusivo",
        "efusivos","elegante","elegantes","eletrizante","eletrizantes","elogio",
        "elogiou","elogiosa","elogiosas","elogioso","elogiosos","elogiado",
        "elogiada","elucidativa","elucidativas","elucidativo","elucidativos",
        "emocionado","emocionados","emocionadas","emocionada","emocionante",
        "empenhada","empenhadas","empenhado","empenhados","empolgada","empolgadas",
        "empolgado","empolgados","encantado","encantada","encantador","encantadora",
        "encantadoramente","encantadoras","encantadores","encorajada","encorajadas",
        "encorajado","encorajador","encorajadora","encorajadoras","encorajadores",
        "encorajados","engenhoso","engenhosa","engracado","engracada","entusiasmada",
        "entusiasmado","entusiasmante","entusiasmantes","entusiasticamente",
        "entusiasta","entusiastas","equilibrada","equilibradas","equilibrado",
        "equilibrados","erudita","eruditas","erudito","eruditos","esbelta",
        "esbeltas","esbelto","esbeltos","esclarecedor","esclarecedora",
        "esclarecedoras","esclarecedores","esclarecida","esclarecidas","esclarecido",
        "escolarizada","escolarizadas","escolarizado","escolarizados","esforcado",
        "esperto","espetacular","espetacularmente","espetaculares","esplendida",
        "esplendida","esplendido","esplendorosa","esplendorosas","esplendoroso",
        "esplendorosos","estabilizado","estabilizada","estavel","estupenda",
        "estupendas","estupendo","estupendos","excelente","excelentes","excepcionais",
        "excepcional","excepcionalmente","excitante","excitantes","exemplar","exemplares",
        "experta","expertas","experto","expertos","expressiva","expressivas","expressivo",
        "expressivos","extraordinaria","extraordinarias","extraordinario",
        "extraordinarios","fabulosa","fabulosas","fabuloso","fabulosos","facil",
        "facilimo","facilmente","fantastica","fantasticas","fantastico","fantasticos",
        "fascinante","fascinantes","favoravel","favoravelmente","favorecido","favorecida",
        "favorito","favorita","favoritos","favoritas","feliz","felizarda","felizardas",
        "felizardo","felizardos","felizes","fenomenais","fenomenal","foda","fodas",
        "formidaveis","formidavel","formosa","formosas","formoso","formosos","forte",
        "fortissima","fortissimo","fortalecido","fortalecida","geniais","genial",
        "genia","genio","genios","genias","gentil","gentis","glamurosa","glamurosas",
        "glamuroso","glamurosos","gostosa","gostosas","gostoso","gostosos","graciosa",
        "graciosas","gracioso","graciosos","grandiosa","grandiosas","grandioso",
        "grandiosos","grandemente","grandiosamente","habilidosa","habilidosas",
        "habilidoso","habilidosos","habilitada","habilitadas","habilitado","habilitados",
        "harmoniosa","harmoniosas","harmonioso","harmoniosos","hiperculta","hipercultas",
        "hiperculto","hipercultos","hiperdotada","hiperdotadas","hiperdotado","hiperdotados",
        "honesta","honestas","honesto","honestos","honoraveis","honoravel","honrada",
        "honradas","honrado","honrados","honrosa","honrosas","honroso","honrosos",
        "hospitaleira","hospitaleiras","hospitaleiro","hospitaleiros","idolatrada",
        "idolatradas","idolatrado","idolatrados","ideal","iluminada","iluminadas",
        "iluminado","iluminados","ilustre","ilustres","imaculada","imaculadas",
        "imaculado","imaculados","imortalizada","imortalizadas","imortalizado",
        "imortalizados","impecavel","imperdivel","impressionante","impressionantemente",
        "incansaveis","incansavel","incansavelmente","incomparavel","incrivelmente",
        "influente","influentes","inovador","inovadora","inovadoras","inovadores",
        "inovando","inquestionaveis","inquestionavel","insigne","insignes","inspirada",
        "inspiradas","inspirado","inspirador","inspiradora","inspiradoras","inspiradores",
        "inspirados","instrutiva","instrutivas","instrutivo","instrutivos","insuperaveis",
        "insuperavel","inteligente","inteligentes","interessado","invenciveis",
        "invencivel","inventiva","inventivas","inventivo","inventivos","inventor",
        "inventora","inventoras","inventores","inspirada","inspirado","irado",
        "irrefutaveis","irrefutavel","irreprimiveis","irreprimivel","isenta","isentas",
        "isento","isentos","jeitosa","jeitosas","jeitoso","jeitosos","joia","joviais",
        "jovial","justa","justas","justo","justos","leais","leal","legitimo","linda",
        "lindamente","lindo","lisonjeador","lisonjeadora","lisonjeadoras","lisonjeadores",
        "lisonjeira","lisonjeiras","lisonjeiro","lisonjeiros","luxuosa","luxuosas",
        "luxuoso","luxuosos","magnanima","magnanimas","magnanimo","magnanimos",
        "magnifica","magnificas","magnificente","magnificentes","magnifico",
        "magnificos","mago","magos","majestatica","majestaticas","majestatico",
        "majestaticos","majestosa","majestosas","majestoso","majestosos","maneiro",
        "maneiros","maravilhado","maravilhosa","maravilhosas","maravilhoso",
        "maravilhosos","massa","meiga","meigas","meigo","meigos","melhor","melhora",
        "melhorado","melhorando","melhoramento","melhoria","melhorias","melodiosa",
        "melodiosas","melodioso","melodiosos","memoraveis","memoravel","memoriosa",
        "memoriosas","memorioso","memoriosos","merecedor","merecedora","merecedoras",
        "merecedores","meticulosa","meticulosas","meticuloso","meticulosos","milagrosa",
        "milagrosas","milagroso","milagrosos","mimosa","mimosas","mimoso","mimosos",
        "minuciosa","minuciosas","minucioso","minuciosos","modernas","moderno","modernos",
        "modesto","motivada","motivadas","motivado","motivador","motivadora","motivadoras",
        "motivadores","motivados","nobre","nobres","organizada","organizadas","organizado",
        "organizados","orgulhoso","orgulhosa","originais","original","otima","otimo",
        "otimista","participativo","participativa","participativamente","penetrante",
        "penetrantes","perfeita","perfeitamente","perfeitas","perfeito","perfeitos",
        "persuasiva","persuasivas","persuasivo","persuasivos","perspicaz","perspicazmente",
        "pertinente","pertinentes","piedosa","piedosas","piedoso","piedosos","ponderada",
        "ponderadas","ponderado","ponderados","ponderosa","ponderosas","ponderoso",
        "ponderosos","pontuais","pontual","popular","populares","positivo","positivamente",
        "precavida","precavidas","precavido","precavidos","preciosa","preciosas",
        "precioso","preciosos","predileta","prediletas","predileto","prediletos",
        "preferida","preferidas","preferido","preferidos","premiada","premiadas",
        "premiado","premiados","prendada","prendadas","prendado","prendados","preparada",
        "preparadas","preparado","preparados","prestativa","prestativas","prestativo",
        "prestativos","prestigiada","prestigiadas","prestigiado","prestigiados",
        "prestigiante","prestigiantes","prestigiosa","prestigiosas","prestigioso",
        "prestigiosos","prevenida","prevenidas","prevenido","prevenidos","previdente",
        "previdentes","proativo","proativa","proativamente","prodigiosa","prodigiosas",
        "prodigioso","prodigiosos","produtiva","produtivas","produtivo","produtivos",
        "proeminente","proeminentes","proficiente","proficientes","proficientemente",
        "proficua","proficuas","proficuo","proficuos","progresso","progrediu","promissor",
        "promissora","promissoras","promissores","promitente","promitentes","propicia",
        "propicias","propicio","propicios","proporcionais","proporcional","prospera",
        "prosperas","prospero","prosperos","proveitosa","proveitosas","proveitoso",
        "proveitosos","proveitosamente","providenciais","providencial","pujante",
        "pujantes","qualificada","qualificadas","qualificado","qualificados","querida",
        "queridas","querido","queridos","quista","quistas","quisto","quistos","racionais",
        "racional","radiante","radiantes","radiosa","radiosas","radioso","radiosos",
        "realista","realistas","realizada","realizadas","realizado","realizados",
        "receptiva","receptivas","receptivo","receptivos","recomendada","recomendadas",
        "recomendado","recomendados","recomendaveis","recomendavel","recompensado",
        "recompensador","recompensada","recompensadora","reforcada","reforcado",
        "relaxado","renovada","renovadas","renovado","renovados","rentavel","respeitada",
        "respeitadas","respeitado","respeitador","respeitadora","respeitadoras","respeitadores",
        "respeitados","respeitaveis","respeitavel","respeitosa","respeitosas","respeitoso",
        "respeitosos","responsaveis","responsavel","revigorada","revigoradas","revigorado",
        "revigorados","sabia","sabio","santificada","santificadas","santificado",
        "santificados","santissima","santissimas","santissimo","santissimos","santo",
        "santa","sarada","saradas","sarado","sarados","satisfeito","satisfeita",
        "satisfatoriamente","sedutor","sedutora","sedutoras","sedutores","segura",
        "seguras","seguro","seguros","seleta","seletas","seleto","seletos","sensuais",
        "sensual","serena","serenas","sereno","serenos","sexy","simpatica","simpaticas",
        "simpatico","simpaticos","soberba","soberbas","soberbo","soberbos","sofisticada",
        "sofisticadas","sofisticado","sofisticados","sorridente","sorridentes","sossegada",
        "sossegadas","sossegado","sossegados","suave","suaves","sublimada","sublimadas",
        "sublimado","sublimados","sublime","sublimes","sumptuosa","sumptuosas","sumptuoso",
        "sumptuosos","suntuosa","suntuosas","suntuoso","suntuosos","superconfiante",
        "superconfiantes","superdotada","superdotadas","superdotado","superdotados",
        "superelegante","superelegantes","superior","superiores","supimpa","supimpas",
        "suprema","supremas","supremo","supremos","surpreendente","surpreendentes",
        "surpreendido","talentosa","talentosas","talentoso","talentosos","tranquilizador",
        "tranquilizadora","tranquilizadoras","tranquilizadores","tranquilizante",
        "tranquilizantes","triunfador","triunfadora","triunfadoras","triunfadores",
        "triunfante","triunfantes","unificador","unificadora","unificadoras",
        "unificadores","uniformizador","uniformizadora","uniformizadoras",
        "uniformizadores","valente","valentes","valentona","valentonas","valiosa",
        "valiosas","valioso","valiosos","valorizada","valorizado","valorosa",
        "valorosas","valoroso","valorosos","vantajosa","vantajosas","vantajoso",
        "vantajosos","venerada","veneradas","venerado","venerados","veneranda",
        "venerandas","venerando","venerandos","veneraveis","veneravel","verdadeiro",
        "vigorosa","vigorosas","vigoroso","vigorosos","viril","viris","virtuosa",
        "virtuosas","virtuoso","virtuosos","visionaria","visionarias","visionario",
        "visionarios","vistosa","vistosas","vistoso","vistosos","vitalizador",
        "vitalizadora","vitalizadoras","vitalizadores","vitoriosa","vitoriosas",
        "vitorioso","vitoriosos","viva","zelosa","zelosas","zeloso","zelosos"]
            self.nwdictionary = ["abandalhada","abandalhadas","abandalhado","abandalhados","abandonada",
        "abandonadas","abandonado","abandonados","aberrante","aberrantes","aberrativa",
        "aberrativas","aberrativo","aberrativos","abestalhada","abestalhadas","abestalhado",
        "abestalhados","abilolada","abiloladas","abilolado","abilolados","abobada","abobadas",
        "abobado","abobados","abobalhada","abobalhadas","abobalhado","abobalhados","abominador","abominadora",
        "abominadoras","abominadores","abominanda","abominandas","abominando","abominandos","abomináveis",
        "abominável","aborrecida","aborrecidas","aborrecido","aborrecidos","abrutalhada","abrutalhadas",
        "abrutalhado","abrutalhados","absurda","absurdas","absurdo","absurdos","abusada","abusadas",
        "abusado","abusador","abusadora","abusadoras","abusadores","abusados","abusiva","abusivas","abusivo",
        "abusivos","acabada","acabadas","acabado","acabados","acabrunhada","acabrunhadas","acabrunhado",
        "acabrunhados","acanhada","acanhadas","acanhado","acanhado","acanhados","acefala","acefalas",
        "acefalo","acefalos","achacada","achacadas","achacado","achacados","adultera","adulterador",
        "adulteradora","adulteradoras","adulteradores","adulteras","adulterina","adulterinas",
        "adulterino","adulterinos","adultero","adulteros","adversa","adversas","adverso","adversos",
        "afetada","afetadas","afetado","afetados","aflita","aflitas","aflitiva","aflitivas",
        "aflitivo","aflitivos","aflito","aflitos","afobada","afobadas","afobado","afobados",
        "agoniada","agoniadas","agoniado","agoniados","agoniante","agoniantes","agonizante",
        "agonizantes","agressiva","agressivas","agressivo","agressivos","agressor","agressora",
        "agressoras","agressores","alarmante","alarmantes","alarmista","alarmistas","aliciada",
        "aliciadas","aliciado","aliciados","alienada","alienadas","alienado","alienados",
        "alienigena","alienigenas","aluada","aluadas","aluado","aluados","amaldicoada",
        "amaldicoadas","amaldicoado","amaldicoados","ameacador","ameacadora","ameacadoras",
        "ameacadores","ameacante","ameacantes","amedrontado","amorais","amoral","amoralista",
        "amoralistas","amorfa","amorfas","amorfo","amorfos","amuada","amuadas","amuado","amuados",
        "analfabeta","analfabetas","analfabeto","analfabetos","anarquica","anarquicas","anarquico",
        "anarquicos","anarquista","anarquistas","angustiada","angustiadas","angustiado","angustiados",
        "angustiante","angustiantes","aniquilada","aniquiladas","aniquilado","aniquilados","anoretica",
        "anoreticas","anoretico","anoreticos","anormais","anormal","antidesportista","antidesportistas",
        "antiliberais","antiliberal","antiliberalista","antiliberalistas","antinaturais","antinatural",
        "antipatica","antipaticas","antipatico","antipaticos","antipatriota","antipatriotas","antipolitica",
        "antipoliticas","antipolitico","antipoliticos","antiquada","antiquadas","antiquado","antiquados",
        "antisociais","antisocial","apagada","apagadas","apagado","apagados","apalermada","apalermadas",
        "apalermado","apalermados","apatica","apaticas","apatico","apaticos","arcaica","arcaicas","arcaico",
        "arcaicos","ardilosa","ardilosas","ardiloso","ardilosos","ardua","arduas","arduo","arduos","arida",
        "aridas","arido","aridos","arisca","ariscas","arisco","ariscos","arrebentada","arrebentadas",
        "arrebentado","arrebentados","arruinada","arruinadas","arruinado","arruinados","asfixiante",
        "asfixiantes","asna","asnas","asneirenta","asneirentas","asneirento","asneirentos","asno",
        "asnos","aspera","asperas","aspero","asperos","asquerosa","asquerosas","asqueroso","asquerosos",
        "assombrada","assombradas","assombrado","assombrados","assustada","assustadas","assustadica",
        "assustadicas","assustadico","assustadicos","assustado","assustado","assustador","assustadora",
        "assustadoras","assustadores","assustados","atabalhoada","atabalhoadas","atabalhoado","atabalhoados",
        "atarantada","atarantadas","atarantado","atarantados","aterrorizada","aterrorizadas","aterrorizado",
        "aterrorizador","aterrorizadora","aterrorizadoras","aterrorizadores","aterrorizados","atonito",
        "atrapalhada","atrapalhadas","atrapalhado","atrapalhados","atrasada","atrasada mental",
        "atrasadas","atrasadas mentais","atrasado","atrasado mental","atrasados","atrasados mentais",
        "atrofiada","atrofiadas","atrofiado","atrofiados","atrofiante","atrofiantes","atropelada",
        "atropeladas","atropelado","atropelados","atroz","atrozes","atulhada","atulhadas","atulhado",
        "atulhados","aturdida","aturdidas","aturdido","aturdidos","autodestrutiva","autodestrutivas",
        "autodestrutivo","autodestrutivos","autoritaria","autoritarias","autoritario","autoritarios",
        "avarenta","avarentas","avarento","avarentos","avariada","avariadas","avariado","avariados",
        "avaro","avaros","aversa","aversas","averso","aversos","avessa","avessas","avesso","avessos",
        "azarada","azaradas","azarado","azarados","azarenta","azarentas","azarento","azarentos","azeda",
        "azedas","azedo","azedos","babaca","babacas","babao","babaos","babona","babonas","babosa","babosas",
        "baboso","babosos","bagaceira","bagaceiras","bagaceiro","bagaceiros","bagunceira","bagunceiras",
        "bagunceiro","bagunceiros","bajulador","bajuladora","bajuladoras","bajuladores","bandida","bandidas",
        "bandido","bandidos","barraqueira","barraqueiras","barraqueiro","barraqueiros","bastarda","bastardas",
        "bastardo","bastardos","bizarra","bizarras","bizarro","bizarros","blasfema","blasfemador","blasfemadora",
        "blasfemadoras","blasfemadores","blasfemas","blasfemo","blasfemos","boba","bobas","bobo","boboca",
        "bobocas","bobos","bocais","bocal","bosta","brigador","brigadora","brigadoras","brigadores",
        "brigante","brigantes","brigao","brigona","brigonas","briguenta","briguentas","briguento",
        "briguentos","bronca","broncas","bronco","broncos","bruta","brutas","bruto","brutos",
        "bucha","buchas","bufa","bufas","burra","burras","burro","burros","cabeca dura",
        "cabecas duras","cabecuda","cabecudas","cabecudo","cabecudos","cabisbaixa","cabisbaixas",
        "cabisbaixo","cabisbaixo","cabisbaixos","cacete","caceteira","caceteiras","caceteiro",
        "caceteiros","cacetes","cachaceira","cachaceiras","cachaceiro","cachaceiros","cadaverica",
        "cadavericas","cadaverico","cadavericos","cadaverosa","cadaverosas","cadaveroso","cadaverosos",
        "cadente","cadentes","caduca","caducas","caduco","caducos","cafona","cafonas","caga","caga","cagado",
        "cagado","cagando","cagando","cagao","cagarola","cagarolas","cagativa","cagativas","cagativo",
        "cagativos","cagona","cagonas","cagou","cagou","caloteira","caloteiras","caloteiro","caloteiros",
        "caluniada","caluniadas","caluniado","caluniador","caluniadora","caluniadoras","caluniadores",
        "caluniados","canalha","canalhas","cancerosa","cancerosas","canceroso","cancerosos","canibais",
        "canibal","canina","caninas","canino","caninos","cansado","capenga","capengas","caquectica",
        "caquecticas","caquectico","caquecticos","caquetica","caqueticas","caquetico","caqueticos",
        "caralho","carniceira","carniceiras","carniceiro","carniceiros","carrancuda","carrancudas",
        "carrancudo","carrancudos","castigada","castigadas","castigado","castigador","castigadora",
        "castigadoras","castigadores","castigados","castrador","castradora","castradoras","castradores",
        "catastrofica","catastroficas","catastrofico","catastroficos","catinguenta","catinguentas",
        "catinguento","catinguentos","cauteloso","cavernosa","cavernosas","cavernoso","cavernosos",
        "chantagista","chantagistas","charlataes","charlatao","charlatao","charlatona","charlatonas",
        "chata","chatas","chateada","chateadas","chateado","chateados","chato","chatos","chauvinista",
        "chauvinistas","chifruda","chifrudas","chifrudo","chifrudos","chinfrineira","chinfrineiras",
        "chinfrineiro","chinfrineiros","chinfrins","chocas","chocha","chochas","chocho","chochos",
        "choco","chocos","choramingaes","choramingao","choramingas","choramingona","choramingonas",
        "chorao","choroes","chorona","choronas","chula","chulas","chulo","chulos","chunga","chungas",
        "chupa","chupa","cinica","cinicas","cinico","cinicos","ciosa","ciosas","cioso","ciosos","coco",
        "condenada","condenadas","condenado","condenados","condenaveis","condenavel","confusa","confusas",
        "confuso","confusos","consternada","consternadas","consternado","consternador","consternadora",
        "consternadoras","consternadores","consternados","constrangedor","constrangedora","constrangedoras",
        "constrangedores","constrangida","constrangidas","constrangido","constrangidos","consumida",
        "consumidas","consumido","consumidos","consumista","consumistas","controversa","controversas",
        "controverso","controversos","controvertida","controvertidas","controvertido","controvertidos",
        "cornuda","cornudas","cornudo","cornudos","cornuta","cornutas","cornuto","cornutos","corrupta",
        "corruptas","corruptiva","corruptivas","corruptiveis","corruptivel","corruptivo","corruptivos",
        "corrupto","corruptor","corruptora","corruptoras","corruptores","corruptos","covarde","covardes",
        "crapula","crapulas","crapulosa","crapulosas","crapuloso","crapulosos","crassa","crassas","crasso",
        "crassos","cretina","cretinas","cretino","cretinos","criminosa","criminosas","criminoso","criminosos",
        "culpado	","culpavel","danosa","danosas","danoso","danosos","debeis","debil","decadente","decadentes",
        "decadentista","decadentistas","decaida","decaidas","decaido","decaidos","decepcionada","decepcionadas",
        "decepcionado","decepcionados","decepcionante","decepcionantes","decrepita","decrepitas","decrepito",
        "decrepitos","defeituosa","defeituosas","defeituoso","defeituosos","deficiente","deficientes","definhada",
        "definhadas","definhado","definhados","deformada","deformadas","deformado","deformados","defunta",
        "defuntas","defunto","defuntos","degenerada","degeneradas","degenerado","degenerados","degradada",
        "degradadas","degradado","degradados","degradante","degradantes","deleteria","deleterias","deleterio",
        "deleterios","delinquente","delinquentes","delituosa","delituosas","delituoso","delituosos","demagoga",
        "demagogas","demagogica","demagogicas","demagogico","demagogicos","demagogo","demagogos","demente",
        "dementes","demerita","demeritas","demerito","demeritos","demode","demodes","demoniaca","demoniacas",
        "demoniaco","demoniacos","demorada","demoradas","demorado","demorados","denegrida","denegridas",
        "denegrido","denegridos","depauperada","depauperadas","depauperado","depauperados","depenada",
        "depenadas","depenado","depenados","deploraveis","deploravel","depravada","depravadas",
        "depravado","depravador","depravadora","depravadoras","depravadores","depravados",
        "depreciada","depreciadas","depreciado","depreciados","depreciativa",
        "depreciativas","depreciativo","depreciativos","depressiva","depressivas",
        "depressivo","depressivos","depressor","depressora","depressoras","depressores",
        "deprimente","deprimentes","deprimida","deprimidas","deprimido","deprimido","deprimidos",
        "derrotada","derrotadas","derrotado","derrotados","derrotista","derrotistas","desacreditada",
        "desacreditadas","desacreditado","desacreditados","desafeta","desafetas","desafeto","desafetos",
        "desaforada","desaforadas","desaforado","desaforados","desafortunada","desafortunadas","desafortunado",
        "desafortunados","desagradada","desagradadas","desagradado","desagradados","desagradaveis",
        "desagradavel","desagradecida","desagradecidas","desagradecido","desagradecidos","desajeitada",
        "desajeitadas","desajeitado","desajeitados","desajustada","desajustadas","desajustado","desajustados",
        "desalentada","desalentadas","desalentado","desalentados","desalinhada","desalinhadas","desalinhado",
        "desalinhados","desalmada","desalmadas","desalmado","desalmados","desanimada","desanimadas","desanimado",
        "desanimado","desanimado","desanimador","desanimadora","desanimadoras","desanimadores","desanimados",
        "desaparafusada","desaparafusadas","desaparafusado","desaparafusados","desapontada","desapontadas",
        "desapontado","desapontado","desapontador","desapontadora","desapontadoras","desapontadores","desapontados",
        "desapropriada","desapropriadas","desapropriado","desapropriados","desaprovador","desaprovadora",
        "desaprovadoras","desaprovadores","desarranjada","desarranjadas","desarranjado","desarranjados",
        "desarticulada","desarticuladas","desarticulado","desarticulados","desastrada","desastradas",
        "desastrado","desastrados","desastrosa","desastrosas","desastroso","desastrosos","desatinada",
        "desatinadas","desatinado","desatinados","desatualizada","desatualizadas","desatualizado",
        "desatualizados","desavergonhada","desavergonhadas","desavergonhado","desavergonhados",
        "desbaratada","desbaratadas","desbaratado","desbaratador","desbaratadora","desbaratadoras",
        "desbaratadores","desbaratados","desbocada","desbocadas","descabida","descabidas","descabido",
        "descabidos","descarada","descaradas","descarado","descarados","desclassificada","desclassificadas",
        "desclassificado","desclassificados","descomedida","descomedidas","descomedido","descomedidos",
        "desconexa","desconexas","desconexo","desconexos","desconfortaveis","desconfortavel","descontente",
        "descontentes","descontrolada","descontroladas","descontrolado","descontrolados","descoordenada",
        "descoordenadas","descoordenado","descoordenados","descuidada","descuidadas","descuidado","descuidados",
        "desdenhosa","desdenhosas","desdenhoso","desdenhosos","deselegante","deselegantes","desencontrada",
        "desencontradas","desencontrado","desencontrados","desengoncada","desengoncadas","desengoncado",
        "desengoncados","desengracada","desengracadas","desengracado","desengracados","desequilibrada",
        "desequilibradas","desequilibrado","desequilibrados","desgastada","desgastadas","desgastado",
        "desgastados","desgostosa","desgostosas","desgostoso","desgostosos","desgovernada","desgovernadas",
        "desgovernado","desgovernados","desgracada","desgracadas","desgracado","desgracados","desiludida",
        "desiludidas","desiludido","desiludidos","desinformada","desinformadas","desinformado","desinformados",
        "desinstruida","desinstruidas","desinstruido","desinstruidos","desinteressada","desinteressadas",
        "desinteressado","desinteressados","desinteressante","desinteressantes","deslambida","deslambidas",
        "deslambido","deslambidos","deslavada","deslavadas","deslavado","deslavados","desleais","desleal",
        "desleixada","desleixadas","desleixado","desleixados","desmantelada","desmanteladas","desmantelado",
        "desmantelados","desmazelada","desmazeladas","desmazelado","desmazelados","desmedida","desmedidas",
        "desmedido","desmedidos","desmemoriada","desmemoriadas","desmemoriado","desmemoriados","desmentida",
        "desmentidas","desmentido","desmentidos","desmesurada","desmesuradas","desmesurado","desmesurados",
        "desmiolada","desmioladas","desmiolado","desmiolados","desmoralizada","desmoralizadas","desmoralizado",
        "desmoralizador","desmoralizadora","desmoralizadoras","desmoralizadores","desmoralizados","desmotivada",
        "desmotivadas","desmotivado","desmotivador","desmotivadora","desmotivadoras","desmotivadores",
        "desmotivados","desnaturada","desnaturadas","desnaturado","desnaturados","desnorteada","desnorteadas",
        "desnorteado","desnorteados","desobediente","desobedientes","desocupada","desocupadas","desocupado",
        "desocupados","desonesta","desonestas","desonesto","desonestos","desonrada","desonradas","desonrado",
        "desonrados","desonrosa","desonrosas","desonroso","desonrosos","desordeira","desordeiras","desordeiro",
        "desordeiros","desordenada","desordenadas","desordenado","desordenados","desorganizada","desorganizadas",
        "desorganizado","desorganizados","desorientada","desorientadas","desorientado","desorientados","despeitada",
        "despeitadas","despeitado","despeitados","despeitorada","despeitoradas","despeitorado","despeitorados",
        "desperdicada","desperdicadas","desperdicado","desperdicador","desperdicadora","desperdicadoras",
        "desperdicadores","desperdicados","desprezado","desprezaveis","desprezavel","despreziveis","desprezivel",
        "desproporcionada","desproporcionadas","desproporcionado","desproporcionados","despropositada",
        "despropositadas","despropositado","despropositados","desqualificada","desqualificadas",
        "desqualificado","desqualificados","desregrada","desregradas","desregrado","desregrados",
        "desregulada","desreguladas","desregulado","desregulados","desrespeitada","desrespeitadas",
        "desrespeitado","desrespeitador","desrespeitadora","desrespeitadoras","desrespeitadores",
        "desrespeitados","desrespeitosa","desrespeitosas","desrespeitoso","desrespeitosos",
        "destemperada","destemperadas","destemperado","destemperados","destrambelhada","destrambelhadas",
        "destrambelhado","destrambelhados","destratada","destratadas","destratado","destratados",
        "destrutiva","destrutivas","destrutivo","destrutivos","destrutor","destrutora","destrutoras",
        "destrutores","desumana","desumanas","desumano","desumanos","desunida","desunidas","desunido",
        "desunidos","desvairada","desvairadas","desvairado","desvairados","desvalida","desvalidas",
        "desvalido","desvalidos","desvariada","desvariadas","desvariado","desvariados","desventurada",
        "desventuradas","desventurado","desventurados","desventurosa","desventurosas","desventuroso",
        "desventurosos","desvirtuada","desvirtuadas","desvirtuado","desvirtuados","deteriorada","deterioradas",
        "deteriorado","deteriorados","detestada","detestadas","detestado","detestados","detestaveis",
        "detestavel","deturpada","deturpadas","deturpado","deturpados","devaneador","devaneadora",
        "devaneadoras","devaneadores","devassa","devassada","devassadas","devassado","devassados",
        "devassas","devasso","devassos","devastada","devastadas","devastado","devastador",
        "devastadora","devastadoras","devastadores","devastados","diabolica","diabolicas",
        "diabolico","diabolicos","difamada","difamadas","difamado","difamador","difamadora",
        "difamadoras","difamadores","difamados","discriminadora","discriminadoras","discriminadores",
        "discriminados","dispensaveis","dispensavel","displicente","displicentes","dissidente",
        "dissidentes","dissimulada","dissimuladas","dissimulado","dissimulados","distorcida",
        "distorcidas","distorcido","distorcidos","divagante","divagantes","doentia","doentias",
        "doentio","doentios","dolosa","dolosas","doloso","dolosos","draconiana","draconianas",
        "draconiano","draconianos","drogada","drogadas","drogado","drogados","duvidosa","duvidosas",
        "duvidoso","duvidosos","egoista","egoistas","embacada","embacadas","embacado","embacados",
        "embaracosa","embaracosas","embaracoso","embaracosos","empapucada","empapucadas","empapucado",
        "empapucados","emporcalhada","emporcalhadas","emporcalhado","emporcalhados","encabulado","encanada",
        "encanadas","encanado","encanados","endemoniada","endemoniadas","endemoniado","endemoniados",
        "endiabrada","endiabradas","endiabrado","endiabrados","enervada","enervadas","enervado","enervados",
        "enervante","enervantes","enfadada","enfadadas","enfadado","enfadados","enfadonha","enfadonhas",
        "enfadonho","enfadonhos","enfastiada","enfastiadas","enfastiado","enfastiados","enfastiante",
        "enfastiantes","enfezada","enfezadas","enfezado","enfezados","enganacao","enganacao","enganacao",
        "enganacao","enganada","enganadas","enganado","enganador","enganadora","enganadoras",
        "enganadores","enganados","enganosa","enganosas","enganoso","enganosos","enjoada",
        "enjoadas","enjoado","enjoados","enlouquecida","enlouquecidas","enlouquecido",
        "enlouquecidos","enojada","enojadas","enojado","enojados","enraivecida","enraivecidas",
        "enraivecido","enraivecidos","enrolada","enroladas","enrolado","enrolados","entediada",
        "entediadas","entediado","entediados","entediante","entediante","entediante","entediantes",
        "entristecida","entristecidas","entristecido","entristecidos","entubada","entubadas",
        "entubado","entubados","entulhada","entulhadas","entulhado","entulhados","envaidecida",
        "envaidecidas","envaidecido","envaidecidos","envelhecida","envelhecidas","envelhecido",
        "envelhecidos","envenenador","envenenadora","envenenadoras","envenenadores","envergonhada",
        "envergonhadas","envergonhado","envergonhado","envergonhados","enviesada","enviesadas","enviesado",
        "enviesados","equivocada","equivocadas","equivocado","equivocados","errada","erradas","errado",
        "errado","errado","errados","erratica","erraticas","erratico","erraticos","erro","erro",
        "errou","escabrosa","escabrosas","escabroso","escabrosos","esclerosada","esclerosadas",
        "esclerosado","esclerosados","esdruxula","esdruxulas","esdruxulo","esdruxulos","esgotante",
        "esgotantes","espuria","espurias","espurio","espurios","estragada","estragadas","estragado",
        "estragado","estragado","estragados","estragou","estragou","estranha","estranhas","estranho",
        "estranhos","estropiada","estropiadas","estropiado","estropiados","estupida","estupidas","estupido",
        "estupidos","evasiva","evasivas","evasivo","evasivos","exagerada","exageradas","exagerado",
        "exagerados","excessiva","excessivas","excessivo","excessivos","falha","falhada","falhadas",
        "falhado","falhados","falhas","falho","falhos","falida","falidas","falido","falidos","falsa",
        "falsas","falseta","falsetas","falsissima","falsissimas","falsissimo","falsissimos","falso",
        "falso","falso","falsos","faltosa","faltosas","faltoso","faltosos","farsante","farsantes",
        "farsista","farsistas","farsola","farsolas","fascista","fascistas","fastidiosa","fastidiosas",
        "fastidioso","fastidiosos","fedorenta","fedorentas","fedorento","fedorentos","feia",
        "feias","feio","feio","feio","feios","filha da puta","filhasda puta","filho da puta",
        "filhos da puta","fingida","fingidas","fingido","foda","foda-se","fodeu","fodido",
        "forcada","forcadas","forcado","forcados","fudeu","fraca","fracalhota","fracalhotas",
        "fracalhote","fracalhotes","fracas","fracassada","fracassadas","fracassado","fracassados",
        "fraco","fraco","fraco","fracos","fracota","fracotas","fracote","fracotes","fraudulenta",
        "fraudulentas","fraudulento","fraudulentos","frivola","frivolas","frivolo","frivolos",
        "frouxa","frouxas","frouxo","frouxos","frustrada","frustradas","frustrado","frustrados",
        "fuck","fudido","fula","fulas","fulo","fulos","funesta","funestas","funesto",
        "funestos","furibunda","furibundas","furibundo","furibundos","furiosa","furiosas",
        "furioso","furioso","furiosos","futeis","futil","gasta","gastas","gasto","gastos",
        "gatuna","gatunas","gatuno","gatunos","grossa","grossas","grosseira","grosseirao",
        "grosseiras","grosseiro","grosseirona","grosseironas","grosseiros","grosso","grossos",
        "grotesca","grotescas","grotesco","grotescos","grudenta","grudentas","grudento",
        "grudentos","hedionda","hediondas","hediondo","hediondos","herege","hereges",
        "heretica","hereticas","heretico","hereticos","hipocrita","hipocritas",
        "histerica","histericas","histerico","histericos","horrenda","horrendas",
        "horrendo","horrendos","horripilante","horripilantes","horriveis","horrivel",
        "horrivel","horrorosa","horrorosas","horroroso","horrorosos","hostil","hostis",
        "humilhacao","humilhada","humilhadas","humilhado","humilhados","idiota",
        "idiotas","ilegais","ilegal","ilegitima","ilegitimas","ilegitimo","ilegitimos",
        "ilegiveis","ilegivel","ilicita","ilicitas","ilicito","ilicitos","iliterata",
        "iliteratas","iliterato","iliteratos","ilogica","ilogicas","ilogico","ilogicos",
        "iludida","iludidas","iludido","iludidos","ilusoria","ilusorias","ilusorio",
        "ilusorios","imatura","imaturas","imaturo","imaturos","imbecil","imbecis",
        "imitador","imitadora","imitadoras","imitadores","imorais","imoral","impaciente",
        "impaciente","impacientes","impenetraveis","impenetravel","imperdoaveis",
        "imperdoavel","imperfeita","imperfeitas","imperfeito","imperfeito","imperfeito",
        "imperfeitos","impessoais","impessoal","impopular","impopulares","importuna",
        "importunada","importunadas","importunado","importunados","importunas",
        "importuno","importunos","imposta","impostas","imposto","impostor","impostora",
        "impostoras","impostores","impotente","impotentes","imprecisa","imprecisas",
        "impreciso","imprecisos","imprestaveis","imprestavel","imprevidente","imprevidentes",
        "improcedente","improcedentes","improdutiva","improdutivas","improdutivo","improdutivos",
        "imprudente","imprudentes","impudente","impudentes","impugnada","impugnadas",
        "impugnado","impugnados","impulsiva","impulsivas","impulsivo","impulsivos","impura",
        "impuras","impuro","impuros","imunda","imundas","imundo","imundos","inabeis",
        "inabil","inaceitaveis","inaceitavel","inacessiveis","inacessivel","inapresentaveis",
        "inapresentavel","inapta","inaptas","inapto","inaptos","inativa","inativa",
        "inativas","inativas","inativo","inativo","inativos","inativos","incapaz",
        "incapazes","incerta","incertas","incerto","incertos","incomodado",
        "incompetente","incompetentes","incompleta","incompletas","incompleto",
        "incompletos","incompreensiveis","incompreensivel","inconcebiveis",
        "inconcebivel","inconciliaveis","inconciliavel","inconclusa","inconclusas",
        "inconcluso","inconclusos","incongruente","incongruentes","inconsciente",
        "inconscientes","inconsequente","inconsequentes","inconsistente","inconsistentes",
        "inconsolada","inconsoladas","inconsolado","inconsolados","inconsolaveis","inconsolavel",
        "inconstante","inconstantes","incontrariaveis","incontrariavel","incontrolada","incontroladas",
        "incontrolado","incontrolados","inconveniente","inconvenientes","inconversaveis","inconversavel",
        "incorrecta","incorrectas","incorrecto","incorrectos","incorreta","incorretas","incorreto",
        "incorretos","incorrigiveis","incorrigivel","inculta","incultas","inculto","incultos",
        "incuraveis","incuravel","indecente","indecentes","indecifraveis","indecifravel",
        "indecisa","indecisas","indeciso","indecisos","indecorosa","indecorosas",
        "indecoroso","indecorosos","indelicada","indelicadas","indelicado","indelicados",
        "indesejada","indesejadas","indesejado","indesejados","indesejaveis",
        "indesejavel","indigesta","indigestas","indigesto","indigestos","indigna",
        "indignada","indignadas","indignado","indignados","indignas","indigno","indignos",
        "indisciplinada","indisciplinadas","indisciplinado","indisciplinados","indiscreta",
        "indiscretas","indiscreto","indiscretos","individualista","individualistas","indolente",
        "indolentes","inefaveis","inefavel","ineficaz","ineficazes","ineficiente",
        "ineficientes","inelegiveis","inelegivel","inenarraveis","inenarravel","inepta",
        "ineptas","inepto","ineptos","inerte","inexata","inexatas","inexato",
        "inexatos","inexoraveis","inexoravel","inexperiente","inexperientes",
        "inexperta","inexpertas","inexperto","inexpertos","inexplicaveis",
        "inexplicavel","inexpressiva","inexpressivas","inexpressivo","inexpressivos",
        "inexprimiveis","inexprimivel","infamada","infamadas","infamado","infamados",
        "infamante","infamantes","infame","infamerrima","infamerrimas","infamerrimo",
        "infamerrimos","infames","infamissima","infamissimas","infamissimo","infamissimos",
        "infecunda","infecundas","infecundo","infecundos","infeliz","infelizes","infernais",
        "infernal","inferteis","infertil","infieis","infiel","inflexiveis","inflexivel",
        "influenciaveis","influenciavel","infortunada","infortunadas","infortunado",
        "infortunados","infrutifera","infrutiferas","infrutifero","infrutiferos",
        "infundada","infundadas","infundado","infundados","ingenua","ingenuas",
        "ingenuo","ingenuos","ingrata","ingratas","ingrato","ingratos","ininteligiveis",
        "ininteligivel","iniqua","iniquas","iniquo","iniquos","injuriada",
        "injuriadas","injuriado","injuriados","injuriante","injuriantes",
        "injuriosa","injuriosas","injurioso","injuriosos","injusta","injustas",
        "injusto","injustos","inoportuna","inoportunas","inoportuno","inoportunos",
        "inospita","inospitas","inospito","inospitos","insana","insanas","insano",
        "insanos","insatisfatoria","insatisfatorias","insatisfatorio","insatisfatorios",
        "insatisfeita","insatisfeitas","insatisfeito","insatisfeito","insatisfeitos",
        "insegura","inseguras","inseguro","inseguros","insensata","insensatas",
        "insensato","insensatos","insensiveis","insensivel","insipida","insipidas",
        "insipido","insipidos","insipiente","insipientes","insolente","insolentes",
        "insolita","insolitas","insolito","insolitos","insonsa","insonsas","insonso",
        "insonsos","insossa","insossas","insosso","insossos","instaveis","instavel",
        "insubordinada","insubordinadas","insubordinado","insubordinados","insuficiente",
        "insuficientes","intempestiva","intempestivas","intempestivo","intempestivos","intolerante",
        "intolerantes","intoleraveis","intoleravel","intragaveis","intragavel","intrataveis",
        "intratavel","intrusa","intrusas","intruso","intrusos","inuteis","inutil","invalida","invalidas",
        "invalido","invalidos","invasiva","invasivas","invasivo","invasivos","invasor","invasora",
        "invasoras","invasores","inviaveis","inviavel","inviesada","inviesadas","inviesado","inviesados",
        "irracionais","irracional","irrealista","irrealistas","irregular","irregulares","irrelevante",
        "irrelevantes","irritada","irritadas","irritadica","irritadicas","irritadico","irritadicos","irritado",
        "irritado","irritados","irritante","irritantes","irritativa","irritativas","irritativo","irritativos",
        "irritaveis","irritavel","ja era","jegue","jumento","laconia","laconias","laconica","laconicas",
        "laconico","laconicos","laconio","laconios","lamentaveis","lamentavel","lamentavel","lamento",
        "lamentosa","lamentosas","lamentoso","lamentosos","lastimaveis","lastimavel","lastimosa","lastimosas",
        "lastimoso","lastimosos","lazarenta","lazarentas","lazarento","lazarentos","lenta","lentas",
        "lento","lento","lentos","leprosa","leprosas","leproso","leprosos","lerda","lerdas","lerdo",
        "lerdos","lesa","lesada","lesadas","lesado","lesados","lesas","letargica","letargicas",
        "letargico","letargicos","leviana","levianas","leviano","levianos","libertina","libertinas",
        "libertino","libertinos","libidinosa","libidinosas","libidinoso","libidinosos","lunatica",
        "lunaticas","lunatico","lunaticos","macabra","macabras","macabro","macabros","machista","machistas",
        "magoado","mal-afamada","mal-afamadas","mal-afamado","mal-afamados","mal-afeicoada","mal-afeiçoadas",
        "mal-afeicoado","mal-afeicoados","mal-afortunada","mal-afortunadas","mal-afortunado","mal-afortunados",
        "mal-agradecida","mal-agradecidas","mal-agradecido","mal-agradecidos","mal-amada","mal-amadas",
        "mal-amado","mal-amados","malandra","malandras","malandreca","malandrecas","malandreco","malandrecos",
        "malandro","malandros","malcheirosa","mal-cheirosa","malcheirosas","mal-cheirosas","malcheiroso",
        "mal-cheiroso","malcheirosos","mal-cheirosos","mal-comportada","mal-comportadas","mal-comportado",
        "mal-comportados","malcriada","malcriadas","malcriado","malcriados","maldisposta","maldispostas",
        "maldisposto","maldispostos","maldita","malditas","maldito","malditos","maldizente","maldizentes",
        "maldosa","maldosas","maldoso","maldosos","maledicente","maledicentes","maleducada","mal-educada",
        "maleducadas","mal-educadas","maleducado","mal-educado","maleducados","mal-educados","malefica",
        "maleficas","malefico","maleficos","malencarada","mal-encarada","malencaradas","mal-encaradas",
        "malencarado","mal-encarado","malencarados","mal-encarados","malevola","malevolas","malevolente",
        "malevolentes","malevolo","malevolos","malfadada","malfadadas","malfadado","malfadados",
        "malfazeja","malfazejas","malfazejo","malfazejos","malfeita","mal-feita","malfeitas",
        "mal-feitas","malfeito","mal-feito","malfeitor","malfeitora","malfeitoras",
        "malfeitores","malfeitos","mal-feitos","malformada","malformadas","malformado",
        "malformados","mal-humorada","mal-humoradas","mal-humorado","mal-humorados",
        "maligna","malignas","maligno","malignos","mal-intencionada","mal-intencionadas",
        "mal-intencionado","mal-intencionados","malograda","malogradas","malogrado",
        "malogrados","mal-paga","mal-pagas","mal-pago","mal-pagos","malquista",
        "malquistas","malquisto","malquistos","malsucedida","malsucedidas","malsucedido",
        "malsucedidos","mal-vestida","mal-vestidas","mal-vestido","mal-vestidos",
        "maniaca","maniacas","maniaco","maniaco-depressiva","maniaco-depressivas",
        "maniaco-depressivo","maniaco-depressivos","maniacos","manipulador","manipuladora",
        "manipuladoras","manipuladores","manipulados","manipulaveis","manipulavel","maquiavelica",
        "maquiavelicas","maquiavelico","maquiavelicos","maquiavelista","maquiavelistas",
        "maquinada","maquinadas","maquinado","maquinados","marginais","marginal",
        "marginalizada","marginalizadas","marginalizado","marginalizados","massante",
        "massante","massificante","massificante","mediocre","mediocres","meditabunda","meditabundas",
        "meditabundo","meditabundos","medonha","medonhas","medonho","medonhos","melancolica","melancolicas",
        "melancolico","melancolicos","melodramatica","melodramaticas","melodramatico","melodramaticos",
        "menosprezante","menosprezantes","menosprezaveis","menosprezavel","mentira","mentirosa","mercenaria",
        "mercenarias","mercenario","mercenarios","merda","mesquinha","mesquinhas","mesquinho","mesquinhos",
        "monotona","monotonas","monotono","monotonos","monstruosa","monstruosas","monstruoso","monstruosos",
        "morbida","morbidas","morbido","morbidos","moribunda","moribundas","moribundo","moribundos",
        "morna","mornas","morno","mornos","morosa","morosas","moroso","morosos","morta","mortas",
        "mortica","morticas","mortico","morticos","morto","mortos","mula","mula","mula","mulas",
        "mundana","mundanas","mundano","mundanos","murcha","murchas","murcho","murchos","mutilada",
        "mutiladas","mutilado","mutilados","naba","nabas","nabo","nabos","nao aguento","nao suporto",
        "nao gosto","nao quero","nauseada","nauseadas","nauseado","nauseados","nauseante",
        "nauseantes","nazi","nazis","nazista","nazistas","nebulosa","nebulosas","nebuloso",
        "nebulosos","nefasta","nefastas","nefasto","nefastos","negativa","negativas","negativo",
        "negativos","negligente","negligentes","nervoso	","neurotica","neuroticas","neurotico",
        "neuroticos","nociva","nocivas","nocivo","nocivos","nojenta","nojentas","nojento","nojentos",
        "nula","nulas","nulo","nulos","obscena","obscenas","obsceno","obscenos","obscura","obscuras",
        "obscurecida","obscurecidas","obscurecido","obscurecidos","obscuro","obscuros","obsessiva",
        "obsessivas","obsessivo","obsessivos","obsoleta","obsoletas","obsoleto","obsoletos","obtusa",
        "obtusas","obtuso","obtusos","oca","ocas","oco","ocos","odeio","odeio","odiada","odiadas",
        "odiado","odiados","odiando","odiando","odiáveis","odiável","odienta","odientas","odiento",
        "odientos","odio","odio","odio","odio","odiosa","odiosas","odioso","odiosos","ofendida",
        "ofendidas","ofendido","ofendidos","ofensiva","ofensivas","ofensivo","ofensivos","ofuscada",
        "ofuscadas","ofuscado","ofuscados","omissa","omissas","omisso","omissos","omitida",
        "omitidas","omitido","omitidos","oportunista","oportunistas","opressiva","opressivas",
        "opressivo","opressivos","opressor","opressora","opressoras","opressores",
        "opressos","oprimente","oprimentes","oprimida","oprimidas","oprimido","oprimidos",
        "ostensiva","ostensivas","ostensivo","ostensivos","ostentativa","ostentativas",
        "ostentativo","ostentativos","ostentosa","ostentosas","ostentoso","ostentosos","palerma",
        "palermas","palhaça","palhaças","palhaco","palhacos","pau no cu","paranoica","paranoicas",
        "paranoico","paranoicos","pariu","pariu","paspalha","paspalhao","paspalhas","paspalho",
        "paspalhoes","paspalhona","paspalhonas","paspalhos","pastelaes","pastelao","pastelona",
        "pastelonas","pateta","patetas","patetica","pateticas","patetico","pateticos","patife"
        ,"patifes","pavorosa","pavorosas","pavoroso","pavorosos","peca","pecador","pecadora"
        ,"pecadoras","pecadores","pecas","peco","pecos","pedante","pedantes","pegajosa",
        "pegajosas","pegajoso","pegajosos","perdularia","perdularias","perdulario","perdularios",
        "permissiva","permissivas","permissivo","permissivos","perniciosa","perniciosas","pernicioso",
        "perniciosos","perturbada","perturbadas","perturbado","perturbador","perturbadora",
        "perturbadoras","perturbadores","perturbados","perturbante","perturbantes","perversa",
        "perversas","perverso","perversos","pervertedor","pervertedora","pervertedoras",
        "pervertedores","pervertida","pervertidas","pervertido","pervertidos","pessima",
        "pessimas","pessimista","pessimistas","pessimo","pessimos","petulante","petulantes",
        "piegas","pifia","pifias","pifio","pifios","pior","piores","podre","podres","politiqueira",
        "politiqueiras","politiqueiro","politiqueiros","porca","porcalhaes","porcalhao",
        "porcalhona","porcalhonas","porcas","porcina","porcinas","porcino","porcinos","porco","porcos",
        "pornografica","pornograficas","pornografico","pornograficos","porra","possessa",
        "possessas","possessiva","possessivas","possessivo","possessivos","possesso","possessos",
        "preconceituosa","preconceituosas","preconceituoso","preconceituosos","preguicosa","preguicosas",
        "preguicoso","preguicosos","prejudicada","prejudicadas","prejudicado","prejudicados","prejudiciais",
        "prejudicial","preocupado","prepotente","prepotentes","presuncosa","presuncosas","presuncoso",
        "presuncosos","pretensa","pretensas","pretensiosa","pretensiosas","pretensioso","pretensiosos",
        "pretenso","pretensos","primitiva","primitivas","primitivo","primitivos","problematica","problematicas",
        "problematico","problematicos","profana","profanador","profanadora","profanadoras","profanadores",
        "profanas","profano","profanos","proibitiva","proibitivas","proibitivo","proibitivos","promiscua",
        "promiscuas","promiscuo","promiscuos","prostituida","prostituidas","prostituido","prostituidos",
        "prostituta","prostitutas","prostituto","prostitutos","prostrada","prostradas","prostrado",
        "prostrados","psicopata","psicopatas","psicotica","psicoticas","psicotico","psicoticos","puta",
        "puta que pariu","putaria","putas","puto","puto","puto","putos","putrefata","putrefatas",
        "putrefato","putrefatos","putrida","putridas","putrido","putridos","quadrupede","quadrupedes",
        "questionaveis","questionavel","que e bom nada","rabugenta","rabugentas","rabugento","rabugentos",
        "racista","racistas","raivosa","raivosas","raivoso","raivosos","rancorosa","rancorosas","rancoroso",
        "rancorosos","rançosa","rançosas","rançoso","rançosos","ranheta","ranhetas","ranhosa","ranhosas",
        "ranhoso","ranhosos","ranzinza","ranzinzas","rebaixada","rebaixadas","rebaixado","rebaixados","relapsa",
        "relapsas","relapso","relapsos","relaxada","relaxadas","relaxado","relaxados","renegada","renegadas",
        "renegado","renegados","repetitiva","repetitivas","repetitivo","repetitivos","repressiva","repressivas",
        "repressivo","repressivos","repressor","repressora","repressoras","repressores","reprovada","reprovadas",
        "reprovado","reprovador","reprovadora","reprovadoras","reprovadores","reprovados","reprovaveis",
        "reprovavel","repugnancia","repugnante","repugnantes","repulsa","repulsas","repulsiva","repulsivas",
        "repulsivo","repulsivos","repulso","repulsos","revoltada","revoltadas","revoltado","revoltados",
        "revoltante","revoltantes","revoltosa","revoltosas","revoltoso","revoltosos","ridicula",
        "ridicularizador","ridicularizadora","ridicularizadoras","ridicularizadores","ridicularizante",
        "ridicularizantes","ridiculas","ridiculo","ridiculos","rispida","rispidas","rispido",
        "rispidos","rude","rudes","rudimentar","rudimentares","ruim","ruinosa","ruinosas","ruinoso",
        "ruinosos","ruins","safada","safadas","safado","safados","sem graca","sem-caracter","sem-carater",
        "sem-sabor","sem-sal","sinistra","sinistras","sinistro","sinistros","sofrega","sofregas","sofrego",
        "sofregos","sofrida","sofridas","sofrido","sofridos","solitario","sombria","sombrias","sombrio",
        "sombrios","songamonga","songa-monga","songamongas","songa-mongas","sonolento","sonsa","sonsas",
        "sonso","sonsos","sozinho","subversiva","subversivas","subversivo","subversivos","subversor",
        "subversora","subversoras","subversores","sufocada","sufocadas","sufocado","sufocador","sufocadora",
        "sufocadoras","sufocadores","sufocados","sufocante","sufocantes","suja","sujas","sujo","sujos",
        "superficiais","superficial","superflua","superfluas","superfluo","superfluos","supersticiosa",
        "supersticiosas","supersticioso","supersticiosos","tedio","tedio","tedio","tediosa","tediosas",
        "tedioso","tediosos","temeraria","temerarias","temerario","temerarios","temerosa","temerosas",
        "temeroso","temerosos","temida","temidas","temido","temidos","temiveis","temivel","temorosa",
        "temorosas","temoroso","temorosos","tendenciosa","tendenciosas","tendencioso","tendenciosos",
        "tenebrosa","tenebrosas","tenebroso","tenebrosos","terriveis","terrivel","timido","tinhosa",
        "tinhosas","tinhoso","tinhosos","tirana","tiranas","tiranica","tiranicas","tiranico","tiranicos",
        "tirano","tiranos","tolo","tolos","toma no cu","tonta","tontas","tontinha","tontinhas","tontinho",
        "tontinhos","tonto","tontos","toxica","toxicas","toxico","toxicos","traicoeira","traicoeiras",
        "traicoeiro","traicoeiros","traida","traidas","traido","traidor","traidora","traidoras","traidores",
        "traidos","transviada","transviadas","transviado","transviados","trapaca","trapaceira","trapaceiras",
        "trapaceiro","trapaceiros","trapacenta","trapacentas","trapacento","trapacentos","tremulo","triste",
        "tristes","turraes","turrao","turrona","turronas","ultrajada","ultrajadas","ultrajado","ultrajados",
        "ultrajante","ultrajantes","ultrapassada","ultrapassadas","ultrapassado","ultrapassados","umilhacao",
        "usurpador","usurpadora","usurpadoras","usurpadores","utopica","utopicas","utopico","utopicos","vadia",
        "vadias","vadio","vadios","vaga","vagaba","vagabunda","vagabundas","vagabundo","vagabundos","vaiada",
        "vaiadas","vaiado","vaiados","vazia","vazias","vazio","vazios","vergonhosa","vergonhosas","vergonhoso",
        "vergonhosos","violenta","violentada","violentadas","violentado","violentados","violentas","violento",
        "violentos","virulenta","virulentas","virulento","virulentos","vis","vomitada","vomitadas","vomitado",
        "vomitados","vulgar","vulgares","vulgarizada","vulgarizadas","vulgarizado","vulgarizador","vulgarizadora",
        "vulgarizadoras","vulgarizadores","vulgarizados","vulneraveis","vulneravel","zoado","zuado"]
            self.neutralwdictionary = ["acreditando","acredite","acreditei","aleatoria","algum dia","alteracao","alteracoes",
        "ambigua","ambiguidade","ambiguidades","anomalamente","anomalia","anomalias","anomalo","antecipa",
        "antecipacao","antecipacoes","antecipado","antecipar","aparece","apareceu","aparente","aparentemente",
        "aproxima","aprocao","aproximacoes","aproximada","aproximadamente","aproximado","aproximando",
        "arbitraria","arbitrariamente","arbitrariedade","arriscada","arriscado","arriscando","arriscaram",
        "as vezes","assume","assume","assumido","assumindo","atipicamente","caprichos","cautelosamente",
        "cautelosos","claro","concebivel","concebivelmente","condicional","condicionalmente","confunde",
        "confusao","confuso","considera","contingencia","contingencias","contingente","contingentemente",
        "contingentes","de repente","de vez","dependencia","dependencia","dependencias","dependendo",
        "dependentes","depender","dependia","desconcertante","desconhecido","desconhecido","desconhecimento",
        "desestabilizadora","desviando","desviar","desviaram","desvio","desvios","difere","diferencas",
        "diferentes","diferiu","diverge","dobradicas","duvida","duvidas","duvidosa","duvidou","em algum lugar",
        "encruzilhada","esclarecimento","esclarecimentos","especula","especula","especulacao","especulacoes",
        "especulando","especular","especulativamente","especulativo","esporadicamente","esporadico",
        "exposicao","exposicoes","flutua","flutuante","flutuar","flutuou","imaterial","imprecisao",
        "impreciso","imprecisoes","imprevisibilidade","imprevisivel","imprevisivelmente","imprevistas",
        "imprevistas","improbabilidade","improvavel","incerta","incerteza","incertezas","incerto","incluir",
        "incognitas","incompletude","indeciso","indeciso","indefinido","indefinicao","indefinidamente",
        "indefinir","indetectavel","indeterminado","indeterminado","indeterminavel","indeterminavel",
        "indocumentados","inespecifica","inesperadamente","inesperado","inexacta","inexatidao","inoportuno",
        "inquantavel","instabilidade","instabilidades","intangiveis","maio","mais arriscados","mais vaga",
        "nao acessivel","nao coberta","nao comprovadas","nao escrito","nao garantido","nao identificado",
        "nao observaveis","nao planejada","nao quantificada","nao testado","normalmente","novo calculo","obrigado",
        "obrigada", "oscilacao","parece","pendencias","pendente","pode","pode ser","poderia","possibilidade","possibilidades",
        "possevel","possivelmente","precaucao","precaucao","precaucoes","predizer","preliminar",
        "preliminarmente","pressupostos","presume","presumido","presumindo","presumir","presumivelmente",
        "presuncao","presuncoes","preve","prevendo","prever","previsao","previsibilidade","previsoes",
        "prevista","probabilidade","probabilidades","probabilistico","provavel","provavelmente","prudencia"
        ,"quase","quase","randomico","randomizacao","randomizado","randomizar","raramente","reavalia",
        "reavaliacao","reavaliacoes","reavaliados","reavaliando","reavaliar","recalcula","recalculado",
        "recalculando","recalcular","recalculo","reconsidera","reconsiderado","reconsiderando",
        "reconsiderar","reexame","reexaminando","reexaminar","reinterpreta","reinterpretacao",
        "reinterpretacoes","reinterpretado","reinterpretando","reinterpretar","revisao","revista",
        "risco","riscos","rumores","subita","sugere","sugerindo","sugerir","sugestao","susceptibilidade",
        "talvez","tendem","timidamente","turbulencia","vaga","vagamente","vagueza","varia","variabilidade",
        "variacao","variacoes","variancias","variar","variaveis","variavel","variavelmente","volatil",
        "volatilidade","volatilidades"]
            self.nedictionary = ["D=","D-=",")*","):","D:","¬¬","¬¬'","¬.¬","¬_¬","¬__¬","\=","=\\",
        ":(",":((",":(((","):",")):","))):",":'(",":´(",")':",")´:",":'-(",")-':",
        ":-(",")-:",":(","):",":'(",":´(",")':",":'-(",")-':",":-.",".-:",":/",
        "\:",":-/","\-:",":@","@:",":[","]:",":-[","]-:","\:",":{","}:",":-|",
        "|-:",":|","|:",":-||","||-:",":<",">:",":-<",">-:","ç-ç:",":c",":-c",
        ":o","o:",":O","O:",":-O","O-:",":s","s:",":S","S:",";(",");",";@","@;",
        ";s","S;","s;","<.<","=(",")=","=/","\=","=@","@=",">.<",">..<",">_<",
        ">__<",">.>","<.<",">..>","<..<",">__>","<__<","°o°","°O°","8-0","0-8",
        "D-':","D:","D;","D=","D8","DX","o.O","O.o","O.O","o.o","0.o","O.O",
        "o_0","o_O","o__O","o__0","0_0","0_o","0__0","o_O","u.u","u_u","U.U",
        "v.v","=|"]#,"=\",':\']
            self.pedictionary = ['=3','=-3','=D','=-D','=p','p=','P=','*)','(*','*-)','(-*','*-*',
        '*--*','*_*','*__*','*.*',':)','(:',':-)','(-:',':-))','((-:',':]','[:',
        ':^)','(^:',':}','{:',':>','<:',':3',':b',':B','=B','=B',':-b',':c)',':D',
        ':d',':-D',':o)',':P',':p',':-P',':-p',':U',':-U',';)','(;',';-)','(-;',
        ';]','[;',';-]','[-;',';^)','(^;',';D',';d','^^','^.^','^..^','^_^','^__^',
        '^-^','^--^','(=','=]','[=','8-)','(-8','8)','(8','8D','8-D','xD','x-D',
        'xp','XP','X-P','x-p','o/','\o/']
    
    @staticmethod
    def _count_char(text, regex = None):        
        if regex is None:
            return len(text)
        else:
            t = 0
            for c in text:
                if re.match(regex, c):
                    t = t + 1
            return t

    '''
    -----------------------------------------------------------------------------------------------------------------------
    DEFINICAO DOS META-ATRIBUTOS
    -----------------------------------------------------------------------------------------------------------------------
    '''
    
    '''
    -----------------------------------------------------------------------------------------------------------------------
    META-ATRIBUTOS BASEADOS EM ANALISE DE CARACTERES (C) - 16 meta-atributos 
    -----------------------------------------------------------------------------------------------------------------------
    '''

    @property
    def C1(self):
        return self.C 
#       C1: Quantidade total de caracteres (C)         
    @property
    def C2(self):
        return self.LOWER / float(self.C)
#       C2: Razão entre o número total de letras minúsculas (a-z) e o total de caracteres (C)
    @property
    def C3(self):
        return self.UPPER / float(self.C)
#       C3: Razão entre o número total de caracteres maiúsculos (A-Z) e o total de caracteres (C)
    @property
    def C4(self):
        return self.NUMBERS / float(self.C)
#       C4: Razão entre a quantidade de números (dígitos) e o total de caracteres (C)
    @property
    def C5(self):
        return self.WHITE / float(self.C)
#       C5: Razão entre o número de espaços em branco (white spaces) e o total de caracteres (C)
    @property
    def C6(self):
        return self.TAB / float(self.C)
#       C6: Razão entre o número de tabulações (tab spaces) e o total de caracteres (C)
    @property
    def C7(self):
        return MetaAttributes._count_char(self.raw, r'\'') / float(self.C)
#       C7: Razão entre o número de aspas (“) e o total de caracteres (C)
    @property
    def C8(self):
        return MetaAttributes._count_char(self.raw, r'\,') / float(self.C)
#       C8: Razão entre o número de vírgulas (,) e o total de caracteres (C)
    @property
    def C9(self):
        return MetaAttributes._count_char(self.raw, r'\:') / float(self.C)
#       C9: Razão entre o número de dois-pontos (:) e o total de caracteres (C)
    @property
    def C10(self):
        return MetaAttributes._count_char(self.raw, r'\;') / float(self.C)
#       C10: Razão entre o número de ponto-e-vírgulas (;) e o total de caracteres (C)
    @property
    def C11(self):
        return MetaAttributes._count_char(self.raw, r'\?') / float(self.C)
#       C11: Razão entre o número de pontos de interrogação simples (?) e o total de caracteres (C)
    @property
    def C12(self):
        return MetaAttributes._count_char(self.raw, r'\?\?+') / float(self.C)
#       C12: Razão entre o número de múltiplos pontos de interrogação (???) e o total de caracteres (C)
    @property
    def C13(self):
        return MetaAttributes._count_char(self.raw, r'\!') / float(self.C)
#       C13: Razão entre o número de pontos de exclamação simples (!) e o total de caracteres (C)
    @property
    def C14(self):
        return MetaAttributes._count_char(self.raw, r'\!\!+') / float(self.C)
#       C14: Razão entre o número de múltiplos pontos de exclamação (!!!) e o total de caracteres (C)
    @property
    def C15(self):
        return MetaAttributes._count_char(self.raw, r'\.') / float(self.C)
#       C15: Razão entre o número de pontos finais simples (.) e o total de caracteres (C)
    @property
    def C16(self):
        return MetaAttributes._count_char(self.raw, r'\.\.+') / float(self.C)     
#       C16: Razão entre o número de reticências (...) e o total de caracteres (C)     
    
    '''
    -----------------------------------------------------------------------------------------------------------------------
    META ATRIBUTOS BASEADOS EM ANÁLISE DE PALAVRAS (W) - 28 meta-atributos (12 + W13_N)
    -----------------------------------------------------------------------------------------------------------------------
    '''

    @property
    def W1(self):  
        return self.N
#       W1: Quantidade total de palavras (P)
    @property
    def W2(self):     
        n = []
        for w in self.WORDS:
            n.append(len(w))
        return float(numpy.mean(n))
#       W2: Média da quantidade de caracteres por palavra (P)
    @property
    def W3(self):
        return self.VRICH / float (self.N)
#       W3: Razão entre o número de palavras diferentes e o total de palavras (número total de palavras diferentes/P)
    @property
    def W4(self):    
        t = 0
        for s in self.SIZES:
            if s > 6:
                t = t + 1
        return t / float(self.N)
#       W4: Razão entre o número de palavras com mais de 6 caracteres e o total de palavras (P)
    @property
    def W5(self):
        t = 0
        for s in self.SIZES:
            if s <= 3:
                t = t + 1
        return t / float(self.N)
#       W5: Razão entre o número de palavras com 1 a 3 caracteres (palavras curtas) e o total de palavras (P)
    @property
    def W6(self):
        return len(self.HXLEGO) / float(self.N)
#       W6: Razão entre hapax legomena (palavra que ocorre uma única vez em todo um texto) e o número total de palavras (P)
    @property
    def W7(self):
        return len(self.V) / float(self.N)
#       W7: Razão entre hapax dislegomena (palavra que ocorre apenas duas vezes em todo um texto) e o número total de palavras (P)
    @property
    def W8(self):
        sum = 0       
        for f, amt in self.V.viewitems():
            it = amt * math.pow(f/float(self.N), 2)
            sum = sum + it
        yule = (-1.0/self.N + sum)
#       print amt
#       print it       
#       print self.N
#       print sum
#       print yule
        return yule
#       W8: Medida K de Yule*
    @property
    def W9(self):
        simpson = 0
        i=1
#       OBS2: Sentenças de apenas uma palavra tornam a funcao indefinida
        for f, amt in self.V.viewitems():
            it = amt *(i / float(self.N)) * ((i-1.0) / (self.N - 1.0))
            simpson = simpson + it
            i=i+1
#       print amt
#       print i
#       print self.N
#       print it 
#       print simpson        
        return simpson
#       W9: Medida D de Simpson*
    @property
    def W10(self):
        return len(self.V) / float(self.VRICH)
#       W9: Medida S de Sichel*
    @property
    def W11(self):
        hlego_count = len(self.HXLEGO)
        v_count = float(self.VRICH)
#       print hlego_count
#       print v_count        
#       W11: Medida R de Honore*        
        if hlego_count == v_count:
            return 0
        else:
            return (100.0 * math.log10(self.N)) / float(1.0-(hlego_count/float(v_count))) 
    @property
    def W12(self):
        entropy = 0
        for f, amt in self.V.viewitems():
            it = amt * (-math.log10(f/float(self.N))) * (f/float(self.N))
            entropy = entropy + it
#       print f
#       print amt
#       print self.N
#       print it 
#       print entropy
#       max = float(math.log10(self.N))        
        return entropy# / max
#       W12: Medida de Entropia*
    @property
    def W13_N(self):
#       OBS3: A maior palavra em portugues possui tamanho 46, segundo o dicionário Houaiss
        vFreq = numpy.zeros([self.nMaxLengthFreq])      
        for item in nltk.FreqDist(self.SIZES).items():           
            if item[0] < self.nMaxLengthFreq:
                vFreq[item[0]-1] = item[1]/float(self.N)
#            if item[0] >50:
#                print self.raw
#                print nltk.FreqDist(self.SIZES).items()
#                print item
#                print vFreq
#                raw_input('+++++++++++')
        return vFreq
#       W13_N: Razão entre a distribuição de frequência do tamanho das palavras (16 meta-atributos diferentes) e o total de palavras (P)
   
    '''
    -----------------------------------------------------------------------------------------------------------------------
    META ATRIBUTOS BASEADOS EM ANALISE DA ESTRUTURA TEXTUAL (TS) - 10 meta-atributos
    -----------------------------------------------------------------------------------------------------------------------
    ''' 
   
    @property
    def TS1(self):
        return self.S
#       TS1: Quantidade total de frases (F)
    @property
    def TS2(self):
        return len(self.PARAGRAPHS)
#       TS2: Quantidade total de parágrafos
    @property
    def TS3(self):
        sents_per_paragraph = []
        for p in self.PARAGRAPHS:
            sents_per_paragraph.append(len(p))
        return numpy.average(sents_per_paragraph)
#       TS3: Média de frases (F) por parágrafo
    @property
    def TS4(self):
        words_per_paragraph = []
        for p in self.PARAGRAPHS:
            total_words = 0
            for s in p:
                for w in s:
                    if w.isalpha():
                        total_words = total_words + 1
            words_per_paragraph.append(total_words)
        return numpy.average(words_per_paragraph)
#       TS4: Média de palavras (P) por parágrafo
    @property
    def TS5(self):
        chars_per_paragraph = []
        for p in self.PARAGRAPHS:
            total_chars = 0
            for s in p:
                for w in s:
                    total_chars = total_chars + len(w)
            chars_per_paragraph.append(total_chars)
        return numpy.average(chars_per_paragraph)
#       TS5: Média de caracteres (C) por parágrafo
    @property
    def TS6(self):
        words_per_sentence = []
        for p in self.PARAGRAPHS:
            for s in p:
                total_words = 0
                for w in s:
                    if w.isalpha():
                        total_words = total_words + 1
                words_per_sentence.append(total_words)
        return numpy.average(words_per_sentence)
#       TS6: Média de palavras (P) por frase (F)
    @property
    def TS7(self):
        amt = 0
        for p in self.PARAGRAPHS:
            for s in p:
                if len(s)>0:
                    first_char = s[0][0]
                    if first_char.islower():
                        amt = amt + 1
        return amt / float(self.S)
#       TS7: Razão entre o número de frases iniciadas por letra minúscula (a-z) e o número total de frases (F)
    @property
    def TS8(self):
        amt = 0        
        for p in self.PARAGRAPHS:            
            for s in p:
                if len(s)>0:
                    first_char = s[0][0]
                    if first_char.isupper():
                        amt = amt + 1                
        return amt / float(self.S)       
#       TS8: Razão entre o número de frases iniciadas por letra maiúscula (A-Z) e o número total de frases (F)
    @property
    def TS9(self):
        blank = 0
        for p in self.PARAGRAPHS:
            if len(p) == 0:
                blank = blank + 1
        return blank / float(self.TS2)
#       TS9: Razão entre o número de linhas em branco e o total de parágrafos
    @property
    def TS10(self):
        lenghts = []
        for p in self.PARAGRAPHS:
            lenght = 0
            for s in p:                
                for w in s:
                    #if len(w)>0:                        
                    lenght = lenght + len(w)
            lenghts.append(lenght)
        return numpy.average(lenghts)
#       TS10: Quantidade média de caracteres em linhas não vazias
        
    '''
    -----------------------------------------------------------------------------------------------------------------------
    META ATRIBUTOS BASEADOS EM ANALISE DA MORFOLOGIA TEXTUAL (TM) - 6 meta-atributos
    -----------------------------------------------------------------------------------------------------------------------
    '''

    @property
    def TM1(self):
        articles = []
        for word, tag in self.TAGGED:
            if tag == 'ART':
                articles.append(word)
        freqdist = nltk.FreqDist(articles)

        article_ratio = {}
        for article, freq in freqdist.viewitems():
            article_ratio = freq / float(self.N)
        return article_ratio
#       TM1: Razão entre o número de artigos e o total de palavras (P)
    @property
    def TM2(self):
        freqdist = self._morfo_freq(['PROADJ', 'PRO-KS', 'PROPESS', 'PRO-KS-REL', 'PRO-SUB'])

        pronoun_ratio = {}
        for pronoun, freq in freqdist.viewitems():
            pronoun_ratio = freq / float(self.N)
        return pronoun_ratio
#       TM2: Razão entre o número de pronomes e o total de palavras (P)
    @property
    def TM3(self):
        freqdist = self._morfo_freq('VAUX')

        verb_ratio = {}
        for verb, freq in freqdist.viewitems():
            verb_ratio = freq / float(self.N)
        return verb_ratio
#       TM3: Razão entre o número de verbos-auxiliares e o total de palavras (P)
    @property
    def TM4(self):
        freqdist = self._morfo_freq(['KC', 'KS'])

        conj_ratio = {}
        for conj, freq in freqdist.viewitems():
            conj_ratio = freq / float(self.N)
        return conj_ratio
#       TM4: Razão entre o número de conjunções e o total de palavras (P)
    @property
    def TM5(self):
        freqdist = self._morfo_freq('IN')

        inter_ratio = {}
        for inter, freq in freqdist.viewitems():
            inter_ratio = freq / float(self.N)
        return inter_ratio
#       TM5: Razão entre o número de interjeições e o total de palavras (P)
    @property
    def TM6(self):
        freqdist = self._morfo_freq('PREP')

        prep_ratio = {}
        for prep, freq in freqdist.viewitems():
            prep_ratio = freq / float(self.N)
        return prep_ratio
#       TM6: Razão entre o número de preposições e o total de palavras (P)    
    
    '''   
    -----------------------------------------------------------------------------------------------------------------------
    META ATRIBUTOS BASEADOS EM SOCIOLINGUISTICA (Psycholinguistic Cues)
    -----------------------------------------------------------------------------------------------------------------------
    A partir daqui atributos sociolinguisticos baseados em dicionario
    '''
#    def ma_dict_x(dictionary,tokenizedText):
    
#    nTokensInText = len(tokenizedText)
#    nWordsFound = 0    
#    for iToken in range(0,nTokensInText):
#        if tokenizedText[iToken] in dictionary:
#            nWordsFound = nWordsFound + 1
            
#    p = nWordsFound/float(nTokensInText)
#    return p
    
    @property
    def PC1(self):
    
        nTokensInText = len(self.WORDS)
        nWordsFound = 0    
        for iToken in range(0,nTokensInText):
            if self.WORDS[iToken] in self.pwdictionary:
                nWordsFound = nWordsFound + 1
           
        PW = nWordsFound/float(nTokensInText)
        return PW
    
    @property        
    def PC2(self):
    
        nTokensInText = len(self.WORDS)
        nWordsFound = 0    
        for iToken in range(0,nTokensInText):
            if self.WORDS[iToken] in self.nwdictionary:
                nWordsFound = nWordsFound + 1
           
        NW = nWordsFound/float(nTokensInText)
        return NW
    
    @property
    def PC3(self):
    
        nTokensInText = len(self.WORDS)
        nWordsFound = 0    
        for iToken in range(0,nTokensInText):
            if self.WORDS[iToken] in self.neutralwdictionary:
                nWordsFound = nWordsFound + 1
           
        NEUTRAL = nWordsFound/float(nTokensInText)
        return NEUTRAL  
            
    @property
    def PC4(self):
    
        nTokensInText = len(self.WORDS)
        nWordsFound = 0    
        for iToken in range(0,nTokensInText):
            if self.WORDS[iToken] in self.pedictionary:
                nWordsFound = nWordsFound + 1
           
        PE = nWordsFound/float(nTokensInText)
        return PE
            
    @property        
    def PC5(self):
    
        nTokensInText = len(self.WORDS)
        nWordsFound = 0    
        for iToken in range(0,nTokensInText):
            if self.WORDS[iToken] in self.nedictionary:
                nWordsFound = nWordsFound + 1
           
        NE = nWordsFound/float(nTokensInText)
        return NE
        
    '''
    -----------------------------------------------------------------------------------------------------------------------

    -----------------------------------------------------------------------------------------------------------------------
    '''
    def _morfo_freq(self, part_of_speech):
        if isinstance(part_of_speech, str):
            part_of_speech = [part_of_speech]

        words = []
        for word, tag in self.TAGGED:
            if tag in part_of_speech:
                words.append(word)
        return nltk.FreqDist(words)
    
    '''
    -----------------------------------------------------------------------------------------------------------------------
    MECANISMO PARA CONSTRUÇÃO DE VETOR NUMPY DE CARACTERÍSTICAS (META-ATRIBUTOS)
    -----------------------------------------------------------------------------------------------------------------------
    '''
       
    @property
    def all_meta_attributes(self):
        vMA = numpy.array([])
#        lMA = []       
        
#        analise de caracteres (16)
#        -------------------------------------------------------------------------
        for i in range(1,17):       
          
            vMA = numpy.append(vMA,getattr(self, 'C' + str(i)))
#            lMA.append(('C' + str(i), vMA[-1]))
        
#        analise de palavras (13)
#        -------------------------------------------------------------------------
        for i in range(1,13):        
           # listMetrics.append(('f0'+str(i),getattr(metrics, 'f0' + str(i))))
            vMA = numpy.append(vMA,getattr(self, 'W' + str(i)))
#            lMA.append(('W' + str(i), vMA[-1]))
        
#        Atributo 13 (vetor com n atributos)
        m = self.W13_N    
        for i in range(0,m.shape[0]):
            vMA = numpy.append(vMA,m[i])            
#            lMA.append(('W13_' + str(i), vMA[-1]))
        

#        analise de estrutura do texto (10)  
#        -------------------------------------------------------------------------       
        for i in range(1,11):        
#           listMetrics.append(('f'+str(i),getattr(metrics, 'f' + str(i))))
            vMA = numpy.append(vMA,getattr(self, 'TS' + str(i)))
#            lMA.append(('TS' + str(i), vMA[-1]))
      
#        analise morfologica
#        -------------------------------------------------------------------------
        for i in range(1,7):        
           
            vMA = numpy.append(vMA,getattr(self, 'TM' + str(i)))
 #           lMA.append(('TM' + str(i), vMA[-1]))
        
#       dicionarios psicolinguisticos
#       ---------------------------------------------------------------------------
        for i in range(1,6):        
           
            vMA = numpy.append(vMA,getattr(self, 'PC' + str(i)))
#            lMA.append(('PC' + str(i), vMA[-1]))
           
           
#        print lMA
#        print len(lMA)
        #raw_input('-------------------------------------------')
      
        return vMA
     
    
   