# Show Role High Risk Icon Column

**Technical Name:** ShowRoleHighRiskIconColumn

**Category:** Security

**Default Value:** False

**Impact Level:** High

**Description:**

This parameter controls the visibility of a high-risk icon next to roles within the Pathlock Cloud GRC platform. When enabled, a warning icon is displayed next to roles deemed high-risk, based on their configuration and associated permissions.

**Business Impact:**

Enabling this feature assists in quickly identifying high-risk roles, facilitating easier governance and improved risk management. It aids compliance teams and security administrators in prioritizing their review and mitigation efforts towards the most sensitive parts of the system.

**Technical Impact when configured:**

Once configured, a warning icon (symbolized by a yellow triangle with an exclamation mark) appears next to roles classified as high risk. This visual cue is intended to draw immediate attention to potential security risks, helping in the rapid identification and addressing of such vulnerabilities.

**Examples Scenario:**

- **Role Review**: During periodic security reviews, an auditor can quickly scan through the list of roles and immediately spot which ones are high-risk, needing further investigation or immediate action.

**Related Settings:**

- There are no direct related settings found in the provided code references. 

**Best Practices:** configure when roles have been evaluated for risk and you wish to offer visual cues for quick identification; avoid when not all roles have been assessed for risk, to prevent a false sense of security.