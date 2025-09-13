# Flowers encountered in the game are described here. Species are moved to
# flora_collection.py.

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
