# Max Records For Audit

**Technical Name:** MaxRecordsForAudit

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

The Max Records For Audit parameter controls the maximum number of records or entries that can be audited within a given audit operation. This setting ensures the audit processes are manageable and prevents performance degradation by limiting the amount of data processed in single audit operations.

**Business Impact:**

Setting an appropriate limit on the number of records for audit operations has a direct impact on the performance and efficiency of audit processes. It helps in ensuring that critical and relevant audit information is processed promptly, thereby supporting compliance and governance requirements. Proper configuration of this parameter can prevent potential overloads on system resources, thereby maintaining system stability and reliability.

**Technical Impact when configured:**

- Optimizes audit processing time by ensuring only a manageable number of records are processed.
- Helps in maintaining system performance by preventing excessive load during audit operations.
- Ensures that audit logs remain focused on the most relevant data, enhancing the effectiveness of audit reviews.

**Examples Scenario:**

- In a scenario where an organization needs to audit user activities within a particular timeframe, setting Max Records For Audit to a reasonable limit ensures that the system selectively audits only the specified number of records, improving the audit process efficiency and making it easier for auditors to analyze the data.

**Related Settings:** 

- `HRMitigatedUsers` - This setting might be relevant as it deals with user-specific data, similar to audit records filtering.

**Best Practices:** configure when,
- The system experiences performance issues during audit operations.
- Audit operations yield excessively large datasets that are impractical to analyze.

avoid when,
- The default value satisfactorily manages the audit data volume without impacting system performance.
- Detailed audit information is required without any data being omitted due to limitations.