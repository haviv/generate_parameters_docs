**Update Cache Period For Role Authorizations Mins**

**Technical Name:** UpdateCachePeriodForRoleAuthorizationsMins

**Category:** Configuration

**Default Value:** 5

**Impact Level:** Medium

**Description:**

This parameter configures the time interval in minutes at which authorization review statistics are recalculated and refreshed in the system's cache.

**Business Impact:**

Adjusting this parameter can balance system performance against the need for up-to-date authorization review statistics. A lower value will ensure more current data but may increase load on system resources, while a higher value reduces load but may result in the use of outdated information for decision-making.

**Technical Impact when configured:**

Modifying the UpdateCachePeriodForRoleAuthorizationsMins affects how frequently the system updates the cache with new authorization review statistics. This can impact the performance of the Pathlock Cloud GRC platform, particularly in areas related to security, risk, and compliance reporting and analysis.

**Example Scenario:**

If your organization experiences significant changes in role assignments or permissions frequently, you might reduce the cache update period to ensure that authorization review statistics reflect these changes in a timely manner. Conversely, if changes are less frequent, you could increase the period to reduce system load without significantly impacting the relevance of the data.

**Related Settings:**

While the provided code references did not explicitly link to directly related settings, they imply a connection to overall system caching strategies and performance settings within the Pathlock Cloud GRC platform.

**Best Practices:** 

- Configure the cache period to a lower value during times of significant organizational change to ensure data remains current.
- Avoid setting the cache period too low as a default to prevent unnecessary strain on system resources. Aim for a balance between data freshness and system performance.