import argparse
import re

from dice_rolling import __version__


class ParsingResult:
    def __init__(self):
        self.n_dice = 1
        self.n_sides = 0
        self.addition = 0
        self.keep = 0
        self.seed = None

    def __setattr__(self, key, value):
        if value or value == 0:
            # Set the int value to the attribute if the value is not None.
            super().__setattr__(key, int(value))
        elif key in ['seed']:
            # If the key is in the list of allowed keys to be set as None, allow.
            super().__setattr__(key, None)


def request_type(arg):
    regex = re.compile(ArgumentParser.REQUEST_REGEX)
    if not regex.match(arg):
        raise argparse.ArgumentParser
    return arg


class ArgumentParser(argparse.ArgumentParser):

    REQUEST_REGEX = r'^(\d*)d(\d+)(?:\+(\d+))?(k(h|l)\d+)?$'

    def __init__(self):
        super().__init__(description="Dice roller.", add_help=True)

        self.add_argument('request', type=request_type)
        self.add_argument('-s', '--seed', dest='seed', default=None)
        self.add_argument('-v', '--version', action='version', version=__version__)

    def parse(self):
        args = self.parse_args()
        result = ParsingResult()

        regex_result = re.search(self.REQUEST_REGEX, args.request, re.IGNORECASE)

        result.n_dice = regex_result.group(1)
        result.n_sides = regex_result.group(2)
        result.addition = regex_result.group(3)

        keep = regex_result.group(4)
        if keep:
            result.keep = int(keep[2:]) * (1 if keep[1] == 'h' else -1)

        if result.n_sides == 0:
            import sys
            print("A dice must have at least one side.", file=sys.stderr)
            exit(3)

        if args.seed:
            result.seed = int(args.seed)

        return result
