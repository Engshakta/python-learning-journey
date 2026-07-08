print("---1. Testing full module alliasing----")

import math as m

print(f"PI via mode alias : {m.pi}")

try:
    print(math.pi)
except NameError as e:
    print(f"expected crash: {e}")

print("\n--- 2. Testing Direct Entity Aliasing ---")

from math import e as Euler, floor as floor_intiger
print(f"Euler's constant via alias: {Euler}")
print(f"Floor's calculation via allias: {floor_intiger(9.9)}")

try:
    print(e)
except NameError as e:
    print(f"expected crash : {e}")
