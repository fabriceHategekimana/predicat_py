# import module:
utilitaires pour l'import et l'export des données (actuellement en format csv)

## toCSV(name, csvFormat):
Export the datas to csv

## fromCSV(name):
Import the datas from csv

## fromCSVTable(name, columnid, entity):#entity is the classe/type of the tuple
Can import csvs that doesent follow the shape of a triplet. A columnid is given as the id and every other column ar constructed by those triplets:
columnid targetColumnName targetColumnValue0, etc.
