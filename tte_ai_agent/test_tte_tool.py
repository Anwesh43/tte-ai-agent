from tools.tte_tools import playAnimation, getEffects, addEffect, clearScreen 
import time 


text1 = """
root@cybernode:~$ ./initialize.sh

[00:00:01] Initializing CyberNode Terminal v4.8.2
[00:00:02] Loading encrypted configuration files...
[00:00:03] Establishing secure communication channel...
[00:00:04] Checking system integrity...
[00:00:05] System integrity verified.

root@cybernode:~$ systemctl status network

● network.service - Network Management Service
   Loaded: loaded (/etc/systemd/system/network.service)
   Active: active (running)
   Status: "All network interfaces operational"

[INFO] Scanning available network interfaces...
[INFO] Interface eth0: UP
[INFO] Interface wlan0: UP
[INFO] Interface tun0: CONNECTED

root@cybernode:~$ ./security_scan --deep

[SCAN] Initializing network discovery...
[SCAN] Discovering active hosts...
[SCAN] Analyzing open communication ports...
[SCAN] Inspecting firewall configurations...
[SCAN] Validating encryption protocols...

Progress: [####----------------] 20%
Progress: [########------------] 40%
Progress: [############--------] 60%
Progress: [################----] 80%
Progress: [####################] 100%

[RESULT] 128 network endpoints analyzed.
[RESULT] 24 encrypted connections identified.
[RESULT] 0 critical vulnerabilities detected.
[RESULT] Security assessment completed.

root@cybernode:~$ ./decrypt_archive.sh

[CRYPTO] Loading AES-256 encryption module...
[CRYPTO] Verifying authentication token...
[CRYPTO] Deriving secure encryption keys...
[CRYPTO] Processing encrypted data blocks...

Decrypting block 001/005... SUCCESS
Decrypting block 002/005... SUCCESS
Decrypting block 003/005... SUCCESS
Decrypting block 004/005... SUCCESS
Decrypting block 005/005... SUCCESS

[CRYPTO] Archive successfully decrypted.
[CRYPTO] Integrity verification: PASSED

root@cybernode:~$ cat mission_status.log

========================================
        CYBERNODE CONTROL CENTER
========================================

SYSTEM STATUS     : ONLINE
NETWORK STATUS    : SECURE
ENCRYPTION        : AES-256
FIREWALL          : ACTIVE
THREAT LEVEL      : LOW
MISSION STATUS    : COMPLETED

========================================

root@cybernode:~$ echo "ACCESS GRANTED"

ACCESS GRANTED

root@cybernode:~$ _
"""

text2 = """
ai@neuralcore:~$ python3 neural_engine.py --initialize

==================================================
             NEURAL CORE AI SYSTEM
                  VERSION 9.2
==================================================

[BOOT] Initializing artificial intelligence engine...
[BOOT] Detecting available compute resources...
[BOOT] Loading neural network architecture...
[BOOT] Allocating accelerator memory...
[BOOT] Initializing inference runtime...

[GPU] Accelerator 0 detected.
[GPU] Accelerator 1 detected.
[GPU] Accelerator 2 detected.
[GPU] Accelerator 3 detected.

[MEMORY] Allocating 64 GB shared memory...
[MEMORY] Allocation completed.

[MODEL] Loading transformer architecture...
[MODEL] Reading model configuration...
[MODEL] Initializing attention mechanisms...
[MODEL] Preparing positional embeddings...
[MODEL] Loading token embeddings...
[MODEL] Restoring model weights...

Loading model weights:
[##----------------------------] 7%
[#####-------------------------] 17%
[#########---------------------] 30%
[############------------------] 40%
[################--------------] 53%
[####################----------] 67%
[########################------] 80%
[############################--] 93%
[##############################] 100%

[MODEL] Model successfully loaded.
[MODEL] Running inference diagnostics...

[TEST] Tokenizer initialization........ PASS
[TEST] Attention mechanism............. PASS
[TEST] KV cache allocation............. PASS
[TEST] Context window validation....... PASS
[TEST] Tensor parallelism.............. PASS
[TEST] Memory optimization............. PASS

ai@neuralcore:~$ python3 benchmark.py

[BENCHMARK] Starting performance evaluation...

Input tokens: 8192
Output tokens: 2048
Batch size: 16
Precision: FP16

[BENCHMARK] Performing warmup iterations...
[BENCHMARK] Running inference tests...
[BENCHMARK] Measuring token throughput...
[BENCHMARK] Evaluating latency distribution...

==========================================
          INFERENCE BENCHMARK
==========================================

Average latency      : 24.8 ms
Token throughput     : 4096 tokens/sec
GPU utilization      : 92%
Memory utilization   : 76%
Model status         : OPTIMAL

==========================================

ai@neuralcore:~$ python3 agent.py --interactive

[AGENT] Initializing reasoning engine...
[AGENT] Registering available tools...
[AGENT] Connecting vector database...
[AGENT] Initializing retrieval pipeline...
[AGENT] Loading conversation memory...
[AGENT] Starting orchestration engine...

[AGENT] All systems operational.

USER > Analyze the future of artificial intelligence.

AI > Processing request...
AI > Retrieving relevant knowledge...
AI > Evaluating technological trends...
AI > Generating structured response...

AI > Artificial intelligence is entering
     a new era of autonomous reasoning,
     multimodal intelligence, and advanced
     human-machine collaboration.

AI > Future systems will combine planning,
     memory, reasoning, and tool execution
     to solve increasingly complex problems.

AI > Analysis complete.

[STATUS] Neural engine operating normally.
[STATUS] Awaiting next instruction...

ai@neuralcore:~$ _
"""

