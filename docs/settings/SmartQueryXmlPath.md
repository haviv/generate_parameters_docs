**Technical Name:** SmartQueryXmlPath

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**

The SmartQueryXmlPath parameter specifies the file system path to XML files used within the Pathlock Cloud GRC platform for various configuration and reporting purposes. These XML files can define smart queries, report layouts, or other data structures crucial for the functioning of the platform.

**Business Impact:**

Correct configuration of the SmartQueryXmlPath is essential for ensuring that the Pathlock Cloud GRC platform can access and utilize XML-based configurations and queries. This is crucial for generating accurate and in-depth reports, performing configuration tests, and delivering event notifications precisely. Misconfiguration can lead to failures in reporting, testing, and event notification deliveries, directly impacting audit accuracy, risk management, and compliance monitoring.

**Technical Impact:** when configured

When properly configured, the SmartQueryXmlPath allows the system to reliably locate and use XML configurations, enabling:
- The dynamic creation and customization of employee profiles and reports.
- Execution of built-in configuration tests to ensure system integrity and permissions correctness.
- Utilization of custom translations and formatting for report outputs, enhancing readability and compliance.

**Examples Scenario:**

Consider an organization employs the Pathlock Cloud GRC platform for monitoring user activities and system changes across its ERP systems. By configuring SmartQueryXmlPath, the organization can define custom reports in XML format that specify what data should be extracted and how it should be presented, facilitating audits and compliance reviews. For example, creating a smart query that highlights user role changes within sensitive systems, aiding in the early detection of unauthorized privilege escalations.

**Related Settings:**

- IsInExport (Reference in employee grid column builder for report export settings)
- TestDetails (Referenced in configuration test scenarios for permissions and driver installations)

**Best Practices:** configure when setting up or updating the Pathlock Cloud GRC platform to ensure it can access necessary XML files for reports, tests, and configurations. Avoid misconfiguring the path to prevent system errors, incomplete reports, and failed configuration tests. Regularly verify the accessibility and permissions of the folder specified by SmartQueryXmlPath, especially after system updates or migrations.