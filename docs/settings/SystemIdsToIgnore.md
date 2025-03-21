# System Ids To Ignore

**Technical Name:** SystemIdsToIgnore

**Category:** Configuration

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter allows for the specification of system IDs that should be excluded from certain operations within the Pathlock Cloud GRC platform. It is primarily used in user data retrieval contexts to ignore specific systems, thereby preventing the inclusion of data from those systems in user-related queries and operations.

**Business Impact:**

By utilizing the SystemIdsToIgnore parameter, organizations can fine-tune the scope of GRC activities to exclude data from non-relevant or sensitive systems. This ensures that GRC processes like audits, compliance checks, and risk assessments are focused only on relevant systems, which can streamline operations and reduce unnecessary workload.

**Technical Impact when configured:**

When configured, the SystemIdsToIgnore parameter will filter out any user-related data from the specified systems. This means that any processes or workflows that rely on user data from across the organization's systems will not include data from the ignored systems, potentially affecting the comprehensiveness of audits, risk assessments, and other GRC activities.

**Examples Scenario:**

In a scenario where an organization wants to exclude data from a legacy system that is no longer actively managed but still contains historical user data, the SystemIdsToIgnore can be configured to ignore this system's ID. This can help the organization focus on current, active systems for compliance and risk management efforts without deleting the historical data that might still be needed for legal or archival purposes.

**Related Settings:** None

**Best Practices:** Configure when systems contain irrelevant, outdated, or sensitive data that should not impact GRC processes. Avoid when comprehensive data across all systems is necessary for accurate GRC reporting and analysis.