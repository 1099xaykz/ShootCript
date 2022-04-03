import os
import sys

def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

def main():
  slowprint("Instalando...")
  os.system("pip install requests")
  os.system("py -m install requests")
  os.system("python -m install requests")
  print("Instalado")
  
if __name__=="__main__":
  main()
