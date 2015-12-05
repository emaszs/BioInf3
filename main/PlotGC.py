from Bio.Blast import NCBIWWW, NCBIXML
from Bio import SeqIO
from Bio.SeqUtils import GC
import pylab
# from Bio.Blast.Applications import NcbiblastnCommandline


gc_value_list = []

sequence_list = []
for rec in SeqIO.parse("reads_for_analysis.fastq", "fastq"):
    sequence_list.append(rec.seq)
    gc_value_list.append(GC(rec.seq))


genes_to_query = []
for i in range(len(gc_value_list)):
    if (gc_value_list[i] >= 85) :
        for j in range(i-2, i+3):
            if (j >= 0 and j < len(gc_value_list)):
                genes_to_query.append(j)

print (genes_to_query)
print(sequence_list[6045])
pylab.plot(gc_value_list)
pylab.xlabel("Genai")
pylab.ylabel("C ir G %")
pylab.show()


# blastn_cline = NcbiblastnCommandline(query="mi_in.fasta", db="nt", out="my_out.xml", remote=True)
# stdout, stderr = blastn_cline()

print("Querying")
enterez_query = "bacteria[Organism]"
ncbi = NCBIWWW.qblast(program="blastn" , database="nt", 
                                sequence=sequence_list[6045], 
                                entrez_query=enterez_query, expect=10.0, hitlist_size=1) #seka, pagal kuria ieskoma  galima nurodyti ir kodu
 
blast = NCBIXML.read(ncbi)
for sequence in blast.alignments:
    print ('>%s'%sequence.title) # rasto atitikmens pavadinimas fasta formatu