# Authorization Review Statistics Calculation Interval In Minutes

**Technical Name:** AuthorizationReviewStatisticsCalculationIntervalInMinutes

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `AuthorizationReviewStatisticsCalculationIntervalInMinutes` parameter defines the time interval, in minutes, for recalculating authorization review statistics in the Pathlock Cloud GRC platform. This includes updating relevant metrics and insights based on the latest data available.

**Business Impact:**

Setting the appropriate interval impacts how current the authorization review statistics are, affecting decision-making related to security, risk, and compliance management. A shorter interval may ensure data is more up-to-date but could increase system load, affecting performance.

**Technical Impact when configured:**

- **Increased Frequency:** A lower value (shorter interval) means more frequent updates, ensuring data is timely, supporting proactive risk management and compliance activities.
- **Performance Consideration:** Setting a very short interval might impact the platform's performance due to the increased frequency of data processing and calculation.

**Examples Scenario:**

- **Scenario for High-Frequency Environments:** In environments where user roles and permissions are highly dynamic, setting a shorter interval ensures that authorization review statistics reflect recent changes more accurately, aiding in timely auditing and compliance checks.
- **Scenario for Stable Environments:** In more static environments, a longer interval could be sufficient, reducing computational load without significantly impacting the relevance of audit and compliance data.

**Related Settings:** 

- DashboardMaxResults
- DashboardSortingOrder

**Best Practices:** 

- **Configure when:** There is a need for up-to-date authorization review statistics to support compliance and security decisions.
- **Avoid when:** The system is already under heavy load or if the environment does not require frequent updates of authorization review statistics.