# Share To Directory Select

**Technical Name:** ShareToDirectorySelect

**Category:** Configuration

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

The ShareToDirectorySelect parameter enables administrators to specify a directory path for sharing resources within the Pathlock Cloud GRC platform. This setting is crucial for defining how and where shared resources within the SAP Connector for Active Directory are accessed and managed.

**Business Impact:**

By configuring this parameter, organizations can streamline their resource sharing strategy, ensuring that sensitive data and resources are only accessible in specific, secure directories. This enhances data management practices and supports compliance with data protection standards.

**Technical Impact when configured:**

Once the ShareToDirectorySelect parameter is configured, it directs the SAP Connector for Active Directory to utilize a specified directory path when sharing resources. This configuration ensures that resources are shared in a controlled environment, reducing the risk of unauthorized access or data leakage.

**Examples Scenario:**

An organization wishes to limit access to shared SAP reports to a specific network directory. By configuring the ShareToDirectorySelect parameter to point to this directory, the organization can ensure that only authorized personnel can access these reports from the specified path.

**Related Settings:**

- `ScopeDirectoryPath`

**Best Practices:** configure when establishing secure data sharing practices within the organization; avoid when there is no clear data management strategy or policy in place.