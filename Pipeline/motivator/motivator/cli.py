import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--extreme", action="store_true")
    args = parser.parse_args()

    if args.extreme:
        print("NO EXCUSES. KEEP GOING.")
    else:
        print("Keep going. You’ve got this.")


if __name__ == "__main__":
    main()