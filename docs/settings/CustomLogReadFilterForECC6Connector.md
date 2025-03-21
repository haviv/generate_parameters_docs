# Custom Log Read Filter For ECC6 Connector

**Technical Name:** CustomLogReadFilterForECC6Connector

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The CustomLogReadFilterForECC6Connector parameter allows users to define custom filters for reading logs from the ECC6 Connector in the Pathlock Cloud GRC platform. This ensures that organizations can tailor the retrieval of log data to meet specific security, risk management, and compliance requirements.

**Business Impact:**

Configuring this parameter effectively can significantly enhance an organization's ability to monitor and audit activities within the ECC6 environment. By filtering log data, companies can focus on the most relevant information, helping to identify potential security breaches, compliance issues, or operational risks more quickly and accurately.

**Technical Impact when configured:**

When configured, this parameter instructs the ECC6 Connector to apply the specified filter criteria to the log data being read. This can reduce the volume of data transmitted and processed, potentially improving system performance and reducing the time required for log analysis.

**Examples Scenario:**

- **Audit Readiness:** A company configures the CustomLogReadFilterForECC6Connector to exclude routine informational logs, focusing on error messages and security alerts. This approach ensures that audit-related log analysis is more efficient and focused on compliance-related events.
  
- **Security Monitoring:** To enhance security monitoring, an organization sets the filter to include only logs related to user authentication and authorization. This allows the security team to quickly detect and respond to potential unauthorized access attempts.

**Related Settings:**

- SapDownloadDataButtons

**Best Practices:** 

- **configure when** you need to refine the data being gathered from the ECC system to align with specific compliance, security, or operational requirements. Tailoring log retrieval can streamline audits and security monitoring efforts.
  
- **avoid when** unnecessary, as over-filtering can lead to missed critical information. Ensure that the filter criteria are regularly reviewed and updated in line with evolving business requirements and threat landscapes.