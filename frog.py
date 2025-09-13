# This file keeps track of frogs (the small ones that you can catch, not you
# or the NPCs), including their genetic traits and mechanics for altering them
# with magic mud.

# You and the NPCs are sentient frogs whose traits are not known, if they even
# exist. All catchable frogs, however, have seven traits, abbreviated in the
# acronym ANOURES: Amplitude (size), Nobility (affinity for the dream, as you
# discover late in the game), Odour (stench), Umbrage (attitude, and for
# purposes of machinery, heat), Ribbit (noise, also powering multiple types of
# machines), Edacity (appetite, useful for clearing algae overgrowth), and
# Saturation (ability to absorb water, useful for a couple other machines).
# These traits are all heritable and can be artificially perturbed (heritably)
# by exposing frog spawn to magic mud. They can only be exposed to one batch
# of mud, and the mud may also do nothing. Genetic changes only change the
# species of the frog when the new seven-number code matches another species'
# code. The same applies for variants, which have different appearances and
# slightly different traits, but no difference in flavors preferred. In
# cases where an NPC requires a particular species, any variant will do. For
# gateways, pools, machines, etc., specific trait values are required, but the
# species and variant are not independently relevant. Every species has
# exactly three variants (the base and two others). Two-letter abbreviations
# labeling frogs in the inventory are always the base species, but the
# appearance depends on the variant.

# Every species (but not variant) also has a plushie version that can be
# found or traded for somewhere in the game.

from critters import all_flavors

class GeneticTrait(object):
    """This class keeps track of the value of one individual trait in the
    ANOURES acronym. Seven traits are needed to specify one genetic code.
    This class contains the mechanism for updating the trait for the next
    generation upon administraton of magic mud to frog spawn. The mutation
    occurs in place."""
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self._check_valid()
    def _check_valid(self):
        assert self.name in ("Amplitude", "Nobility", "Odour", "Umbrage", "Ribbit", "Edacity", "Saturation")
        assert self.value >= 1 and self.value <= 7, f"invalid starting trait value {self.value}"
    def adjust(self, operation, scalar):
        assert operation in ("add", "mult", "min", "max", "suppress"), f"invalid operation {operation}"
        match operation:
            case "add":
                self.value += scalar
            case "mult":
                self.value *= scalar
            case "min":
                self.value = 1
            case "max":
                self.value = 7
            case "suppress":
                pass
        self.value = max(1, min(7, self.value))

class GeneticCode(object):
    """A genetic code consists of instances of each of the seven traits. This
    can be considered analogous to one copy of a complete genome."""
    def __init__(self, code):
        assert len(code) == 7, "invalid genetic code: wrong length"
        A, N, O, U, R, E, S = map(int, code)
        self.traits = {
            'A': GeneticTrait('Amplitude',  A),
            'N': GeneticTrait('Nobility',   N),
            'O': GeneticTrait('Odour',      O),
            'U': GeneticTrait('Umbrage',    U),
            'R': GeneticTrait('Ribbit',     R),
            'E': GeneticTrait('Edacity',    E),
            'S': GeneticTrait('Saturation', S),
        }

class Frog(object):
    """The frog base class establishes record keeping for species, including
    its genetic makeup, canonical genetics (as defined in the encyclopedia,
    which describe the genetic makeup that triggers mutation to that species),
    name, abbreviation, variant (defined in a subclass), and flavors preferred
    by the species."""
    def __init__(self,
                 genetics,
                 canonical_genetics=None,
                 species=None,
                 species_abbrev=None,
                 variant=None,
                 variant_abbrev=None,
                 flavors=""):
        self.genetics = GeneticCode(genetics)
        self.canonical_genetics = canonical_genetics or self.genetics
        self.species = species
        self.species_abbrev = self.get_abbreviation(species_abbrev, species)
        self.variant = variant
        self.flavors = flavors.split(", ")
        assert set(self.flavors).issubset(all_flavors), f"invalid favourite flavors {self.flavors} specified"
    def get_abbreviation(self, abbrev, name):
        if abbrev is not None and len(abbrev) > 0: return abbrev
        if name is None: return None
        initials = "".join([word[0].upper() for word in name.split()])
        if len(initials) > 2: initials = initials[:2]
        return initials
    # TODO: define inheritance of offspring

class FrogVariant(Frog):
    """The variant subclass of the Frog base class simplifies instantiation
    of variants of a given species, inheriting all other attributes from the
    base frog supplied as one of the arguments to __init__. Variants also have
    canonical genetics which behave the same as those for base frogs."""
    def __init__(self,
                 genetics,
                 variant_name,
                 base_frog):
        super(self).__init__(genetics,
                             canonical_genetics=base_frog.canonical_genetics,
                             species=base_frog.species,
                             variant=variant_name,
                             flavors=base_frog.flavors)
