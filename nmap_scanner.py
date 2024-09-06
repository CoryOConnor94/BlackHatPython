import nmap
import json

scannerObject = nmap.PortScanner
results = scannerObject.scan_top_ports("localhost")
results = json.dumps(result, indent=1, sort_keys=True)
print(results)