# This file describes the environmental variables in the game Mudbourne.

# Gameplay takes place in either the Waking or the Dream world at any given
# time, and all living things are naturally occurring in one or the other,
# but rarely both (and in case of both, they may have different properties
# in the two contexts).
all_domains = set(("Waking", "Dream"))

# Parallel between both domains, the same set of locations are present, with
# only slight differences in layout (mainly stairs, bridges, and doors). The
# paired_locations dict contains Waking domain locations as keys and Dream
# domain locations as values.
paired_locations = {
    "Spawning Pools":"Distant Pools",
    "Kindergarten":"Future Farms",
    "Residential District":"Homeward Bound",
    "Climate Control":"Frozen Dreams",
    "Central Junction":"Dream Core",
    "Restricted Research":"Memory Works",
    "Golden Isles (Waking)":"Golden Isles (Dream)"
}
waking_locations = set(paired_locations.keys())
dream_locations = set(paired_locations.values())
temperate_waking_locations = waking_locations.copy()
temperate_waking_locations.remove("Climate Control")
temperate_dream_locations = dream_locations.copy()
temperate_dream_locations.remove("Frozen Dreams")
temperate_waking_northern = temperate_waking_locations.copy()
temperate_waking_northern.remove("Spawning Pools")
all_locations = set.union(waking_locations, dream_locations)

# Habitats are specific features that are required for some critters (bugs)
# to spawn, in addition to any climate and weather requirements.
all_habitats = set(("Reeds", "Red Lilies", "Lilypads", "Millipads",
    "Dream Orchids", "Mother Jellies", "Mahopany Trees", "Marsh Shrubs"))

# Tile types are the normally-immutable properties of a tile. However,
# in the Climate Control (and its parallel Frozen Dreams) location only,
# water can be converted to ice and vice versa, and the natural precipitation
# is snow and not rain. Stagnant water is only naturally ocurring in an area
# of the Kindergarten (and parallel Future Farms), but it can be temporarily
# created in a very small area by one of the machines you can acquire.
all_tile_types = set(("grass", "mud", "ice", "water", "deep water",
    "stagnant water", "inside"))

# Weather is a binary state of either raining or not raining in most locations,
# and either snowing or not snowing in the Climate Control (Frozen Dreams)
# location. There are machines you can acquire in-game that modify a very
# small area's weather.
all_weather = set(("raining", "not raining", "snowing")) # not snowing is just not raining
all_times = set(("Daytime", "Nighttime", "Dawn", "Dusk"))

# Temperature is predictable for a given time of day as follows. Note that
# snow effectively decreases the temperature level by one in all cases.cccccbenhtdlhbivfteufkhfjkeveehkbeldherrhvub

#
# Dawn (5:00-7:00): Warm (clear, raining) or Mild (snowing)
# Day (7:00-19:00): Balmy (clear, raining) or Warm (snowing)
# Dusk (19:00-21:00): Warm (clear, raining) or Mild (snowing)
# Night (21:00-5:00): Chilly (clear, raining) or Cold (snowing)
#
# Extreme temperatures can only be achieved artificially, with machines to
# heat (Hot) or cool (Frozen) a small area. Effects from multiple machines
# in overlapping areas are not additive, but they are additive with the
# effect of precipitation.
temperature_scale = {
    1:"Frozen",
    2:"Cold",
    3:"Chilly",
    4:"Mild",
    5:"Warm",
    6:"Balmy",
    7:"Hot"
}
all_temperatures = set(temperature_scale.values())

# Humidity is a factor of tile type and whether it's raining (but not
# snowing). Rain increases the default tile humidity level by one.
#
# Normal (not raining) humidity on each type of tile is:
#
# Inside: Dry (2)
# Grass: Normal (3)
# Mud: Damp (4)
# Water: Wet (5)
#
# Humidity also can be modified by in-game machines over a small area.
# As with temperature, multiple machines' effects are not additive, but they
# are additive with the effects of rain. Additionally, cultivators, spore
# cultivators, and farmers use compost which may also affect humidity for
# any flora they grow. Namely, absorbant compost nullifies the increment
# to humidity that normally occurs with rain, and insulating compost
# nullifies snow's effect on temperature.
humidity_scale = {
    1:"Parched",
    2:"Dry",
    3:"Normal",
    4:"Damp",
    5:"Wet",
    6:"Drenched",
    7:"Waterlogged"
}
all_humidities = set(humidity_scale.values())
