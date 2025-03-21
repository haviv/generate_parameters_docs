# Rebuild Users Minimal Sync Profiles For AD

**Technical Name:** RebuildUsersMinimal_SyncProfilesForAD

**Category:** User Management

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

This parameter controls the process of synchronizing minimal user profiles from Active Directory (AD) into the Pathlock platform. It is designed to streamline the process of syncing user data by focusing on essential information, thus optimizing performance and reducing sync times.

**Business Impact:**

Enabling this parameter can significantly impact the efficiency and speed of user data synchronization processes. It is particularly beneficial for organizations with a large number of user profiles in AD that need to be managed within the Pathlock platform. Efficient sync processes can lead to improved system performance and user experience.

**Technical Impact when configured:**

When configured, this parameter initiates a process to rebuild and synchronize minimal user profiles from AD. It implies that only critical user attributes are considered during the sync process, which might include identifiers like UserID, roles, and basic access privileges but excludes extensive profile details.

**Examples Scenario:**

Consider an organization undergoing a company-wide system update where all user profiles need to be quickly updated in the Pathlock platform to reflect recent changes in job roles and access privileges. Activating this parameter can expedite the sync process, ensuring that the system reflects the most current user information without unnecessary delays.

**Related Settings:** EnableCollapseCompositeRolesView

**Best Practices:** 

- **Configure when:** Immediate updates of user profiles in the Pathlock platform are required, especially following significant changes in user roles or permissions within AD.
- **Avoid when:** Comprehensive details of user profiles are needed to be synced. In such cases, syncing full profiles might be more appropriate to ensure no critical information is omitted.