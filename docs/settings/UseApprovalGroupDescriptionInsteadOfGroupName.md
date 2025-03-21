# Use Approval Group Description Instead Of Group Name

**Technical Name:** UseApprovalGroupDescriptionInsteadOfGroupName

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the approval process within workflow actions utilizes the descriptive label of a group rather than its technical name. This is particularly relevant in scenarios where group names are not intuitive or do not clearly convey the group's purpose or membership.

**Business Impact:**

Enabling this feature can increase clarity for administrators and approvers by using more descriptive and understandable terms. This is especially beneficial in complex environments where group names may be cryptic or formulated based on internal conventions that are not widely understood.

**Technical Impact when configured:**

When enabled, this parameter ensures that throughout the approval workflow process, especially in the `WorkFlowApprovalGroupStep`, the descriptive labels of groups are displayed instead of their technical names. This can aid in reducing confusion and making the approval process more transparent.

**Examples Scenario:**

- **Before Configuration:** Approval groups are displayed as "GRP00123", which does not provide intuitive insight into the group's purpose.
- **After Configuration:** The same approval group is displayed as "Finance Department Approvers", clearly indicating the function and membership of the group.

**Related Settings:**

- `DisableCustomReportQueyCaching` - While not directly related, adjusting this setting may impact the performance of reports that utilize approval group data.

**Best Practices:** 

- **Configure when:** Approval processes involve multiple groups with technical names that do not clearly convey their purpose.
- **Avoid when:** Approval group names are already descriptive enough or when changes might cause confusion among current users familiar with the existing naming conventions.