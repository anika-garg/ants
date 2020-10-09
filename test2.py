from ants import *
hive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
colony = AntColony(None, hive, ant_types(), layout, dimensions)
 #
 # Test LongThrower Hit
ant = LongThrower()
in_range = Bee(2)
colony.places['tunnel_0_0'].add_insect(ant)
colony.places["tunnel_0_5"].add_insect(in_range)
ant.action(colony)
