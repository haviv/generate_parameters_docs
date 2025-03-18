# Actions Address

**Technical Name:** Actions_Address

**Category:** Workflow

**Default Value:** None

**Impact Level:** High

**Description:**

The `Actions_Address` parameter is used to configure the email address for sending notifications related to specific events or violations detected by the Pathlock Cloud GRC platform.

**Business Impact:**

Setting this parameter ensures that designated data owners or administrators are promptly notified about important security or compliance events, aiding in the swift resolution of issues that could otherwise compromise the organizational GRC (Governance, Risk Management, and Compliance) posture.

**Technical Impact when configured:**

When the `Actions_Address` is configured, the system triggers automated email notifications to the specified address(es) upon the occurrence of configured events or violations. This facilitates real-time awareness and responsiveness to critical GRC-related activities within the organization.

**Examples Scenario:**

For instance, if an application area within the system detects a violation of SoD (Segregation of Duties) policies, the `Actions_Address` parameter ensures that an email is dispatched to the relevant data owner or specified email address, providing details about the violation for immediate action.

**Related Settings:**

- CommonSettings.Default.IsValidateInstallation
- CommonSettings.Default.ShowCSG
- CommonSettings.Default.SettingsKey
- CommonSettings.Default.RolesRegistryNodes

**Applicable Workflows Actions:**

N/A

**Best Practices:** 

- **Configure when:** You want to ensure that key personnel are immediately informed about important events, allowing for rapid response to potential issues.
- **Avoid when:** Notifications for certain events are not necessary or when over-notification could lead to alert fatigue among recipients.