<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "Qingqing Cao, https://awk.ai/, Twitter@sysnlp"

import argparse
import numpy as np

from experiment_impact_tracker.utils import gather_additional_info
from experiment_impact_tracker.utils import load_initial_info
from pathlib import Path


def one_energy(log_dir):
    sys_data = load_initial_info(log_dir)
    eff_data = gather_additional_info(sys_data, log_dir)
    return eff_data['total_power']


def main(args):
    log_parent_path = Path(args.log_parent_dir)
    energy = [one_energy(x) for x in log_parent_path.iterdir() if x.is_dir()]
    print(f"found {len(energy)} logs")
    avg = np.mean(energy)
    std = np.std(energy)
    print(f"{log_parent_path} energy")
    print(f"avg (kwh), std (kwh), avg (J), std (J), std ratio (%)")
    print(f"{avg:.5f}, {std:.5f}, {avg * 3.6e6:.1f}, "
          f"{std * 3.6e6:.1f}, {std * 100 / avg:.1f}")
    if args.num_examples:
        per_ex_avg = avg / args.num_examples
        per_ex_std = std / args.num_examples
        print(f"{log_parent_path} per example energy")
        print(f"avg (J), std (J), std ratio (%)")
        print(f"{per_ex_avg * 3.6e6:.1f}, {per_ex_std * 3.6e6:.1f}, "
              f"{per_ex_std * 100 / per_ex_avg:.1f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("log_parent_dir", type=str,
                        help="parent dir of the dir containing log files "
                             "from experiment_imapct_tracker")
    parser.add_argument("-n", "--num_examples", default=0, type=int,
                        help="number of examples to get "
                             "average energy per example ",
                        )
    main(parser.parse_args())
=======
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
>>>>>>> add energy summary script
