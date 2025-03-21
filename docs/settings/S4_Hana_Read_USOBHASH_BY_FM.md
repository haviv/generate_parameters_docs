# S4 Hana Read USOBHASH BY FM

**Technical Name:** S4_Hana_Read_USOBHASH_BY_FM

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The `S4_Hana_Read_USOBHASH_BY_FM` parameter is responsible for enabling or disabling the reading of USOBHASH values through Function Modules (FMs) in S4/HANA environments. USOBHASH is a critical value related to the authorization checks and security configurations within SAP systems, ensuring that only authorized users can access specific functions and data.

**Business Impact:**

Enabling this parameter ensures that the system accurately checks permissions against the current security settings, enhancing the overall security posture by preventing unauthorized access. Disabling it might lead to a potential security risk where changes in authorization objects are not properly identified, thus exposing sensitive data or critical functions to unauthorized users.

**Technical Impact when configured:**

- When enabled, it allows the Pathlock Cloud GRC platform to read USOBHASH values, supporting comprehensive security and risk analysis by ensuring alignment with the latest SAP authorization settings.
  
- When disabled, it prevents the system from accessing these critical security settings, which may impact the platform's ability to perform thorough risk assessments, potentially leaving vulnerabilities unaddressed.

**Examples Scenario:**

A corporation utilizes the Pathlock platform for their GRC needs. By enabling `S4_Hana_Read_USOBHASH_BY_FM`, they can ensure that any changes in SAP authorizations are immediately reflected and assessed within their risk analysis modules, maintaining a high security and compliance posture.

**Related Settings:**

- `S4_Hana_Read_Disable_USOBHASH`: Disables the reading of USOBHASH, directly related to the usage of this parameter.

**Best Practices:** 

- Configure when a real-time update and thorough security check of SAP authorizations are required.
  
- Avoid when the organization's policy dictates minimizing external accesses to its SAP system for security reasons, or if the overhead on the SAP system should be minimized.