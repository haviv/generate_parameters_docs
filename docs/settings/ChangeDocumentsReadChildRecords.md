# Change Documents Read Child Records

**Technical Name:** ChangeDocumentsReadChildRecords

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ChangeDocumentsReadChildRecords` parameter is designed for auditing purposes within the Pathlock Cloud GRC platform. It captures changes in child records within specified tables, aiding in the thorough monitoring of data modifications.

**Business Impact:**

Utilizing this parameter enables organizations to maintain comprehensive audit trails of changes occurring within their ERP systems. It ensures accountability and transparency in operations, particularly in sensitive areas where unauthorized modifications could have significant compliance or operational risks.

**Technical Impact when configured:**

When enabled, this parameter meticulously logs all updates or deletions to child records in specific, non-ignored tables, despite being incrementally set to not capture changes. This ensures that all relevant modifications are captured and available for audit review, providing a granular level of visibility over data changes.

**Examples Scenario:**

An audit team needs to review all recent alterations to employee roles within the SAP environment to ensure compliance with internal segregation of duties policies. By enabling `ChangeDocumentsReadChildRecords`, they can track down every relevant change made to these records, identify who made these changes, and determine if any unauthorized modifications occurred.

**Related Settings:**

- `IsIncreamantly`: Indicates whether changes are captured incrementally. For this parameter, it is set to false, ensuring all changes are logged for the audit records.
- `igonredTable`: Specifies which tables are to be ignored by the reader. For example, "CD1251" is an ignored table and changes to it will not be captured by this parameter.

**Best Practices:** 

- **Configure when:** You require detailed audit trails of changes to sensitive child records within your ERP environment. Essential for compliance with internal controls and external regulatory requirements.
- **Avoid when:** Minimal auditing is sufficient, or if the performance impact of detailed logging outweighs its benefits. In scenarios where only high-level oversight is needed, this detailed logging might be unnecessary.