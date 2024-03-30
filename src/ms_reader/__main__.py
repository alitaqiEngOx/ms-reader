import argparse
import logging
import time

logging.getLogger().setLevel(logging.INFO)


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


def main() -> None:
    """
    """
    args = parse_args()
    return

if __name__ == "__main__":
    start_time = time.time()
    main()
    logging.info(f"Full time = {time.time() - start_time} s")