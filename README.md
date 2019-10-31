# hetio-net
CSCI 493.71: Big Data  
Project I: Model of HetioNet

Khan_Rafi: Khinshan Khan and Shakil Rafi

## Requirements

- Python 3+
- mongo 4+
- neo4j 3.5+
- Java 8
- pymongo 3.9.0
- py2neo 4.3.0

## Setup

The following instructions were tested on Arch Linux:

- start the MongoDB service:
    - `sudo systemctl enable mongodb.service`
- start the neo4j service:
  - `sudo systemctl start neo4j.service`
- in the file `/etc/neo4j/neo4j.conf` make sure that `dbms.directories.import` is set to `/var/lib/neo4j/import`.
- the directory `/var/lib/neo4j/import/` should exist and your user should have read and write access to it:
    - by default, this directory will be owned by the `neo4j` user and the `neo4j` group
    - `usermod -a -G neo4j $(whoami)`
- the default neo4j username is `neo4j` and the password is `password`
    - modify `utils/common.py` to match your neo4j username and password

## Run

From download:

```bash
cd Khan_Rafi
python app.py
```

From GitHub:

```bash
git clone https://github.com/kkhan01/hetio-net
cd hetio-net
python app.py
```

## Further Analysis Notes

### edges.tsv relationships

#### Compound
- CrC = Compound Resembles Compound
- CtD = Compound Treats Disease
- CpD = Compound Palliates Diseases
- CuG = Compound Upregulates Genes
- CbG = Compound Binds Genes
- CdG = Compound Downregulates Gene
#### Disease
- DrD = Disease Resembles Disease
- DlA = Disease Localizes Anatomy
- DuG = Disease Upregulates Gene
- DaG = Disease Associates Genes
- DdG = Disease Downregulates Genes
#### Anatomy
- AuG = Anatomy Upregulates Genes
- AeG = Anatomy Expresses Gene
- AdG = Anatomy Downregulates Genes
#### Gene
- Gr>G = Gene Regulates Gene
- GcG = Gene Covaries Gene
- GiG = Gene Interacts Gene
