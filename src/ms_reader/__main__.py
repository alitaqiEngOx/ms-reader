import argparse
import logging
import os
import time

from operations import read


logging.getLogger().setLevel(logging.INFO)

def assert_errors(args: argparse.Namespace) -> None:
    """
    Ensures the MeasurementSet directory exists.
    """
    if not os.path.exists(os.path.abspath(args.ms_dir)):
        raise FileNotFoundError(
            f"{args.ms_dir} does not exist"
        )

def main() -> None:
    """
    Entry to the pipeline.
    """
    args = parse_args()
    read.ms(args.ms_dir)

def parse_args() -> argparse.Namespace:
    """
    Parser for terminal arguments.
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