from critters import all_flavors

class GeneticTrait(object):
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
    def __init__(self,
                 genetics,
                 variant_name,
                 base_frog):
        super(self).__init__(genetics,
                             canonical_genetics=base_frog.canonical_genetics,
                             species=base_frog.species,
                             variant=variant_name,
                             flavors=base_frog.flavors)

common_green = Frog(
    genetics="4444444",
    species="Common Green",
    flavors="Salty")
pungent_green = FrogVariant(
    genetics="4664444",
    variant_name="Pungent Green",
    base_frog=common_green)
greater_green = FrogVariant(
    genetics="6454744",
    variant_name="Greater Green",
    base_frog=common_green)

vast_mudlurker = Frog(
    genetics="7444444",
    species="Vast Mudlurker",
    flavors="Sweet")
poor_mudlurker = FrogVariant(
    genetics="7344444",
    variant_name="Poor Mudlurker",
    base_frog=vast_mudlurker)
royal_mudlurker = FrogVariant(
    genetics="7554444",
    variant_name="Royal Mudlurker",
    base_frog=vast_mudlurker)

long_legged_dazzler = Frog(
    genetics="4774444",
    species="Long-Legged Dazzler",
    flavors="Bitter")
longer_legged_dazzler = FrogVariant(
    genetics="5774444",
    variant_name="Longer-Legged Dazzler",
    base_frog=long_legged_dazzler)
long_winded_dazzler = FrogVariant(
    genetics="4774441", # S=1,2,3
    variant_name="Long-Winded Dazzler",
    base_frog=long_legged_dazzler)

furious_lurker = Frog(
    genetics="4447474",
    species="Furious Lurker",
    flavors="Salty, Sweet")
obvious_lurker = Frog(
    genetics="4447574",
    variant_name="Obvious Lurker",
    base_frog=furious_lurker)
rancid_lurker = FrogVariant(
    genetics="4257474",
    variant_name="Rancid Lurker",
    base_frog=furious_lurker)

weeny_sponge = Frog(
    genetics="1444441",
    species="Weeny Sponge",
    flavors="Bitter")
hungry_sponge = FrogVariant(
    genetics="1444471",
    variant_name="Hungry Sponge",
    base_frog=weeny_sponge)
sleeping_sponge = FrogVariant(
    genetics="1555551",
    variant_name="Sleeping Sponge",
    base_frog=weeny_sponge)

dozy_dreamer = Frog(
    genetics="5555555",
    species="Dozy Dreamer",
    flavors="Slimy")
burly_dreamer = FrogVariant(
    genetics="7555554",
    variant_name="Burly Dreamer",
    base_frog=dozy_dreamer)
polished_dreamer = FrogVariant(
    genetics="5445555",
    variant_name="Polished Dreamer",
    base_frog=dozy_dreamer)

grubby_rascal = Frog(
    genetics="5175555",
    species="Grubby Rascal",
    flavors="Spicy, Sour")
starving_rascal = FrogVariant(
    genetics="5175575",
    variant_name="Starving Rascal",
    base_frog=grubby_rascal)
common_rascal = FrogVariant(
    genetics="4174444",
    variant_name="Common Rascal",
    base_frog=grubby_rascal)

pocket_snoozer = Frog(
    genetics="1555555",
    species="Pocket Snoozer",
    flavors="Umami")
silent_snoozer = FrogVariant(
    genetics="1554455",
    variant_name="Silent Snoozer",
    base_frog=pocket_snoozer)
damp_snoozer = FrogVariant(
    genetics="155557",
    variant_name="Damp Snoozer",
    base_frog=pocket_snoozer)

pristine_peacheyes = Frog(
    genetics="1414444",
    species="Pristine Peach-eyes",
    flavors="Sour")
preening_peacheyes = FrogVariant(
    genetics="1614444",
    variant_name="Preening Peach-eyes",
    base_frog=pristine_peacheyes)
pristine_redeyes = FrogVariant(
    genetics="1415544",
    variant_name="Pristine Red-eyes",
    base_frog=pristine_peacheyes)

