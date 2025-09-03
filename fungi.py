# All types of fungi in the game Mudbourne are described here, along with
# their effects on frogs' genetic traits via magic mud.

# Fungi naturally occuring in the Waking domain always have simple additive
# (or subtractive) effects on genetic traits, while Dream domain fungi may
# be multipliers (x-1 or x2) of other fungi's effects, min or max functions,
# or "suppress" (which nullifies any other effect on the same trait in a
# given batch of mud. Fungi are native to, and growable, in only one of the
# two domains. Hybrid fungi created from spore prints may grow in the optimal
# conditions for either of the two contributing species, however, which may
# mean they can be grown in either the Dream or the Waking domain.

from environment import all_domains, all_tile_types, all_temperatures, \
    all_humidities, all_weather

class SingleTraitModifier:
    def __init__(self, trait_code, scalar=0, operation="add"):
        """Trait code refers to the one-letter abbreviation in ANOURES
        for each genetic trait, scalar is the amount by which it is
        indicated to be modified (including +/-, where 0 is a valid
        option), and type is the mathematical function to be applied
        to the trait with the associated factor, from the options add
        (this covers subtraction), multiply (abbreviated mult),
        minimize (abbreviated min), maximize (abbreviated max), and
        suppress. Note that min and max are not affected by modifiers
        that affect other scalar modifiers multiplicatively -- that is,
        a x-1 will not turn a min into a max or vice versa. They are,
        however, overriden by suppress, which will always result in no
        net change to the indicated trait. The combination of multiple
        modifiers by hybridization is handled simply by aggregating
        modifiers (without simplifying e.g. -1 and x-1 to x1), as the
        logic governing modifier combination is carried out only at the
        time of mixing magic mud -- see other classes for this functionality.
        """
        self.code = trait_code
        self.scalar = scalar
        self.operation = operation
        self._check_valid()
    def _check_valid(self):
        assert self.code in "ANOURES" and len(self.code) == 1
        assert type(self.scalar) is int
        assert self.operation in ("add", "mult", "min", "max", "suppress")
    def apply_to_frog(self, gen_code):
        """To be used by subclasses to actually modify frog genetics,
        but useful to have implemented at this level for e.g. checking how
        a specific modification _would_ affect a frog, which is functionality
        enabled in-game."""
        trait = gen_code.traits[self.code]
        trait.adjust(self.operation, self.scalar)

class MultiTraitModifier:
        """A multi-trait modifier aggregates modifications to a given trait
        from multiple sources, either as a hybrid mushroom or as the first
        step in mixing magic mud. This class intentionally does not include
        functionality for condensing modifications of different types into
        a single net modifier, as this may result in incorrect properties of
        a mud in case further modifiers to the same trait are added later."""
    def __init__(self, single_trait_modifiers=[]):
        self.modifiers = {
            'A':[],
            'N':[],
            'O':[],
            'U':[],
            'R':[],
            'E':[],
            'S':[],
        }
        for mod in single_trait_modifiers:
            self.modifiers[mod.code].append(mod)
    def combine(self, other_multi_trait_modifiers):
        for mod in other_multi_trait_modifiers:
            for code in self.modifiers.keys():
                self.modifiers[code] += other_multi_trait_modifiers.modifiers[code]

class Mud:
    def __init__(self, multi_trait_modifiers):
        self.aggregate_modifier = MultiTraitModifier()
        self.aggregate_modifier.combine(multi_trait_modifiers)
        self.mix_mud()
    def mix_mud(self):
        single_trait_modifiers = []
        for collection in self.aggregate_modifier.modifiers.values():
            match len(collection):
                case 0:
                    pass
                case 1:
                    single_trait_modifiers += collection
                case _:
                    additives = []
                    multiplicatives = []
                    min_maxes = []
                    suppress = False
                    for mod in collection:
                        match mod.operation:
                            case "add":
                                additives.append(mod)
                            case "mult":
                                multiplicatives.append(mod)
                            case "min" | "max":
                                min_maxes.append(mod)
                            case "suppress":
                                suppress = True
                    if suppress:
                        continue
                    elif len(min_maxes) > 0:
                        single_trait_modifiers += min_maxes[0]
                        # Caution: undefined behavior if there is both a min and a max
                        # for the same trait. Here we just accept the first one found.
                    elif len(additives) > 0:
                        additive_scalar = sum([mod.scalar for mod in additives])
                        multiplicative_scalar = 1
                        if len(multiplicatives) > 0:
                            for mod in multiplicatives:
                                multiplicative_scalar *= mod.scalar
                        final_additive = multiplicative_scalar * additive_scalar
                        code = additives[0].code
                        single_trait_modifiers.append(
                            SingleTraitModifier(code, final_additive, operation="add"))
        self.mixed_modifier = MultiTraitModifier(single_trait_modifiers)
    def apply_to_frog(self, frog):
        for code in "ANOURES":
            match len(mod := self.mixed_modifier[code]):
                case 0:
                    continue
                case 1:
                    frog_trait = frog.genetics.traits[code]
                    frog_trait.adjust(mod.operation, mod.scalar)
                case _:
                    assert False, "mud not fully mixed at time of applying to frog"

