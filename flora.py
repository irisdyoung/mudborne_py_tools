# All types of flowers encountered in the game are catalogued here.

# Flowers can be found in either the Waking or the Dream domain (never both),
# on only one tile type (water, deep water, or grass), and are native to one or
# more locations, although once found, they can be grown on the appropriate
# tile type in any location, in their native domain. They do not automatically
# replenish and must be replanted. Flowers can be traded with NPCs for certain
# items. Seeds can only be used to replant flowers.

from environment import waking_locations, temperate_waking_locations, temperate_waking_northern, dream_locations, temperate_dream_locations, all_locations
from environment import all_domains, all_habitats, all_tile_types

class Flower:
    """The flower's native growing conditions are logged as well as any
    habitat the flower creates for critters."""
    def __init__(self, name, domain, locations, tile_type, habitat_created=None):
        self.name = name
        self.domain = domain
        self.locations = locations
        self.tile_type = tile_type
        self.habitat_created = habitat_created
        self._check_valid()
    def _check_valid(self):
        assert self.domain in all_domains
        assert set(self.locations).issubset(all_locations)
        assert self.tile_type in all_tile_types
        if self.habitat_created is not None:
            assert self.habitat_created in all_habitats

red_lily = Flower(          name="Red Lily",
    domain="Waking",        locations=temperate_waking_locations,
    tile_type="water",      habitat_created="Red Lilies")
pink_lily = Flower(         name="Pink Lily",
    domain="Waking",        locations=["Central Junction"],
    tile_type="water")
red_lotus = Flower(         name="Red Lotus",
    domain="Waking",        locations=["Kindergarten"],
    tile_type="water")
white_lotus = Flower(       name="White Lotus",
    domain="Waking",        locations=temperate_waking_locations,
    tile_type="deep water")
azure_heart = Flower(       name="Azure Heart",
    domain="Waking",        locations=["Residential District"],
    tile_type="water")
frosty_crown = Flower(      name="Frosty Crown",
    domain="Waking",        locations=["Climate Control"],
    tile_type="water")
croakfoot = Flower(         name="Croakfoot",
    domain="Waking",        locations=["Climate Control"],
    tile_type="deep water")
toadflux = Flower(          name="Toadflux",
    domain="Waking",        locations=["Central Junction"],
    tile_type="grass")
dream_orchid = Flower(      name="Dream Orchid",
    domain="Dream",         locations=dream_locations,
    tile_type="water",      habitat_created="Dream Orchids")
broken_crown = Flower(      name="Broken Crown",
    domain="Dreaming",      locations=["Frozen Dreams"],
    tile_type="water")
hoppyhock = Flower(         name="Hoppyhock",
    domain="Dream",         locations=["Residential District"],
    tile_type="water")
cherry_bomb = Flower(       name="Cherry Bomb",
    domain="Dream",         locations=["Future Farms"],
    tile_type="water")
motherwart = Flower(        name="Motherwart",
    domain="Dream",         locations=["Memory Works"],
    tile_type="water")
lost_lotus = Flower(        name="Lost Lotus",
    domain="Dream",         locations=dream_locations,
    tile_type="deep water")
