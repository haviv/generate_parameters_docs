# Backup Root

**Technical Name:** BackupRoot

**Category:** Configuration

**Default Value:** None

**Impact Level:** High

**Description:** The BackupRoot parameter specifies the root directory used for storing backup data such as application settings, event logs, and registry backups as part of the Pathlock Cloud GRC platform's server maintenance operations.

**Business Impact:** Proper configuration of BackupRoot is critical in ensuring that backup operations are successful, which in turn helps in disaster recovery scenarios and aids in maintaining business continuity. Misconfiguration can lead to a failure in backup processes, potentially resulting in data loss during critical events.

**Technical Impact when configured:** When BackupRoot is configured correctly, it provides a centralized location for storing backups securely and efficiently. It enables the Pathlock Cloud GRC platform to perform consistent backup operations across different components, such as application settings, event logs, and registry settings, fostering a robust security and compliance posture.

**Examples Scenario:**

- **Regular Backup Routine:** A company configures BackupRoot to a dedicated backup server with ample storage. This setup simplifies management and ensures that backups are available and segregated from operational data, minimizing the risk of data loss from operational issues or cyber-attacks.

**Related Settings:** None explicitly mentioned in the provided code references.

**Best Practices:** 
- **Configure when:** Setting up the server maintenance tasks for the first time or when modifying the storage location for backup data. Ensure the specified path is accessible and has adequate storage space.
- **Avoid when:** The specified path is on the same physical drive as the operational data, or the location is not regularly monitored for available storage space, which might result in unsuccessful backups.