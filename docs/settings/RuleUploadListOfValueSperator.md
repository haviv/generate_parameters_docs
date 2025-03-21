**Rule Upload List Of Value Separator**

**Technical Name:** RuleUploadListOfValueSeparator

**Category:** Configuration

**Default Value:** "," (comma)

**Impact Level:** Medium

**Description:**

The Rule Upload List Of Value Separator parameter is used to define the character or string that separates values within a list when uploading rules to the Pathlock Cloud GRC platform. This setting ensures correct parsing and interpretation of lists contained in the data being imported, such as roles, permissions, or other entity attributes, by specifying how individual values are distinguished from one another.

**Business Impact:**

Proper configuration of this parameter is crucial for maintaining the integrity of rule definitions within the Pathlock Cloud GRC environment. Incorrectly configured separators can lead to erroneous rule interpretations, which may subsequently impact the platform's ability to accurately assess compliance, enforce access controls, or identify risks. Ensuring this parameter is correctly set preserves the operational effectiveness of security, risk, and compliance activities.

**Technical Impact when configured:**

- Correct parsing of imported lists: Facilitates the accurate importation of complex data by specifying how to effectively separate individual elements within a list, impacting the effective governance of roles, permissions, and compliance policies.
- Error reduction: Minimizes the probability of import errors that can arise from incorrectly formatted data, ensuring that rule uploads do not fail due to parsing issues.

**Example Scenario:**

Consider a situation where an organization is importing a list of roles associated with specific permissions. If the Rule Upload List Of Value Separator is set to a comma (`,`), the system will recognize each comma-separated value as a distinct role or permission. For example, a string "Role1,Role2,Role3" will be correctly parsed into three separate roles: Role1, Role2, and Role3. Incorrect configuration (e.g., using a semicolon `;` as a separator while the data uses commas) would lead to parsing errors or incorrect data interpretation.

**Related Settings:**

- RolesSplliterRolesChildRolePattern
- FMGetMissingAuthorizationForUser

**Best Practices:** configure when

- Importing rules that contain lists or multiple values requiring separation.
- Initial configuration of the Pathlock Cloud GRC platform to ensure compatibility with existing data formatting conventions.

avoid when

- There is a mismatch between the configured separator and the actual data format used in rule definitions, which can lead to import failures or incorrect data parsing.