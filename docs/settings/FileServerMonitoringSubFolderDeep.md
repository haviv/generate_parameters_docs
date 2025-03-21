# File Server Monitoring Sub Folder Deep

**Technical Name:** FileServerMonitoringSubFolderDeep

**Category:** Configuration

**Default Value:** 0

**Impact Level:** Medium

**Description:**

This parameter configures the depth of subfolder monitoring within the file server's directory structure for the Pathlock Cloud GRC platform. It determines how deep into the directory hierarchy the system will monitor for changes, focusing primarily on activities within specified folders.

**Business Impact:**

Setting an appropriate value for this parameter helps in maintaining a careful balance between security and performance. A higher depth level can provide more detailed monitoring of file server activities, which is critical for achieving compliance with various regulatory standards. However, it may also lead to higher resource consumption. On the other hand, setting this too low might miss important activities happening in deeper folders, potentially compromising security.

**Technical Impact when configured:**

- **Higher Values:** More extensive monitoring capabilities, which can capture activities occurring in deeper nested folders, enhancing security and compliance posture. This comes at the cost of increased resource usage.
  
- **Lower Values:** Reduced system load due to less intensive monitoring. While this improves performance, it may overlook activities in deeper folders, which can be a security risk.

**Examples Scenario:**

- **Compliance Requirement:** An organization must comply with GDPR, needing to monitor access and modifications to personal data stored in file servers. By configuring `FileServerMonitoringSubFolderDeep` to an appropriate depth, the organization can ensure it captures all relevant activities without overly straining system resources.
  
- **Security Policy:** A company's security policy mandates monitoring any change in the network share containing sensitive financial data. Setting this parameter ensures that even changes in nested folders are detected and reported.

**Related Settings:**

- `MonitoredApplications` - defines the specific applications or directories to be monitored alongside their depth levels.
  
- `FoldersWithoutPermissions` - specifies folders that should be skipped during monitoring due to lack of permission or other criteria.

**Best Practices:** 

- **Configure when**: You need detailed auditing of file and folder activities to meet security and compliance requirements. It's particularly important when sensitive data is stored in nested directory structures.

- **Avoid when**: The emphasis is on minimizing system impact, and the risk associated with not monitoring deeper directories is low. In such cases, prioritize monitoring only the top-level directories or those known to contain sensitive information.