# Ccm Drawer Field Set

**Technical Name:** CcmDrawerFieldSet

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CcmDrawerFieldSet` parameter is designed to configure how details within a workflow, specifically around authorization certifications and data exception details, are presented and interacted with by users. It affects the layout and fields available in the drawer (sidebar) that appears in the Pathlock Cloud GRC platform during these workflow steps.

**Business Impact:**

Proper configuration of this parameter can streamline the user experience, making it easier for users to review, certify, or manage exceptions within their workflow tasks. It impacts how quickly and efficiently tasks related to authorization certifications and data exceptions are resolved, which in turn affects the overall security, compliance, and risk management processes within an organization.

**Technical Impact when configured:**

When configured, `CcmDrawerFieldSet` alters the presentation and availability of information and controls within the workflow steps related to authorization certifications and data exception details. This can lead to a more tailored and efficient user interaction, directly impacting the effectiveness of these workflows.

**Examples Scenario:**

For instance, in a scenario where a company must certify user roles and permissions within its GRC platform, the `CcmDrawerFieldSet` can be configured to only display relevant fields and information needed for certifiers to make informed decisions quickly.

**Related Settings:**

- `CampaignNameDateFormat`

**Best Practices:** Configure when you need to optimize the workflow steps related to certification and exception handling. Avoid when default workflow configuration suffices for your organization's needs.