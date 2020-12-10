#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 16:42:23 2020

@authors: singaresekou & laminegueye
"""
#Importation
import findspark
findspark.init
from pyspark import SparkConf
from pyspark import SparkContext

#Instanciation
sc = SparkContext.getOrCreate(SparkConf().setMaster("local[*]"))

#Importation du fichier txt
text_file = sc.textFile("sample.txt")

#Le word count
counts = text_file.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
             
#Affichage du resultat sous la forme (clé, valeur)
for x in counts.collect():
    print(x)
    
#Export du fichier resultant 
counts.coalesce(1).saveAsTextFile("projet.txt")
