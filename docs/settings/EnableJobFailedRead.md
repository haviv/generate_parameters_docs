# Enable Job Failed Read

**Technical Name:** EnableJobFailedRead 

**Category:** Audit

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter enables reading failed job entries from the SAP system. When enabled, it captures and logs entries related to failed transactions or jobs, helping in audit and compliance efforts by providing a trail of failed attempts that could indicate misuse or an attempt to bypass security controls.

**Business Impact:** By enabling this feature, organizations can enhance their audit capabilities, ensuring that all failed transactions or job attempts are logged and reviewed. This can be critical for identifying and addressing potential security breaches or compliance issues early, enhancing overall governance, risk management, and compliance (GRC) processes.

**Technical Impact when configured:** When enabled, transaction codes (T-Codes) that fail are captured along with the user name, timestamp, and transaction identifier (Transid), but without the IP address. This data is essential for auditing and monitoring potentially suspicious activities within the SAP system.

**Example Scenario:** Consider a scenario where there is a need to monitor and audit all failed attempts to execute specific high-risk transactions in SAP. By enabling the `EnableJobFailedRead` parameter, the organization can ensure that these failed attempts are captured and logged for further investigation and audit trails, assisting in identifying whether the failures are due to user errors, system issues, or potential malicious activities.

**Related Settings:** 

- `SodFullReportRunOfflineNotifiyInMail`

**Best Practices:** 

- **Configure when:** There is a requirement for detailed audit trails, including failed jobs or transactions within SAP systems, particularly for sensitive or critical operations.
  
- **Avoid when:** The additional logging of failed transactions might result in excessive data storage requirements or if there's no specific need to audit failed transactions in detail.