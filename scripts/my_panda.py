import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))

from envtest import panda

print(panda())
