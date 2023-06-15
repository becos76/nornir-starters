"""
Simple nornir get facts script using napalm getters and print the result asynchronously
as soon as each host task finishes

Author: becos76
License: MIT
"""
from nornir import InitNornir
from nornir_utils.plugins.processors import PrintResult
from nornir_napalm.plugins.tasks import napalm_get

nr = InitNornir(config_file='inventory/config.yaml')
nr = nr.with_processors([PrintResult()])

nr.run(task=napalm_get, getters=['facts'])
