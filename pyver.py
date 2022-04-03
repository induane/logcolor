import sys


info = sys.version_info
sys.stdout.write(f"python{info.major}.{info.minor}")
sys.stdout.flush()
sys.exit(0)