spotless_napper = Frog(
    genetics="5515555",
    species="Spotless Napper",
    flavors="Sweet, Spicy")
slippery_napper = FrogVariant(
    genetics="1515555",
    variant_name="Slippery Napper",
    base_frog=spotless_napper)
spotless_nipper = FrogVariant(
    genetics="4414444",
    variant_name="Spotless Nipper",
    base_frog=spotless_napper)

dripping_giant = Frog(
    genetics="7444447",
    species="Dripping Giant",
    flavors="Salty")
dripping_sleeper = Frog(
    genetics="7555557",
    variant_name="Dripping Sleeper",
    base_frog=dripping_giant)
contented_giant = FrogVariant(
    genetics="7444437",
    variant_name="Contented Giant",
    base_frog=dripping_giant)

foul_screamer = Frog(
    genetics="4474744",
    species="Foul Screamer",
    flavors="Sour")
hazy_screamer = FrogVariant(
    genetics="4274744",
    variant_name="Hazy Screamer",
    base_frog=foul_screamer)
flooded_screamer = FrogVariant(
    genetics="4474746",
    variant_name="Flooded Screamer",
    base_frog=foul_screamer)

drowsy_deluge = Frog(
    genetics="5155557",
    species="Drowsy Deluge",
    flavors="Sweet, Slimy")
noisy_deluge = FrogVariant(
    genetics="5155757",
    variant_name="Noisy Deluge",
    base_frog=drowsy_deluge)
trivial_deluge = FrogVariant(
    genetics="4144447",
    variant_name="Trivial Deluge",
    base_frog=drowsy_deluge)

blackeyed_bawler = Frog(
    genetics="7444744",
    species="Black-eyed Bawler",
    flavors="Sweet")
shuteyed_bawler = FrogVariant(
    genetics="7544744",
    variant_name="Shut-eyed Bawler",
    base_frog=blackeyed_bawler)
funky_brawler = FrogVariant(
    genetics="7555764",
    variant_name="Funky Brawler",
    base_frog=blackeyed_bawler)

redbacked_fury = Frog(
    genetics="4447747",
    species="Red-Backed Fury",
    flavors="Spicy")
smallbacked_fury = FrogVariant(
    genetics="3437747",
    variant_name="Small-Backed Fury",
    base_frog=redbacked_fury)
redbacked_feaster = Frog(
    genetics="4477777",
    variant_name="Red-Backed Feaster",
    base_frog=redbacked_fury)

wilted_skulker = Frog(
    genetics="5511551",
    species="Wilted Skulker",
    flavors="Salty, Slimy")
wilted_sulker = FrogVariant(
    genetics="5551451",
    variant_name="Wilted Sulker",
    base_frog=wilted_skulker)
banal_skulker = Frog(
    genetics="4411441",
    variant_name="Banal Skulker",
    base_frog=wilted_skulker)

frosty_hollow = Frog(
    genetics="4441474",
    species="Frosty Hollow",
    flavors="Umami")
damp_hollow = Frog(
    genetics="4441477",
    variant_name="Damp Hollow",
    base_frog=frosty_hollow)
frosty_hollerer = Frog(
    genetics="4441674",
    variant_name="Frosty Hollerer",
    base_frog=frosty_hollow)

reeking_sneaker = Frog(
    genetics="4774144",
    species="Reeking Sneaker",
    flavors="Bitter")
raging_sneaker = FrogVariant(
    genetics="4777174",
    variant_name="Raging Sneaker",
    base_frog=reeking_sneaker)
fleeting_sneaker = FrogVariant(
    genetics="5775155",
    variant_name="Fleeting Sneaker",
    base_frog=reeking_sneaker)

dinky_furnace = Frog(
    genetics="1557155",
    species="Dinky Furnace",
    flavors="Bitter, Slimy")
stinky_furnace = FrogVariant(
    genetics="1577155",
    variant_name="Stinky Furnace",
    base_frog=dinky_furnace)
dusty_furnace = Frog(
    genetics="1357153",
    variant_name="Dusty Furnace",
    base_frog=dinky_furnace)

peaceful_spadefoot = Frog(
    genetics="5551115",
    species="Peaceful Spadefoot",
    flavors="Sour, Sweet")
