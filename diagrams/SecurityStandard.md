```mermaid
graph LR
SecurityStandard(SecurityStandard)
ATT&CK -->|entry can contain one or more|CAPEC[Common Attack Pattern Enumeration and Classification CAPEC]
CAPEC -->|entry can contain one or more|CWE[Common Weakness Enumeration CWE]
CVE -->|entry can contain one or more|CPE[Common Platform Enumeration CPE]
CVE -->|entry can contain one or more|CVSS[Common Vulnerability Scoring System CVSS]
CVE -->|entry can contain one or more|CWE[Common Weakness Enumeration CWE]
CVRF -->|entry can contain one or more|CPE[Common Platform Enumeration CPE]
CVRF -->|entry can contain one or more|CVE[Common Vulnerabilities and Exposures CVE]
CVRF -->|entry can contain one or more|CVSS[Common Vulnerability Scoring System CVSS]
CVRF -->|entry can contain one or more|CWE[Common Weakness Enumeration CWE]
