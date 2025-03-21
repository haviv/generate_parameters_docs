**Enable Directory Monitoring Active Directory Monitoring**

**Technical Name:** EnableDirectoryMonitoringActiveDirectoryMonitoring

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

This parameter activates or deactivates the directory monitoring feature specifically for Active Directory environments in the Pathlock Cloud GRC platform. When enabled, it allows the system to monitor and log activities and changes within specified Active Directory paths, aiding in the oversight of security and compliance.

**Business Impact:**

Enabling this feature provides crucial visibility into the modifications and interactions within the Active Directory, which is fundamental for maintaining security and compliance standards. It aids in detecting potentially unauthorized or malicious changes, ensuring that user and group policies are aligned with corporate governance and compliance requirements.

**Technical Impact when configured:**

Upon configuration, the system begins to monitor designated directories in the Active Directory, capturing and logging transactions and session activities. This includes tracking the creation, modification, and deletion of directory objects, providing administrators with detailed insights into users' actions and resource accesses.

**Examples Scenario:**

- In the case of an audit, enabling directory monitoring provides a comprehensive log of all changes made within the Active Directory over the monitored period, assisting in demonstrating compliance with regulatory requirements.
- To enhance security, monitoring can detect unauthorized changes to sensitive directories, triggering alerts for immediate investigation and remediation.

**Related Settings:**

- ManagedPasswordsSettings

**Best Practices:** configure when the tracking of user activities and changes within Active Directory is a compliance requirement or a part of the organizational security policy. Avoid when monitoring is not necessary due to the potential overhead on system resources and the volume of generated logs.