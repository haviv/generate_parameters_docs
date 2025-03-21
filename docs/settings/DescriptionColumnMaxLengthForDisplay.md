**Technical Name:** DescriptionColumnMaxLengthForDisplay

**Category:** Reporting

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

The `DescriptionColumnMaxLengthForDisplay` parameter controls the maximum length of text that can be displayed in description fields within reports. This setting ensures that the display of lengthy descriptions is properly managed to enhance readability and presentation without impacting the underlying data integrity.

**Business Impact:**

Controlling the maximum length of description texts in reports directly impacts how information is consumed by stakeholders. It ensures that reports remain concise and focused, improving the decision-making process by presenting data in a digestible format. It particularly benefits roles involved in risk management, compliance, and auditing by allowing them to quickly grasp essential information.

**Technical Impact when configured:**

When configured, this parameter dynamically adjusts the display length of description fields in reports. It ensures that texts exceeding the specified maximum length are truncated or suitably formatted for display purposes, enhancing the user interface and user experience.

**Examples Scenario:**

- **Before Configuration:** Reports generated for compliance reviews contain description fields with extensive text, making it challenging to quickly assess and identify key information.
- **After Configuration:** Setting the `DescriptionColumnMaxLengthForDisplay` to a practical value, like 200 characters, reports now present descriptions in a more consumable manner, facilitating quicker reviews and assessments by compliance officers.

**Related Settings:** MaxRoleSizeForRoleAdvisorDialog

**Best Practices:** 

- **Configure when:** You are dealing with reports that contain lengthy descriptions. Setting a reasonable limit based on your organization’s reporting format and user preference can significantly improve readability.
- **Avoid when:** Every detail in the description is critical to the report's purpose, and summarization may lead to loss of vital information. In such cases, consider alternative approaches to present detailed descriptions.