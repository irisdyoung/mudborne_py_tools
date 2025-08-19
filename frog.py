from critters import all_flavors

class GeneticTrait(object):
    def __init__(self, name, value, modifier=None):
        self.name = name
        assert value >= 1 and value <= 7
        self.value = value
        self.modifier = modifier
    def adjust(self, increment, modifier=None):
        self.value = max(1, min(7, self.value + increment))
        self.modifier = modifier

class GeneticCode(object):
    def __init__(self, code):
        assert len(code) == 7, "invalid genetic code: wrong length"
        A, N, O, U, R, E, S = map(int, code)
        self.amplitude  = GeneticTrait('Amplitude',  A)
        self.nobility   = GeneticTrait('Nobility',   N)
        self.odour      = GeneticTrait('Odour',      O)
        self.umbrage    = GeneticTrait('Umbrage',    U)
        self.ribbit     = GeneticTrait('Ribbit',     R)
        self.edacity    = GeneticTrait('Edacity',    E)
        self.saturation = GeneticTrait('Saturation', S)

class Frog(object):
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
        self.variant_abbrev = self.get_abbreviation(variant_abbrev, variant)
        self.flavors = flavors.split(", ")
        assert set(self.flavors).issubset(all_flavors), "invalid favourite flavors specified"
    def get_abbreviation(self, abbrev, name):
        if abbrev is not None and len(abbrev) > 0: return abbrev
        if name is None: return None
        initials = "".join([word[0].upper() for word in name.split()])
        if len(initials) > 2: initials = initials[:2]
        return initials
    # TODO: define inheritance of offspring

class FrogVariant(Frog):
    def __init__(self,
                 genetics,
                 base_frog,
                 variant_name):
        super(self).__init__(genetics,
                             canonical_genetics=base_frog.canonical_genetics,
                             species=base_frog.species,
                             variant=variant_name,
                             flavors=base_frog.flavors)
    # TODO: ensure offspring of variants are renamed back to the base frog name and abbrev

common_green = Frog(
    genetics="4444444",
    species="Common Green",
    flavors="Salty")

pungent_green = FrogVariant(
    genetics="4664444",
    base_frog=common_green,
    variant_name="Pungent Green")

vast_mudlurker = Frog(
    genetics="7444444",
    species="Vast Mudlurker",
    flavors="Sweet")

long_legged_dazzler = Frog(
    genetics="4774444",
    species="Long-Legged Dazzler",
    flavors="Bitter")

weeny_sponge = Frog(
    genetics="1444441",
    species="Weeny Sponge",
    flavors="Bitter")

dozy_dreamer = Frog(
    genetics="5555555",
    species="Dozy Dreamer",
    flavors="Slimy")

pocket_snoozer = Frog(
    genetics="1555555",
    species="Pocket Snoozer",
    flavors="Umami")


# target: 4774441
# target: 7244444
