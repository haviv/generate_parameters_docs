# Import Managers Disable Approval Group Cleanup

**Technical Name:** ImportManagersDisableApprovalGroupCleanup

**Category:** User Management

**Default Value:** Not Applicable

**Impact Level:** Medium

**Description:**

The `ImportManagersDisableApprovalGroupCleanup` parameter controls whether the cleanup process for approval groups is disabled when importing managers into the Pathlock Cloud GRC platform. This parameter specifically affects the handling of inactive user groups during the import process.

**Business Impact:**

Enabling this setting can have significant implications for how approval groups are managed within the organization. Keeping it disabled (which is the implied default behavior) ensures that approval groups are cleaned up and organized, reducing the risk of obsolete or inactive groups cluttering the system. Enabling it, however, may be necessary in scenarios where approval groups for inactive users need to be preserved for audit, compliance, or operational reasons.

**Technical Impact when configured:**

When configured, this setting prevents the automatic cleanup of approval groups related to inactive managers during the import process. This could potentially lead to a larger number of inactive groups being present in the system, which may affect system performance or complicate user management and reporting.

**Examples Scenario:**

An organization is undergoing an audit and needs to maintain a comprehensive record of all approval groups, including those that are inactive, to comply with regulatory requirements. By setting `ImportManagersDisableApprovalGroupCleanup` to avoid deleting these groups, the organization can ensure that their GRC platform fully reflects historical approval processes for the duration of the audit.

**Related Settings:** Not Applicable

**Best Practices:** Configure this setting when there is a specific regulatory or business need to retain approval groups for inactive users. Avoid using this setting under normal operational conditions to prevent unnecessary accumulation of inactive groups, which can clutter the system and impact performance.