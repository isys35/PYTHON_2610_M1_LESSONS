from pathlib import Path

wave = Path("ocean", "wave.txt")

print(wave)

home = Path.home()

print(home)

absolute_wave = Path(home, wave)

print(absolute_wave)

print(absolute_wave.name)
print(absolute_wave.suffix)

tides = absolute_wave.with_name("tides.txt")

print(tides)

WORKING_DERICTORY = Path(__file__).parent.parent
print(WORKING_DERICTORY)



