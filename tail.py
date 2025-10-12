import sys, pathlib
if len(sys.argv)<2: print('Usage: tail.py <file> [n]'); raise SystemExit
n = int(sys.argv[2]) if len(sys.argv)>2 else 10
lines = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8', errors='ignore').splitlines()
for l in lines[-n:]: print(l)
