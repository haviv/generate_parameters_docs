# Disable Automatic Rebuild Indexes

**Technical Name:** DisableAutomaticRebuildIndexes

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** 

This parameter controls whether the automatic rebuilding of indexes during the synchronization of roles process is enabled or disabled. When set, it prevents the system from executing the rebuild indexes operation automatically after roles have been synchronized.

**Business Impact:**

Enabling this setting can lead to performance improvements by reducing system downtime during role synchronization operations, especially in larger environments. However, it might also result in degraded query performance over time if indexes are not manually maintained.

**Technical Impact when configured:**

When configured, this parameter stops the automatic triggering of the index rebuilding process within the Pathlock GRC platform during role synchronization tasks. This change could necessitate manual intervention to ensure database performance is not affected negatively in the long term.

**Example Scenario:**

- In a scenario where a Pathlock GRC system administrator observes that the automatic rebuilding of indexes significantly impacts system performance during peak hours, they could disable this feature to manage the rebuilding process manually during off-peak times.

**Related Settings:** 

- None

**Best Practices:** 

- Configure when: System performance during role synchronization is a priority, and the administrative team can manage index maintenance manually.
- Avoid when: The administrative overhead of manually managing indexes is not feasible, or if the system does not experience significant performance degradation during synchronization processes.