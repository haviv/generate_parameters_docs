**Technical Name:** ActiveDirectorySsoGroupName

**Category:** User Management

**Default Value:** 

**Impact Level:** High

**Description:** 

The 'ActiveDirectorySsoGroupName' parameter specifies the name of the Active Directory (AD) group that is used for Single Sign-On (SSO) authentication in the Pathlock Cloud GRC platform. It determines which AD group's members are permitted automated access to the platform without requiring additional credentials.

**Business Impact:**

Configuring this parameter directly impacts the ease of access for authorized users, streamlining the login process by enabling SSO. It improves user experience, reduces login time, and minimizes the chance of password-related security breaches. However, inaccurate configuration could lead to unauthorized access or accidental lock-out of legitimate users.

**Technical Impact when configured:**

When properly configured, this setting ensures that only members of the specified AD group can utilize SSO to access the platform, enforcing control over platform access and simplifying user management. It interacts with the organization's Active Directory to validate user memberships against the given group name, enabling secure and efficient authentication and authorization processes.

**Examples Scenario:**

Scenario: A company wants to enable SSO for its finance department to securely and quickly access the Pathlock Cloud GRC platform. The IT administrator sets the 'ActiveDirectorySsoGroupName' to "FinanceDeptSSO", a group within their Active Directory that includes all members of the finance department. This enables members of the finance team to access the Pathlock platform using their AD credentials without needing to manage separate logins for the GRC platform.

**Related Settings:**

- CustomTerminateDateFieldinActiveDirectory
- CustomTerminateDateFieldinActiveDirectoryDateFormat

**Best Practices:** configure when

- You have a clear understanding of which user group requires access to the Pathlock Cloud GRC platform through SSO.
- You have verified that all users within the specified Active Directory group are intended to have access to the platform.

avoid when

- The specified Active Directory group includes users who should not have access to the Pathlock Cloud GRC platform.
- There is no established process for managing membership of the specified Active Directory group, risking unauthorized access.