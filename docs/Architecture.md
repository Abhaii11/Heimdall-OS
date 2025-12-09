+---------------------+
|   Heimdall OS ISO   |
+---------------------+
         |
         v
+-------------------------------+
|   Desktop GUI Dashboard       |
|  (PyQt / Tool Launcher + IR)  |
+-------------------------------+
     |           |           |
     |           |           |
 Network      Forensics     Hardening
 Monitoring    (Autopsy)     (Firewall)
 (Zeek/Wire)                 Defaults
     |
     +--> Logs ---> Wazuh ---> AWS (S3/CloudWatch)
                         |
                        Alerting
