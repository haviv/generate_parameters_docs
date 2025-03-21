# Custom Central User Administration Server Host

**Technical Name:** CustomCUAServerHost

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

The Custom Central User Administration Server Host (CustomCUAServerHost) parameter specifies the hostname or IP address of the server designated for Central User Administration (CUA) in the Pathlock Cloud GRC platform. This setting is crucial for organizations utilizing CUA to streamline and centralize the management of user accounts across multiple systems or applications.

**Business Impact:**

Setting the CustomCUAServerHost parameter correctly is vital for ensuring efficient and centralized user management within an organization. It directly impacts the ability to securely and effectively administer user permissions, roles, and access across various systems, thereby supporting compliance with internal and external regulations. Incorrect configuration can lead to synchronization issues, compromised security, and increased administrative overhead.

**Technical Impact when configured:**

Configuring the CustomCUAServerHost parameter enables the Pathlock Cloud GRC platform to connect to the specified CUA server for user data synchronization and central management. This configuration supports streamlined operations such as role assignments, user creations, and terminations across all connected systems, enhancing security and compliance postures by ensuring consistent enforcement of user access policies.

**Examples Scenario:**

A company wants to ensure that any changes in employee roles are reflected promptly across all its systems to maintain security and comply with audit requirements. By configuring the CustomCUAServerHost parameter, the company can automate the synchronization of these changes from a central point, thus minimizing potential security risks associated with manual updates and delays in access revocation.

**Related Settings:**

- EnableCUA
- DisableCua

**Best Practices:** configure when centralizing user administration across multiple systems or applications to ensure security and compliance. Avoid when the organization does not use Central User Administration policies, as incorrect configuration can lead to system integration issues.
