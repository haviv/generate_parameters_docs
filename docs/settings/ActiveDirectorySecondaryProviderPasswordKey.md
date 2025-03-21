# Active Directory Secondary Provider Password Key

**Technical Name:** ActiveDirectorySecondaryProviderPasswordKey

**Category:** Security

**Default Value:** ""

**Impact Level:** High

**Description:**

The `ActiveDirectorySecondaryProviderPasswordKey` parameter is used within the Pathlock platform to store the password key used for authentication with a secondary Active Directory (AD) provider. This setting plays a crucial role in ensuring that the system can securely access and synchronize with secondary AD sources when primary sources fail or are unavailable.

**Business Impact:**

Configuring this parameter with a correct and secure value ensures continuous access to user and group information from a secondary AD source, minimizing disruptions in user management, access control, and security policy enforcement. It significantly impacts the organization's ability to maintain robust security and compliance postures by ensuring uninterrupted synchronization with AD services.

**Technical Impact when configured:**

- Enables the Pathlock platform to authenticate with a secondary AD provider securely.
- Allows for uninterrupted user and group synchronization in scenarios where the primary AD provider is unavailable.
- Strengthens the security by allowing encrypted storage and usage of AD credentials.

**Examples Scenario:**

Consider a scenario where an organization has a primary AD provider for normal operations and a secondary AD provider as a backup. If the primary AD provider experiences downtime due to maintenance or unforeseen issues, the `ActiveDirectorySecondaryProviderPasswordKey` ensures that Pathlock can seamlessly switch to the secondary provider for user and group data, thereby maintaining continuous operations and compliance with access control policies.

**Related Settings:**

- `ActiveDirectoryProviderUsername`

**Best Practices:** 

- **Configure when**: Setting up high availability for your AD infrastructure or when integrating multiple AD services.
- **Avoid when**: There is only one AD service provider, or if the secondary AD provider will not be used for fallback purposes.