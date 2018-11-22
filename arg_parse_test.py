import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, help="the base")
    parser.add_argument("--y", type=int, help="the exponent")
    args = parser.parse_args()
    print(args.x**args.y)


if __name__ == "__main__":
    main()
