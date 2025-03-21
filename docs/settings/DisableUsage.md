# Disable Usage

**Technical Name:** DisableUsage

**Category:** Configuration

**Default Value:** Not explicitly given; infer as "false" to maintain system operability in absence of explicit disablement.

**Impact Level:** Medium

**Description:** A configuration setting designed to temporarily disable certain functions or features within the Pathlock Cloud GRC platform without permanently altering the system's setup or requiring extensive configuration changes. This can be particularly useful for troubleshooting, during maintenance, or when a specific functionality needs to be paused, usually for a short period.

**Business Impact:** Allows administrators to manage and control the availability of features and functionalities within the Pathlock Cloud GRC platform to ensure compliance and integrity of the GRC processes. By enabling this setting, businesses can mitigate risks associated with uncontrolled feature usage, including the potential for unauthorized access or operational disruptions.

**Technical Impact when configured:** When enabled, this setting prevents the use of certain features or services within the platform. It may be used to restrict access to sensitive functions during sensitive periods or to disable functions that are under review for security, compliance, or operational integrity reasons.

**Examples Scenario:**

- **Maintenance Mode:** Prior to system upgrades or maintenance, an administrator enables DisableUsage to prevent users from initiating new processes that can't be completed during the maintenance window.
  
- **Security Incident:** In response to a detected security threat, certain platform functionalities are temporarily disabled to mitigate potential damage or unauthorized access.

**Related Settings:** DisableWorkingHours - This setting might be similarly used to restrict or control usage based on time constraints, offering a nuanced approach to feature availability.

**Best Practices:** 

- **Configure when:** Immediate action is required to mitigate operational, security, or compliance risks. Temporarily disabling a feature can provide the necessary time to assess and address any issues without causing unnecessary system downtime or disrupting user activities significantly.
  
- **Avoid when:** Permanent changes to system functionality are required. For long-term adjustments, consider using more specific configuration settings or permissions to refine system behavior instead of broadly disabling functionalities.