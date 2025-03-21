# Max Records For Changes Log Display

**Technical Name:** MaxRecordsForChangesLogDisplay

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

Controls the maximum number of records that can be displayed or processed in the changes log at any given time. This parameter is crucial for maintaining optimal performance and ensuring that system resources are not overwhelmed by excessively large data retrieval operations.

**Business Impact:**

Directly impacts how audit and review processes are managed by limiting the scope of visible changes within a given period. This parameter ensures that system performance remains steady, enhancing the reliability of audit trails for compliance and oversight purposes.

**Technical Impact when configured:**

When set, this parameter limits the number of entries fetched from the database during audits or when monitoring changes, thus preventing potential performance degradation. It also helps in focusing the audit efforts on the most critical or recent changes by filtering excessive data.

**Examples Scenario:**

- **Compliance Review:** During a quarterly compliance review, auditors need to access a manageable subset of change logs to efficiently assess compliance with internal policies and external regulations. Setting an appropriate maximum limit ensures that auditors can efficiently review the most pertinent changes without being overwhelmed by volume.
- **System Performance:** To prevent slowdowns during peak audit periods, the system administrator sets a reasonable limit on the records displayed, ensuring that the system remains responsive even as multiple users access change logs simultaneously.

**Related Settings:** HideApprovalCommentFromCustomReports

**Best Practices:** Configure when the audit and oversight processes require focusing on a subset of changes over specified periods. Avoid high settings in environments where database performance or system resources are a concern.