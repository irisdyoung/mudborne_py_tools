from critters import Critter

dracofly = Critter(
    name="Dracofly",                flavor="Salty",
    domain="Waking",                locations=waking_locations,
    habitat="Reeds",                tile_types="water",
    time="Daytime",                 weather="raining")
empress = Critter(
    name="Speckled Empress",        flavor="Sweet",
    domain="Waking",                locations=waking_locations,
    habitat="Red Lilies",           tile_types="water",
    time="Daytime",                 weather="not raining")
marshfly = Critter(
    name="Marshfly",                flavor="Salty",
    domain="Waking",                locations=waking_locations,
    habitat="Lilypads",             tile_types="water",
    time="Dawn",                    weather="not raining")
pond_skater = Critter(
    name="Pond Skater",             flavor="Bitter",
    domain="Waking",                locations=waking_locations,
    habitat="Millipads",            tile_types="water",
    time="Dusk",                    weather="not raining")
dreamfly = Critter(
    name="Dreamfly",                flavor="Sour",
    domain="Dream",                 locations=dream_locations,
    habitat="Reeds",                tile_types="water",
    time="Daytime",                 weather="not raining")
forgotten_wish = Critter(
    name="Forgotten Wish",          flavor="Umami",
    domain="Dream",                 locations=dream_locations,
    habitat="Dream Orchids",        tile_types="water",
    time="Daytime",                 weather="raining")
firefly = Critter(
    name="Firefly",                 flavor="Spicy",
    domain="Dream",                 locations=dream_locations,
    habitat="Lilypads",             tile_types="water",
    time="Nighttime",               weather="not raining")
moon_jelly = Critter(
    name="Moon Jelly",              flavor="Slimy",
    domain="Dream",                 locations=dream_locations,
    habitat="Mother Jellies",       tile_types="water",
    time="Dawn",                    weather="not raining")
pink_dasher = Critter(
    name="Pink Dasher",             flavor="Sweet",
    domain="Waking",                locations=waking_locations,
    habitat="Mahopany Trees",       tile_types="grass",
    time="Dawn",                    weather="not raining")
bush_cricket = Critter(
    name="Bush Cricket",            flavor="Salty",
    domain="Waking",                locations=waking_locations,
    habitat="Marsh Shrubs",         tile_types="grass",
    time="Nighttime",               weather="not raining")
orchard_bee = Critter(
    name="Orchard Bee",             flavor="Spicy",
    domain="Waking",                locations=waking_locations,
    habitat="Beehives",             tile_types="grass, water",
    time="Daytime",                 weather="not raining")
swamp_glider = Critter(
    name="Swamp Glider",            flavor="Bitter",
    domain="Dream",                 locations=dream_locations,
    habitat="Stagnant Rushes",      tile_types="water",
    time="Daytime",                 weather="raining")
dreamcutter_bee = Critter(
    name="Dreamcutter Bee",         flavor="Umami",
    domain="Dream",                 locations=dream_locations,
    habitat="Beehives",             tile_types="grass, water",
    time="Nighttime",               weather="not raining")
radiant_skipper = Critter(
    name="Radiant Skipper",         flavor="Sour",
    domain="Waking",                locations=["Residential District"],
    habitat="Azure Hearts",         tile_types="water",
    time="Nighttime",               weather="not raining")
ladybug = Critter(
    name="Seven-spotted Lady",      flavor="Sweet",
    domain="Waking",                locations=waking_locations,
    habitat="Marsh Shrubs",         tile_types="grass",
    time="Dawn",                    weather="not raining")
watchman = Critter(
    name="Purple Watchman",         flavor="Slimy",
    domain="Dream",                 locations=dream_locations,
    habitat="Stone Lanterns",       tile_types="grass, water",
    time="Nighttime",               weather="not raining")
frosted_weevil = Critter(
    name="Frosted Weevil",          flavor="Umami",
    domain="Waking",                locations=["Climate Control"],
    habitat="Marsh Shrubs",         tile_types="grass",
    time="Daytime",                 weather="not raining")
icy_gale = Critter(
    name="Icy Gale",                flavor="Bitter",
    domain="Waking",                locations=["Climate Control"],
    habitat="Croakfeet",            tile_types="water",
    time="Dawn",                    weather="snowing")
dream_weaver = Critter(
    name="Dream Weaver",            flavor="Slimy",
    domain="Dream",                 locations=waking_locations,
    habitat="Doorways",             tile_types="grass, water",
    time="Nighttime",               weather="not raining")
memory_tumbler = Critter(
    name="Memory Tumbler",          flavor="Spicy",
    domain="Dream",                 locations=["Memory Works"],
    habitat="Fragmented Memories",  tile_types="grass, water",
    time="Daytime",                 weather="not raining")
spotted_daydream = Critter(
    name="Spotted Daydream",        flavor="Sour",
    domain="Dream",                 locations=["Golden Isles"],
    habitat="Gateways",             tile_types="water, grass",
    time="Nighttime",               weather="not raining")