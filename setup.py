import os
import sys
os.system("apt update -y")
os.system("apt upgrade -y")
os.system("apt install python -y")
os.system("apt install git -y")
os.system("apt install python2 -y")
os.system("mv CyPher.py ~/../usr/bin")
os.system("echo python ~/../usr/bin/CyPher.py > cypher")
os.system("chmod +x cypher")
os.system("mv cypher ~/../usr/bin")
print("Run By cypher")
