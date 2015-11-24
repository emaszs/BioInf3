
f = open("reads_for_analysis.fastq", "r")
i = 0
charsFound = []
while i < 20000:
    i += 1
    
    next(f)
    next(f)
    next(f)
    line = f.readline().strip()

    for c in line:
        if c not in charsFound:
            charsFound.append(c)
    
    
f.close()

print("Rasti simboliai naudojami kokybes kodavimui:")
print(charsFound)

if "0" in charsFound:
    # Sanger phred+33 arba Illumina 1.8+ phred+33
    if "J" in charsFound:
        print("Naudojama Illumina 1.8+ phred+33 koduote")
    else:
        print("Naudojama Sanger phred+33 koduote")
else:
    #Solexa+64, Illumina 1.3+ Phred+64 arba Illumina 1.5+ Phred+64
    if "=" in charsFound:
        print("Naudojama Solexa+64 koduote")
    elif "A" in charsFound:
        print("Naudojama Illumina 1.3+ phred+64 koduote")
    else:
        print("Naudojama Illumina 1.5+ phred+64 koduote")



