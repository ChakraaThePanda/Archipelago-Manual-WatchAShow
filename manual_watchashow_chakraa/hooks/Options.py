# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class NumberofEpisodes(Range):
    """Select the amount of episodes you want to watch"""
    display_name = "Episodes to beat the game"
    range_start = 1
    range_end = 100
    default = 10

class LocationsPerEpisode(Range):
    """Select the amount of locations each episode have"""
    display_name = "Locations per episode"
    range_start = 1
    range_end = 4
    default = 4

class EpisodesOrder(Choice):
    """Sequential will force the logic to watch the episodes in order, Chaotic will allow the episodes to be watched in any order"""
    display_name = """Sequential or Chaotic"""
    option_chaotic = 0
    option_sequential = 1
    default = 1

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["number_of_episodes"] = NumberofEpisodes
    options["locations_per_episode"] = LocationsPerEpisode
    options["episodes_order"] = EpisodesOrder
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options