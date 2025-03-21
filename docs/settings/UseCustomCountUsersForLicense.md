# Use Custom Count Users For License

**Technical Name:** UseCustomCountUsersForLicense

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The UseCustomCountUsersForLicense parameter allows organizations to customize how users are counted for licensing purposes within the Pathlock Cloud GRC platform. This setting is beneficial for tailoring the licensing model to fit specific organizational needs or to accommodate unique user management scenarios.

**Business Impact:**

Adjusting this parameter can significantly affect the licensing costs and compliance of the Pathlock GRC platform. Organizations can optimize their licensing expenditure by only including relevant users in the license count, potentially excluding service accounts, temporary users, or specific user roles that do not require full access to the Pathlock functionalities.

**Technical Impact when configured:**

When enabled, this setting alters the default behavior of the licensing mechanism by applying a custom user count for licensing. It requires thorough planning and understanding of the licensing agreement with Pathlock to ensure compliance and to accurately reflect the organization's actual user base within the licensing count.

**Examples Scenario:**

An organization wishes to exclude service accounts from their licensing count due to their high number but low activity level. By enabling the UseCustomCountUsersForLicense parameter, they can adjust their user count to exclude these accounts, potentially lowering their licensing fees.

**Related Settings:**

N/A

**Best Practices:** 

- **Configure when:** Your organization's user base includes a significant number of users that should not count towards the licensing total, such as service accounts or temporary users.
  
- **Avoid when:** Your user base is straightforward without the need for custom counting or when unsure of the licensing agreement terms with Pathlock, as improper configuration may lead to compliance issues.