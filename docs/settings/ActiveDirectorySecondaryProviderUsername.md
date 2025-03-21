# Active Directory Secondary Provider Username

**Technical Name:** ActiveDirectorySecondaryProviderUsername

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The Active Directory Secondary Provider Username parameter is used for specifying the username for connecting to a secondary Active Directory (AD) provider. This is particularly useful in environments where a fallback or secondary authentication source is required for enhanced redundancy and fault tolerance.

**Business Impact:**

Configuring this parameter ensures business continuity by providing an alternative authentication method. This is crucial in scenarios where the primary AD server is unavailable, thus preventing potential disruptions in accessing critical applications and services hosted on the Pathlock Cloud GRC platform.

**Technical Impact when configured:**

When configured, the system attempts to authenticate users against the secondary Active Directory provider using this username if the primary AD provider is unreachable. This ensures users maintain access to necessary tools and services without significant interruption.

**Examples Scenario:**

- **Scenario:** A company has a primary and a backup Active Directory server due to their high availability requirements. To configure the Pathlock Cloud GRC platform to fall back to the backup AD in case the primary is down, they use the ActiveDirectorySecondaryProviderUsername parameter to specify the username for the secondary AD connection.
  
  **Outcome:** In the event of a primary AD outage, user authentication requests automatically redirect to the secondary AD, ensuring uninterrupted access to the GRC platform.

**Related Settings:**

- `SecondaryDomainPasswordKey`

**Best Practices:** 
- **Configure when:** there is a secondary AD provider available for redundancy to ensure uninterrupted access to the platform.
- **Avoid when:** there is no secondary AD provider; configuring this setting without a valid secondary provider could cause authentication issues.
