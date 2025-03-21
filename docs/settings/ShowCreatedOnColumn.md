**Technical Name:** ShowCreatedOnColumn

**Category:** Reporting

**Default Value:** False

**Impact Level:** Low

**Description:** This parameter controls whether the "Created On" date column is displayed in various reports and interfaces within the Pathlock Cloud GRC platform.

**Business Impact:** Enabling this parameter provides users with visibility into the creation dates of records, which can be crucial for auditing purposes, understanding the timeline of data entry, and tracking the age of information within the system.

**Technical Impact when configured:** When enabled, the system will include an additional column showing the creation date of records in the relevant reports and interfaces. This may slightly alter the layout or the amount of data loaded on a page, but it is crucial for users who need to reference or audit creation dates.

**Example Scenario:** A compliance officer needs to audit user accounts created within the last quarter to ensure all new accounts have been appropriately authorized and configured according to the company's security policies. By enabling this parameter, they can easily identify when each account was created directly from the user management report, facilitating a timelier and more efficient audit process.

**Related Settings:**
- `SearchUsingContainsInsteadOfStartsWith`: This setting might be relevant when filtering or searching through reports that now include the "Created On" column, affecting how search queries are interpreted and executed.

**Best Practices:** 
- **configure when** tracking or auditing creation dates is essential for compliance, security, or operational purposes.
- **avoid when** the additional information clutters the interface or negatively impacts performance for users who do not require access to creation dates.