text3 = """
commander@orion:~$ ./mission_control --launch

==================================================
            ORION SPACE COMMAND
              MISSION ALPHA-7
==================================================

[MISSION] Initializing spacecraft systems...
[MISSION] Loading navigation parameters...
[MISSION] Establishing ground communication...
[MISSION] Synchronizing onboard computers...

[CHECK] Primary flight computer......... ONLINE
[CHECK] Secondary flight computer....... ONLINE
[CHECK] Navigation system............... ONLINE
[CHECK] Communication array............. ONLINE
[CHECK] Thermal control................. ONLINE
[CHECK] Propulsion system............... READY
[CHECK] Life support.................... NOMINAL
[CHECK] Guidance control................ ACTIVE

commander@orion:~$ ./run_diagnostics

[DIAGNOSTIC] Checking propulsion sensors...
[DIAGNOSTIC] Validating navigation telemetry...
[DIAGNOSTIC] Testing redundant control systems...
[DIAGNOSTIC] Verifying communication uplink...

System diagnostics:
[####----------------] 20%
[########------------] 40%
[############--------] 60%
[################----] 80%
[####################] 100%

[DIAGNOSTIC] All simulated checks passed.

commander@orion:~$ ./launch_sequence --simulation

[MISSION CONTROL] Initiating simulated countdown.

T-10  Guidance system ready.
T-09  Navigation locked.
T-08  Communication confirmed.
T-07  Engine controller ready.
T-06  Internal power enabled.
T-05  Flight computers synchronized.
T-04  Propulsion simulation armed.
T-03  Final status verification.
T-02  All stations reporting GO.
T-01  Ignition simulation started.
T+00  LIFTOFF SIMULATION SUCCESSFUL.

[FLIGHT] Simulated vehicle ascending...
[FLIGHT] Passing 10,000 meters...
[FLIGHT] Passing 25,000 meters...
[FLIGHT] Passing 50,000 meters...
[FLIGHT] Approaching orbital insertion...

[TELEMETRY] Altitude: 180 km
[TELEMETRY] Velocity: 7.4 km/s
[TELEMETRY] Fuel remaining: 68%
[TELEMETRY] Communication: STABLE

[MISSION] Orbital insertion simulation complete.

commander@orion:~$ ./scan_deep_space

[SCAN] Activating long-range sensors...
[SCAN] Calibrating optical instruments...
[SCAN] Analyzing electromagnetic signals...
[SCAN] Mapping surrounding star systems...

[SCAN] Signal detected.
[SCAN] Determining signal origin...
[SCAN] Filtering background radiation...
[SCAN] Performing spectral analysis...

[RESULT] Signal classification: UNKNOWN
[RESULT] Signal strength: 87%
[RESULT] Estimated distance: 4.2 light-years
[RESULT] Further investigation recommended.

commander@orion:~$ cat mission_report.txt

==================================================
                MISSION REPORT
==================================================

MISSION ID          : ALPHA-7
SPACECRAFT          : ORION
MISSION TYPE        : DEEP SPACE EXPLORATION
FLIGHT STATUS       : SIMULATED ORBIT
COMMUNICATION       : ACTIVE
NAVIGATION          : NOMINAL
SENSOR ARRAY        : OPERATIONAL
UNKNOWN SIGNAL      : DETECTED

MISSION STATUS      : PHASE 1 COMPLETE

==================================================

[MISSION CONTROL] Awaiting further instructions...

commander@orion:~$ _
"""

if __name__ == "__main__":
    print(getEffects())
    time.sleep(1)
    clearScreen()
    addEffect("burn", text1)
    addEffect("beam", text2)
    addEffect("fireworks", text3)
    playAnimation()