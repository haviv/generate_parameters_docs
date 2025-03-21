# Switch Back To Original User After Emergency Access

**Technical Name:** SwitchBackToOriginalUserAfterEmergencyAccess

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the system should automatically switch the user session back to the original user after an emergency access is granted and used. It is primarily intended to enhance security by ensuring that emergency access privileges are only available for the duration necessary to resolve the emergency.

**Business Impact:**

Enabling this setting ensures that the system's integrity is maintained by minimizing the risk of unauthorized access after an emergency situation has been resolved. It helps organizations adhere to security best practices and compliance requirements by safeguarding sensitive information and critical system functionalities.

**Technical Impact when configured:**

When enabled, the system will automatically revert the user's access rights back to their original state, removing the elevated access granted during the emergency. This helps in preventing potential security breaches by ensuring that emergency access rights are not misused or left enabled inadvertently.

**Examples Scenario:**

- An IT administrator requires emergency access to resolve a critical system issue. Once the issue is resolved and the emergency access is no longer needed, the system will automatically revert the user's access back to its pre-emergency state, enhancing security and compliance.

**Related Settings:** 

No explicitly related settings found in the provided code references.

**Best Practices:** 

- Configure this setting to "True" in environments where strict access control and security are essential. 
- Avoid enabling this setting if there is a need for prolonged emergency access, but ensure that such cases are reviewed and audited frequently to minimize security risks.