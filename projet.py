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
