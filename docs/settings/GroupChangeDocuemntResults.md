**Group Change Document Results**

**Technical Name:** GroupChangeDocuemntResults

**Category:** Audit

**Default Value:** Not Applicable

**Impact Level:** Medium

**Description:** 

This parameter filters the Change Document records based on specific criteria such as the presence of a username. It ensures that only meaningful data is processed and included in audit trails, by excluding records with empty user fields or those not meeting the defined conditions.

**Business Impact:**

Ensuring that audit trails and change documents contain only relevant information helps in maintaining the integrity of the audit data. It simplifies compliance checks and audit processes by filtering out noise and focusing on significant events.

**Technical Impact when configured:**

When configured, this parameter effectively streamlines the processing of change document records. It reduces the overhead on resources by focusing on records that fulfill the filtering criteria like non-empty usernames, thereby improving system performance and audit data relevancy.

**Example Scenario:**

An organization is undergoing an audit and needs to present all user-related changes within their system for a certain period. Using the GroupChangeDocuemntResults parameter, the system will filter out all irrelevant records, like those without a username, ensuring the audit report is concise and only includes entries significant to the audit.

**Related Settings:**

- `ChangeDocumentRecordSkipDateFilter`

**Best Practices:** Configure when aiming to improve the relevancy of audit records and ensure compliance checks are focused and efficient. Avoid when there is a requirement to capture and audit every change regardless of its relevance or specificity.