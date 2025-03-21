**Technical Name:** VMSFolder

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The VMSFolder parameter specifies the directory path used by the Pathlock GRC platform for storing and accessing various files required for its operations. This includes temporary files created during data transformation processes, connector files for bank systems, and other critical workflow-related files.

**Business Impact:**

Configuring the VMSFolder correctly ensures that the Pathlock GRC platform can efficiently process, store, and manage files necessary for security, risk, compliance activities, and workflow operations. A properly configured VMSFolder supports the seamless execution of data loading activities, thereby minimizing disruptions to business processes and ensuring data integrity and security.

**Technical Impact when configured:**

- Improved file management by consolidating all workflow and process-related files in a designated directory.
- Enhanced performance and reliability of the Pathlock GRC platform due to optimized file access and storage practices.
- Reduced risk of data loss or misplacement by centralizing file storage.

**Examples Scenario:**

- An organization needs to ensure that all temporary files generated during the execution of compliance checks are stored in a secure, central location for auditing purposes. By configuring the VMSFolder parameter, the organization can designate a specific directory for these files, facilitating easy access and management.

**Related Settings:**

- SendApprovalInformationToRequester
- WorkflowItemAdminNotificationFormat

**Best Practices:** 

- **Configure when**: Setting up the Pathlock GRC platform or when changing the system's file storage and management practices.
- **Avoid when**: The specified directory path is not secured, or if there are insufficient permissions for the Pathlock GRC platform to write to and manage files in the designated folder.