**Technical Name:** RoleDescriptionMaxLengthForDisplay

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**
This parameter determines the maximum length of role descriptions that are displayed within the Pathlock Cloud GRC platform. It ensures that role descriptions adhere to a consistent length standard, enhancing readability and uniformity across the system interfaces.

**Business Impact:**
Setting an appropriate maximum length for role descriptions can significantly improve the clarity and effectiveness of role information presented to end users. It helps in avoiding the confusion that can arise from overly lengthy descriptions, making it easier to understand and manage roles within the system.

**Technical Impact when configured:**
When this parameter is configured, any role description exceeding the specified maximum length will be truncated or otherwise adapted to meet this limit. This affects how role information is displayed in various parts of the platform, including workflow updates and system configurations.

**Example Scenario:**
- A system administrator sets the `RoleDescriptionMaxLengthForDisplay` to 100 characters. If a role description is "Senior Financial Analyst with Extended Responsibilities in Budgeting and Forecasting", and its length exceeds 100 characters, it would be displayed up to the 100th character, ensuring that all role descriptions in the system are of a uniform length and are displayed neatly across the platform interfaces.

**Related Settings:** 

**Best Practices:** 
- **Configure when:** It is crucial to maintain uniformity and clarity in the display of role descriptions across the system, especially in environments with a large number of roles or when descriptions tend to be verbose.
- **Avoid when:** The specifics of every role must be displayed fully without truncation, or when the system is used in a context where the detailed descriptions are critical for decision-making or compliance purposes.