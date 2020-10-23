""" """

import argparse
import json

from experiment_impact_tracker.utils import gather_additional_info, load_initial_info


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--log_dir", type=str, help="Directory containing log files from experiment_imapct_tracker")
    args = parser.parse_args()

    sys_data = load_initial_info(args.log_dir)
    eff_data = gather_additional_info(sys_data, args.log_dir)
    for stat in ["cpu_info", "gpu_info", "experiment_impact_tracker_version", "region", "region_carbon_intensity_estimate"]:
        print(f"{stat}: {sys_data[stat]}")
    print(f"Experiment energy usage: {eff_data['total_power']}")


if __name__ == "__main__":
    main()
