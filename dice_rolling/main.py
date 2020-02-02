from dice_rolling import RollBuilder
from dice_rolling.utils.argument_parser import ArgumentParser


def main():
    args = ArgumentParser().parse()

    b = RollBuilder(args.seed)
    b.set_amount_of_dice(args.n_dice)
    b.set_number_of_sides(args.n_sides)
    b.addition_to_roll(args.addition)
    b.keep_n(args.keep)
    b.build()

    print(b.get_result())


if __name__ == "__main__":
    main()