subdued_spadefoot = FrogVariant(
    genetics="3331115",
    variant_name="Subdued Spadefoot",
    base_frog=peaceful_spadefoot)
plain_spadefoot = FrogVariant(
    genetics="4441114",
    variant_name="Plain Spadefoot",
    base_frog=peaceful_spadefoot)

bloated_thunder = Frog(
    genetics="7444774",
    species="Bloated Thunder",
    flavors="Spicy")
storming_thunder = FrogVariant(
    genetics="7465774",
    variant_name="Storming Thunder",
    base_frog=bloated_thunder)
sleepless_night = Frog(
    genetics="7555775",
    variant_name="Sleepless Night",
    base_frog=bloated_thunder)

soggy_marcher = Frog(
    genetics="1234567",
    species="Soggy Marcher",
    flavors="Salty")
expanded_marcher = FrogVariant(
    genetics="7234567",
    variant_name="Expanded Marcher",
    base_frog=soggy_marcher)
arid_marcher = FrogVariant(
    genetics="1234561",
    variant_name="Arid Marcher",
    base_frog=soggy_marcher)

waning_bullfrog = Frog(
    genetics="7654321",
    species="Waning Bullfrog",
    flavors="Salty")
waxing_bullfrog = FrogVariant(
    genetics="1654327",
    variant_name="Waxing Bullfrog",
    base_frog=waning_bullfrog)
drenched_bullfrog = FrogVariant(
    genetics="7654327",
    variant_name="Drenched Bullfrog",
    base_frog=waning_bullfrog)

stubby_scamp = Frog(
    genetics="1111111",
    species="Stubby Scamp",
    flavors="Salty")
bothered_scamp = FrogVariant(
    genetics="1112111",
    variant_name="Bothered Scamp",
    base_frog=stubby_scamp)
slimy_scamp = FrogVariant(
    genetics="1111112",
    variant_name="Slimy Scamp",
    base_frog=stubby_scamp)

towering_prince = Frog(
    genetics="7777777",
    species="Towering Prince",
    flavors="Salty")
lukewarm_prince = FrogVariant(
    genetics="7676767",
    variant_name="Lukewarm Prince",
    base_frog=towering_prince)
serene_prince = FrogVariant(
    genetics="7771777",
    variant_name="Serene Prince",
    base_frog=towering_prince)

secondrate_prowler = Frog(
    genetics="2222222",
    species="Second-rate Prowler",
    flavors="Salty")
shameless_prowler = Frog(
    genetics="2121212",
    variant_name="Shameless Prowler",
    base_frog=secondrate_prowler)
sizzling_prowler = FrogVariant(
    genetics="2227222",
    variant_name="Sizzling Prowler",
    base_frog=secondrate_prowler)

imperfect_blabber = Frog(
    genetics="6666666",
    species="Imperfect Blabber",
    flavors="Salty")
perfect_blabber = FrogVariant(
    genetics="6766666",
    variant_name="Perfect Blabber",
    base_frog=imperfect_blabber)
incessant_blabber = FrogVariant(
    genetics="6666766",
    variant_name="Incessant Blabber",
    base_frog=imperfect_blabber)

lowgrade_croaker = Frog(
    genetics="3333333",
    species="Low-Grade Croaker",
    flavors="Salty")
lowlevel_croaker = FrogVariant(
    genetics="2333332",
    variant_name="Low-Level Croaker",
    base_frog=lowgrade_croaker)
worthless_croaker = FrogVariant(
    genetics="3232323",
    variant_name="Worthless Croaker",
    base_frog=lowgrade_croaker)

sublime_empyrean = Frog(
    genetics="7177777",
    species="Sublime Empyrean",
    flavors="Salty")
sleeping_empyrean = FrogVariant(
    genetics="7177777", # no change; mature tadpoles in Dream
    variant_name="Sleeping Empyrean",
    base_frog=sublime_empyrean)
true_empyrean = FrogVariant(
    genetics="7177777", # no change; breed in one step from Prince
    variant_name="True Empyrean",
    base_frog=sublime_empyrean)
