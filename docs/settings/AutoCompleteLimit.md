# Auto Complete Limit

**Technical Name:** AutoCompleteLimit

**Category:** Configuration

**Default Value:** Value is set by `CommonSettings.Default.AutoCompleteLimit`. 

**Impact Level:** Medium

**Description:**

The `AutoCompleteLimit` parameter controls the maximum number of results returned for auto-complete suggestions in various entity and column name searches throughout the Pathlock Cloud GRC platform. This setting optimizes performance and user experience by limiting the volume of data fetched and displayed during auto-completion operations.

**Business Impact:**

Configuring an appropriate limit enhances user experience by providing a manageable list of auto-complete suggestions, which facilitates faster and more accurate data entry. This is particularly important in environments with large datasets, where unrestricted auto-complete results could overwhelm users and impact the efficiency of security, risk, or compliance tasks.

**Technical Impact when configured:**

A carefully chosen limit can significantly reduce the load on the system by preventing excessive database queries and network traffic, which contributes to overall system responsiveness and reliability. However, setting this limit too low might restrict the usefulness of auto-complete features, forcing users to manually type more information.

**Examples Scenario:**

For instance, when adding a new risk assessment, as an assessor types the name of an entity within the "Entity Name" field, the auto-complete feature suggests possible matches. If the AutoCompleteLimit is set to 10, only the first 10 matching entities are suggested.

**Related Settings:** None identified in the provided references.

**Best Practices:** 

- **Configure when:** There is a need to balance between the usability of auto-complete features and system performance. For large datasets, a lower limit ensures better performance.
- **Avoid when:** Users require extensive auto-complete suggestions to effectively find rare or less frequently accessed entities, in which case a slightly higher limit may be appropriate.