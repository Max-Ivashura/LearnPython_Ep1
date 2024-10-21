# ---------- .txt ----------

file_path = "test_data/output.txt"

try:
  with open(file_path, 'r') as file:
     content = file.read()
     print(content)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")

# ---------- .json ----------
import json

file_path = "test_data/output.json"

try:
  with open(file_path, 'r') as file:
      content = json.load(file)
      print(content )
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")

# ---------- .csv ----------
import csv

file_path = "test_data/output.csv"

try:
  with open(file_path, 'r') as file:
      content = csv.reader(file)
      for line in content:
          print(line)
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to read that file")