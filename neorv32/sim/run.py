#!/usr/bin/env python3

from pathlib import Path
from vunit import VUnit, VUnitCLI
from subprocess import call

#add replace script
import sys
sys.path.insert(0, "../../")
from replace import replace_sonarqube_coverage


def post_run(results):
    results.merge_coverage(file_name="coverage_data")
    call(["gcovr", "-v","-f",".","--sonarqube", "coverage.xml"])
    replace_sonarqube_coverage()

cli = VUnitCLI()
cli.parser.add_argument(
    "--ci-mode",
    action="store_true",
    default=False,
    help="Enable special settings used by the CI",
)
args = cli.parse_args()

PRJ = VUnit.from_args(args=args)

ROOT = Path(__file__).parent

NEORV32 = PRJ.add_library("neorv32")
NEORV32.add_source_files([
    ROOT / "*.vhd",
    ROOT / ".." / "rtl" / "**" / "*.vhd",
    # In VUnit <=v4.5.0, the glob search is not recursive,
    # hence subdir 'mem' is not picked by the previous pattern
    ROOT / ".." / "rtl" / "core" / "mem" / "*.vhd"
])


NEORV32.set_compile_option("enable_coverage", True)
NEORV32.test_bench("neorv32_tb").set_generic("ci_mode", args.ci_mode)
NEORV32.set_sim_option("enable_coverage", True)


PRJ.add_com()
PRJ.add_verification_components()
PRJ.add_osvvm()

PRJ.set_sim_option("enable_coverage", True)
PRJ.set_sim_option("disable_ieee_warnings", True)
PRJ.set_sim_option("ghdl.sim_flags", ["--max-stack-alloc=256"])

PRJ.main(post_run=post_run)
