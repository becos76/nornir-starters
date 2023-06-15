"""
Simple nornir get facts script using napalm getters

Author: becos76
License: MIT
"""
from nornir import InitNornir
from nornir_utils.plugins.functions import print_result
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file='inventory/config.yaml')

napalm_results = nr.run(task=napalm_get, getters=['facts'])

print_result(napalm_results)
