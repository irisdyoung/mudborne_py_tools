# Complete collection of mushroom species implemented in Mudborne

from fungi import Mushroom

stout_funnel = Mushroom(
    name="Stout Funnel",        domain="Waking",        tile_type="water",
    temperature="Balmy",        humidity="Drenched",    weather="raining",
    effects="+1 A")
flat_stinkhorn = Mushroom(
    name="Flat Stinkhorn",      domain="Waking",        tile_type="grass",
    temperature="Balmy",        humidity="Normal",      weather="not raining",
    effects="+1 N, +1 O")
bothersome_fungus = Mushroom(
    name="Bothersome Fungus",   domain="Waking",        tile_type="mud",
    temperature="Warm",         humidity="Damp",        weather="not raining",
    effects="+1 U, +1 E")
withering_rot = Mushroom(
    name="Withering Rot",       domain="Waking",        tile_type="mud",
    temperature="Chilly",       humidity="Damp",        weather="not raining",
    effects="-1 A, -1 S")
shrinking_cap = Mushroom(
    name="Shrinking Cap",       domain="Waking",        tile_type="stagnant water",
    temperature="Balmy",        humidity="Damp",        weather="not raining",
    effects="-1 A, -1 O")
pickled_bonnet = Mushroom(
    name="Pickled Bonnet",      domain="Waking",        tile_type="inside",
    temperature="Mild",         humidity="Parched",     weather="not raining",
    effects="+1 A, +1 S")
raucous_conecap = Mushroom(
    name="Raucous Conecap",     domain="Waking",        tile_type="water",
    temperature="Balmy",        humidity="Waterlogged", weather="raining",
    effects="+1 O, +1 R")
grubby_parachute = Mushroom(
    name="Grubby Parachute",    domain="Waking",        tile_type="mud",
    temperature="Warm",         humidity="Wet",         weather="not raining",
    effects="-1 N")
frosty_jack = Mushroom(
    name="Frosty Jack",         domain="Waking",        tile_type="water",
    temperature="Hot",          humidity="Wet",         weather="not raining",
    effects="-1 U, +1 E")
filling_oyster = Mushroom(
    name="Filling Oyster",      domain="Waking",        tile_type="grass",
    temperature="Frozen",       humidity="Normal",      weather="raining",
    effects="-1 E")
bulbous_muffler = Mushroom(
    name="Bulbous Muffler",     domain="Waking",        tile_type="mud",
    temperature="Cold",         humidity="Damp",        weather="snowing",
    effects="-1 R")
squat_amplifier = Mushroom(
    name="Squat Amplifier",     domain="Dream",         tile_type="mud",
    temperature="Balmy",        humidity="Wet",         weather="raining",
    effects="x2 N, x2 U")
towering_expander = Mushroom(
    name="Towering Expander",   domain="Dream",         tile_type="grass",
    temperature="Warm",         humidity="Normal",      weather="not raining",
    effects="x2 N")
fools_mirror = Mushroom(
    name="Fool's Mirror",       domain="Dream",         tile_type="water",
    temperature="Chilly",       humidity="Wet",         weather="not raining",
    effects="x-1 A, x-1 N")
bloating_mould = Mushroom(
    name="Bloating Mould",      domain="Dream",         tile_type="inside",
    temperature="Mild",         humidity="Dry",         weather="not raining",
    effects="suppress O, x2 S")
stinking_bolete = Mushroom(
    name="Stinking Bolete",     domain="Dream",         tile_type="stagnant water",
    temperature="Warm",         humidity="Damp",        weather="not raining",
    effects="suppress N, x2 O")
pointed_deceiver = Mushroom(
    name="Pointed Deceiver",    domain="Dream",         tile_type="inside",
    temperature="Mild",         humidity="Normal",      weather="not raining",
    effects="suppress A, -1 S")
chattering_bell = Mushroom(
    name="Chattering Bell",     domain="Dream",         tile_type="grass",
    temperature="Chilly",       humidity="Damp",        weather="raining",
    effects="x-1 O, x2 R")
false_suppressor = Mushroom(
    name="False Suppressor",    domain="Dream",         tile_type="inside",
    temperature="Chilly",       humidity="Dry",         weather="not raining",
    effects="suppress U, x2 E")
velvet_inverter = Mushroom(
    name="Velvet Inverter",     domain="Dream",         tile_type="grass",
    temperature="Hot",          humidity="Normal",      weather="not raining",
    effects="x-1 R, x-1 E")
rude_awakening = Mushroom(
    name="Rude Awakening",      domain="Dream",         tile_type="grass",
    temperature="Hot",          humidity="Damp",        weather="raining",
    effects="min N")
torrential_prune = Mushroom(
    name="Torrential Prune",    domain="Dream",         tile_type="mud",
    temperature="Mild",         humidity="Normal",      weather="not raining",
    effects="min A, MAX S")
booming_mane = Mushroom(
    name="Booming Mane",        domain="Dream",         tile_type="water",
    temperature="Mild",         humidity="Damp",        weather="not raining",
    effects="MAX O, MAX R")
chill_pill = Mushroom(
    name="Chill Pill",          domain="Dream",         tile_type="inside",
    temperature="Chilly",       humidity="Normal",      weather="not raining",
    effects="min U")
