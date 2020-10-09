from ants import *
hive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
colony = AntColony(None, hive, ant_types(), layout, dimensions)
p0 = colony.places["tunnel_0_0"]
p1 = colony.places["tunnel_0_1"]  # p0 is p1's exit
bee = Bee(2)
ninja = NinjaAnt()

thrower = ThrowerAnt()
p0.add_insect(thrower)
p1.add_insect(bee)
p1.add_insect(ninja)

print(ninja.place.name)
print("Ninja")
bee.action(colony)
