# Show User Group Filter Outside Users Filter

**Technical Name:** ShowUserGroupFilterOutsideUsersFilter

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter controls whether user-specific filters, particularly those related to displaying or hiding user groups, are applied outside the traditional user filter areas within the Pathlock Cloud GRC platform. This setting adjusts the visibility and application of user group filters in sections of the platform not traditionally associated with user-specific filtering, enhancing the customization and relevance of data and reports.

**Business Impact:**

Enabling this parameter improves the user experience by allowing administrators to tailor the visibility of information and reports based on specific user groups outside the standard filtering areas. This can lead to more focused and efficient security management, risk assessment, and compliance reporting by ensuring only relevant data is made visible to specific user groups, thereby minimizing information overload and streamlining the decision-making process.

**Technical Impact when configured:**

When enabled, the parameter affects the platform's user interface by modifying the visibility of specific data and reports based on user group membership outside the usual filter areas. This can include altering which systems, risks, or compliance metrics are visible to a user based on their group affiliations, thereby providing a more customized and relevant user experience.

**Examples Scenario:**

A company has multiple user groups based on departments, such as HR, Finance, and IT. By enabling the Show User Group Filter Outside Users Filter, the platform can be configured to only show HR-related system risks to the HR department users, finance-related compliance issues to Finance department users, and so forth, even in sections of the platform that don't typically offer this level of filtering.

**Related Settings:** 

- HideXpandionNews: This setting, while not directly related, indicates the presence of user-centered customization features within the platform's common settings, suggesting a broader context for the application of the ShowUserGroupFilterOutsideUsersFilter setting for enhancing user experience and relevance of displayed information.

**Best Practices:** Configure when your organization requires a high level of data and report customization to ensure that users and departments are only presented with the information that is most relevant to their tasks. Avoid when such detailed customization is unnecessary, as it may lead to the complication of the platform's configuration and maintenance without significant benefits.