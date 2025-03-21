# Portal Version

**Technical Name:** PortalVersion

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** High

**Description:**

The `PortalVersion` parameter specifies the version of the user interface for the Pathlock Cloud GRC platform. This parameter controls access to various features and views within the portal, ensuring that users interact with the application's components appropriate to their version setting.

**Business Impact:**

Choosing the correct `PortalVersion` is crucial for aligning the application's functionality with the organization's current processes and compliance requirements. An incorrect version might limit access to necessary features, impacting the efficiency of managing security, risk, and compliance (GRC) activities.

**Technical Impact when configured:**

Proper configuration of `PortalVersion` ensures that users have access to the correct application routes and workflows specific to their version of the platform. It directly affects the application's routing system and the availability of certain features within both the portal and workflow design areas.

**Examples Scenario:**

- **Upgrade Preparation:** Before an organization upgrades to a newer version of Pathlock Cloud GRC, configuring the `PortalVersion` to match the upcoming version can help in validating that the new workflows and routes are fully supported.
- **Feature Access Control:** In a scenario where new features introduced in a newer version of the portal need to be restricted until proper training is provided, setting the `PortalVersion` to an earlier version can temporarily hide these features from end-users.

**Related Settings:** 

- `SendRecurringRemindersForAutoLock_Days`

**Best Practices:** 

- **configure when** planning to upgrade to a newer version to test compatibility and feature access before a complete rollout.
- **avoid when** all users have not been adequately trained on the features of the new version, as it may lead to confusion or misuse of the platform's capabilities.