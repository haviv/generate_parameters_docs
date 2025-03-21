# Everyone Role In PTD

**Technical Name:** EveryoneRoleInPTD

**Category:** Security

**Default Value:** * (Asterisk symbol representing everyone)

**Impact Level:** High

**Description:**

The `EveryoneRoleInPTD` parameter is designed to specify whether a role in the Pathlock GRC platform should be accessible by all users, regardless of their individual permissions or roles. When set to its default value (*), it implies universal access, allowing every user within the platform to access certain functionalities or areas marked with this role.

**Business Impact:**

Configuring the `EveryoneRoleInPTD` parameter to allow access for everyone can significantly enhance the user experience by simplifying access to common resources or functionalities that are intended to be universally available. However, incorrect configuration can lead to security vulnerabilities, as sensitive information or critical functionalities could become accessible to users without the appropriate clearance or intent.

**Technical Impact when configured:**

When the `EveryoneRoleInPTD` is configured to its default state, it systematically overrides individual user permissions and roles, granting blanket access to the specified functionalities within the Pathlock GRC platform. This configuration can be beneficial for features meant to be public or accessible by all users, but it must be managed carefully to avoid unintended security risks.

**Examples Scenario:**

An organization wants to make certain compliance documentation available to all employees using the Pathlock GRC platform, regardless of their department or role. By configuring the `EveryoneRoleInPTD` for the documentation section, the organization can ensure that all users have read access, fostering transparency and widespread awareness of compliance protocols.

**Related Settings:**

- `AddSupportForExcelProtectedFile` (Although seemingly unrelated, careful consideration should be given to how universal access settings like `EveryoneRoleInPTD` might interact with features controlled by other settings).

**Best Practices:** 

- **Configure when:** There is a clear requirement for universal access to certain non-sensitive resources or functionalities within the Pathlock GRC platform. This ensures that all users can effortlessly access these resources without unnecessary barriers.
  
- **Avoid when:** The resource or functionality is sensitive or should only be accessible by users with specific roles or permissions. Always verify the necessity of universal access to prevent potential security breaches.