class Mushroom:
    def __init__(self, name, domain, tile_type, temperature, humidity, weather, effects):
        self.name = name
        self.domain = domain
        self.tile_type = tile_type
        self.temperature = temperature
        self.humidity = humidity
        self.weather = weather
        self.parse_effects(effects)
        self.check_valid()
    def check_valid(self):
        assert self.domain in all_domains
        assert self.tile_type in all_tile_types
        assert self.temperature in all_temperatures
        assert self.humidity in all_humidities
        assert self.weather in all_weather
    def parse_effects(self, effects_str):
        self.effects = []
        for eff in effects_str.split(", "):
            type = "mult" if eff[0] == "x" else "add"
            trait_code = eff[-1] # one-letter code in ANOURES
            factor = eff[1:-1] # +/- single digit
            modifier = TraitModifier(trait_code, factor, type=type)
            self.effects.append(modifier)

stout_funnel = Mushroom(
    name="Stout Funnel",        domain="Waking",        tile_type="water",
    temperature="Balmy",        humidity="Drenched",    weather="raining",
    effects="+1A")
flat_stinkhorn = Mushroom(
    name="Flat Stinkhorn",      domain="Waking",        tile_type="grass",
    temperature="Balmy",        humidity="Normal",      weather="not raining",
    effects="+1N, +1O")
bothersome_fungus = Mushroom(
    name="Bothersome Fungus",   domain="Waking",        tile_type="mud",
    temperature="Warm",         humidity="Damp",        weather="not raining",
    effects="+1U, +1E")
withering_rot = Mushroom(
    name="Withering Rot",       domain="Waking",        tile_type="mud",
    temperature="Chilly",       humidity="Damp",        weather="not raining",
    effects="-1A, -1S")
shrinking_cap = Mushroom(
    name="Shrinking Cap",       domain="Waking",        tile_type="stagnant water",
    temperature="Balmy",        humidity="Damp",        weather="not raining",
    effects="-1A, -1O")
pickled_bonnet = Mushroom(
    name="Pickled Bonnet",      domain="Waking",        tile_type="inside",
    temperature="Mild",         humidity="Parched",     weather="not raining",
    effects="+1A, +1S")
raucous_conecap = Mushroom(
    name="Raucous Conecap",     domain="Waking",        tile_type="water",
    temperature="Balmy",        humidity="Waterlogged", weather="raining",
    effects="+1O, +1R")
grubby_parachute = Mushroom(
    name="Grubby Parachute",    domain="Waking",        tile_type="mud",
    temperature="Warm",         humidity="Wet",         weather="not raining",
    effects="-1N")
frosty_jack = Mushroom(
    name="Frosty Jack",         domain="Waking",        tile_type="water",
    temperature="Hot",          humidity="Wet",         weather="not raining",
    effects="-1U, +1E")
filling_oyster = Mushroom(
    name="Filling Oyster",      domain="Waking",        tile_type="grass",
    temperature="Frozen",       humidity="Normal",      weather="raining",
    effects="-1E")
bulbous_muffler = Mushroom(
    name="Bulbous Muffler",     domain="Waking",        tile_type="mud",
    temperature="Cold",         humidity="Damp",        weather="snowing",
    effects="-1R")
squat_amplifier = Mushroom(
    name="Squat Amplifier",     domain="Dream",         tile_type="mud",
    temperature="Balmy",        humidity="Wet",         weather="raining",
    effects="x2N, x2U")
towering_expander = Mushroom(
    name="Towering Expander",   domain="Dream",         tile_type="grass",
    temperature="Warm",         humidity="Normal",      weather="not raining",
    effects="x2N")
fools_mirror = Mushroom(
    name="Fool's Mirror",       domain="Dream",         tile_type="water",
    temperature="Chilly",       humidity="Wet",         weather="not raining",
    effects="x-1A, x-1N")
bloating_mould = Mushroom(
    name="Bloating Mould",      domain="Dream",         tile_type="inside",
    temperature="Mild",         humidity="Dry",         weather="not raining",
    effects="x0O, x2S")
stinking_bolete = Mushroom(
    name="Stinking Bolete",     domain="Dream",         tile_type="stagnant water",
    temperature="Warm",         humidity="Damp",        weather="not raining",
    effects="x0N, x2O")
pointed_deceiver = Mushroom(
    name="Pointed Deceiver",    domain="Dream",         tile_type="inside",
    temperature="Mild",         humidity="Normal",      weather="not raining",
    effects="x0A, -1S")
chattering_bell = Mushroom(
    name="Chattering Bell",     domain="Dream",         tile_type="grass",
    temperature="Chilly",       humidity="Damp",        weather="raining",
    effects="x-1O, x2R")
false_suppressor = Mushroom(
    name="False Suppressor",    domain="Dream",         tile_type="inside",
    temperature="Chilly",       humidity="Dry",         weather="not raining",
    effects="x0U, x2E")
velvet_inverter = Mushroom(
    name="Velvet Inverter",     domain="Dream",         tile_type="grass",
    temperature="Hot",          humidity="Normal",      weather="not raining",
    effects="x-1R, x-1E")
rude_awakening = Mushroom(
    name="Rude Awakening",      domain="Dream",         tile_type="grass",
    temperature="Hot",          humidity="Damp",        weather="raining",
    effects="mN")
torrential_prune = Mushroom(
    name="Torrential Prune",    domain="Dream",         tile_type="mud",
    temperature="Mild",         humidity="Normal",      weather="not raining",
    effects="mA, MS")
booming_mane = Mushroom(
    name="Booming Mane",        domain="Dream",         tile_type="water",
    temperature="Mild",         humidity="Damp",        weather="not raining",
    effects="MO, MR")
chill_pill = Mushroom(
    name="Chill Pill",          domain="Dream",         tile_type="inside",
    temperature="Chilly",       humidity="Normal",      weather="not raining",
    effects="mU")
