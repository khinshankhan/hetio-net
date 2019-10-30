# hetio-net
Model of HetioNet

Khan_Rafi: Khinshan Khan and Shakil Rafi

## Installation
- [ ] Have this project on a path that you can execute scripts
- [ ] Python 3+
- [ ] mongo 4+
- [ ] neo4j 3.5+
- [ ] Java 8
- [ ] pymongo
- [ ] neo2py
- [ ] start the neo4j
  - `sudo systemctl start neo4j.service` or check your distro's way
- [ ] start the
  - `sudo systemctl enable mongodb.service` or check your distro's way

On arch or an arch based distro, you can run:
```bash
yay -S python
yay -S mongo
yay -S neo4j-community
pip install pymongo
pip install neo2py
```

Notes:
- You should have a directory `/var/lib/neo4j/import/` which the user executing
  the program has permissions to.
- The neo4j username should be `neo4j` and password should be `password`. This
  can be set at [http://localhost:7474](http://localhost:7474)
  - If you need to, you can modify the source code's variables int the project
    root's `utils/common.py`
- You may encounter some path problems since the community version of neo4j
  is a little broken on arch. Simply run `export PATH=/usr/share/neo4j/bin:$PATH`.
- In `/etc/neo4j/neo4j.conf`, `dbms.directories.import` should be set to
  `/var/lib/neo4j/import`.
- Neo4j requires Java 8
- It is recommended to install python packages in a
  [virtualenv](https://docs.python-guide.org/dev/virtualenvs/)

## Run
Navigate over to the project root and run `python app.py`

## Further Analysis Notes

### edges.tsv relationships

#### Compount
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
