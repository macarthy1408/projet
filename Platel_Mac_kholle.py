#!/usr/bin/python3.6
import csv
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-l', action='store_true', help='affiche les valeurs')
parser.add_argument('-a', nargs='+', help='ajouter des valeurs dans le fichier')
parser.add_argument('-c', action='store_true', help='efface les valeurs')
samepren = parser.add_argument_group(title='subcommands', description='parce qu on le demande avec un -s devant')
samepren.add_argument('-s', action='store_true', help='rajoute une option derriere')
samepren.add_argument('--max', action='store_true', help='donne la plus grand valeurs')
samepren.add_argument('--min', action='store_true', help='donne la plus petite valeurs')
samepren.add_argument('--moy', action='store_true', help='donne la moyenne des valeurs')
samepren.add_argument('--sum', action='store_true', help='donne la somme des valeurs')
latete = parser.add_argument_group(title='latete', description='groupe pour l affiche de l ordre')
latete.add_argument('-t', action='store_true', help='affiche les valeurs dans l ordre croissant')
latete.add_argument('--desc', action='store_true', help='affiche les valeurs dans l ordre decroissant')
args = parser.parse_args()

list = []

if args.l:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier: print row
elif args.a:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier:
    for i in range(len(row)):
      list.append(row[i]) 
  for n in args.a:
    list.append(n)
  c = csv.writer(open("fichier.csv", "wb"))
  c.writerow(list)  
elif args.c:
  fichier = csv.writer(open("fichier.csv", "w"))
  fichier.writerow("")
elif args.s and args.min:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier:
    for i in range(len(row)):
      list.append(row[i])
  min = 999999
  for i in range(len(list)):
    if int(list[i]) < min:
      min = int(list[i])
  print("le chiffre le plus petit est", min)
elif args.s and args.max:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier:
    for i in range(len(row)):
      list.append(row[i])
  max = 0
  for i in range(len(list)):
    if int(list[i]) > min:
      min = int(list[i])
  print("le chiffre le plus grand est", min)
elif args.s and args.sum:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier:
    for i in range(len(row)):
      list.append(row[i])
  somme = 0
  for i in range(len(list)):
      somme = somme + int(list[i])
  print("la somme est", somme)
elif args.s and args.moy:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier:
    for i in range(len(row)):
      list.append(row[i])
  somme = 0
  for i in range(len(list)):
      somme = somme + int(list[i])
  moyenne = somme/len(list)
  print("la moyenne est de", moyenne)
elif args.t and args.desc:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier:
    for i in range(len(row)):
      list.append(row[i])
  desc = sorted(list, reverse=True)
  print(desc)
elif args.t:
  fichier = csv.reader(open("fichier.csv", "r"))
  for row in fichier:
    for i in range(len(row)):
      list.append(row[i])
  asc = sorted(list)
  print(asc)
