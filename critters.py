# Critters (frog food and tradable items) in Mudborne are described here.

# Critters in Mudborne include insects, bugs, a couple bees, an arachnid, and
# the smallest type of jellyfish. All are edible by you, giving you a speed
# boost when you are well fed, and all can be fed to tadpoles to help them
# grow. Each type of critter has a flavor, and different species of frogs will
# require food of different flavors (one or someitmes two) for their tadpoles
# to grow into mature frogs. When a new generation of frogs becomes a
# different species than its immediate ancestor, the ancestor's flavor
# preferences apply, and not the species of mature frog the tadpole will grow
# into. If a species likes two flavors, both must be supplied to the tadpoles.

# Most critters are naturally occurring in a particular habitat such as reeds,
# but jellyfish are unique. There are matriarch jellyfish that can only be
# interacted with by restoring their memory fragments and recovering their
# memories, and these are functionally separate from all other jellyfish.
# There are also medium-sized mother jellies that appear in place of salt
# marsh trees in the Dream domain, which can be broken down into a bunch of
# moon jellies and do not replenish. (To replant these, you need to cut down
# and replant some salt marsh trees in the shallows in the Waking domain. If
# you go into the Dream domain with some of those acorns, they'll show up as
# plantable items to grow into mother jellies, but breaking down a mother
# jelly directly doesn't produce any.) The smallest, the moon jellies, are
# regular consumable critters except for how they are caught. They are also
# naturally occurring and self-replenishing near mother jellies in certain
# climate and weather conditions.

from environment import waking_locations, temperate_waking_locations, dream_locations, temperate_dream_locations, all_locations
from environment import all_domains, all_habitats, all_tile_types, all_weather, all_times

all_flavors = set(("Sweet", "Salty", "Umami", "Bitter", "Sour", "Spicy", "Slimy"))

class Critter:
    """Critter instances keep track of their conditions for spawning and their
    flavors."""
    def __init__(self, name, flavor, domain, locations, habitat, tile_types, time, weather):
        self.name = name
        self.flavor = flavor
        self.domain = domain
        self.locations = locations
        self.habitat = habitat
        self.tile_types = tile_types.split(", ")
        self.weather = weather
        self.time = time
        self._check_valid()
    def _check_valid(self):
        assert self.flavor in all_flavors
        assert self.domain in all_domains
        assert set(self.locations).issubset(all_locations), f"invalid locations {", ".join(self.locations)} for critter {self.name}"
        assert self.habitat in all_habitats
        assert self.tile_types in all_tile_types
        assert self.weather in all_weather
        assert self.time in all_times
