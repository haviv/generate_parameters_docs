# Use Forbidden Combination With Schema Filter

**Technical Name:** UseForbiddenCombinationWithSchemaFilter

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** This parameter controls whether the platform should filter out certain combinations of schema definitions that are deemed forbidden based on specific business rules or security policies.

**Business Impact:** Enabling this parameter ensures that the reports generated or the data accessed through the GRC platform adhere to organizational policies and compliance requirements by omitting potentially risky or non-compliant schema combinations.

**Technical Impact when configured:** When this parameter is enabled, the system will apply additional filters on the generated reports or data queries to exclude any combinations of schemas that are identified as forbidden. This may impact the availability of certain data in reports or queries, ensuring that users are only able to access compliant and approved information.

**Example Scenario:** If an organization has determined that certain combinations of access rights or data schemas pose a security risk (e.g., access to both personnel records and financial records by the same role), enabling this parameter would prevent reports or queries from returning results that include these forbidden combinations, thus enforcing the organization's internal security policies.

**Related Settings:**

- `HideApprovedReadOnly`
- `RolesList`
- `ShowChangesBySystem`
- `TableChangesUsers`

**Best Practices:** 

- **Configure when:** You have identified specific combinations of schemas that are not compliant with your organization's policies or pose security risks.
  
- **Avoid when:** Your organization does not have specific combinations of schemas that are considered risky or non-compliant, or if the restriction would unduly limit necessary access to data for business operations.