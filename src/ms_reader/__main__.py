import argparse
import logging
import os
import time


logging.getLogger().setLevel(logging.INFO)


def assert_errors(args: argparse.Namespace) -> None:
    """
    """
    if not os.path.exists(os.path.abspath(args.ms_dir)):
        raise FileNotFoundError(
            f"{args.ms_dir} does not exist"
        )

def main() -> None:
    """
    """
    args = parse_args()

def parse_args() -> argparse.Namespace:
    """
    """
    parser = argparse.ArgumentParser(
        description="MeasurementSet reader for radio astronomy",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "ms_dir",
        type=str,
        help="input MeasurementSet directory"
    )
    return parser.parse_args()


if __name__ == "__main__":
    start_time = time.time()
    main()
    logging.info(f"Full time = {time.time() - start_time} s")