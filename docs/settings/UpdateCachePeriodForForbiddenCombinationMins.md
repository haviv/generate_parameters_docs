**Update Cache Period For Forbidden Combination Mins**

**Technical Name:** UpdateCachePeriodForForbiddenCombinationMins

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `UpdateCachePeriodForForbiddenCombinationMins` parameter determines the frequency, in minutes, at which the cache for forbidden combinations is refreshed. This setting plays a critical part in ensuring that unauthorized access combinations are updated in a timely manner to prevent security breaches.

**Business Impact:**

Adjusting this parameter has a direct impact on the balance between performance and security. A lower value means the system is more responsive to changes in access rights and segregation of duties (SOD) rules, enhancing compliance. Conversely, too frequent updates may impact system performance.

**Technical Impact when configured:**

- A shorter period (lower value) could lead to increased system load due to more frequent cache updates, potentially affecting overall system performance.
- A longer period (higher value) may delay the detection of forbidden access combinations, posing a risk to system security and compliance.

**Examples Scenario:**

- **Scenario:** An organization requires real-time enforcement of SOD policies due to stringent compliance requirements. They would configure the `UpdateCachePeriodForForbiddenCombinationMins` to a lower value to ensure fast detection and mitigation of access violations.
  
**Related Settings:**

- AuthorizationReviewStatisticsCalculationIntervalInMinutes
- DisplayMyWaitingReviewsOnHomeScreen

**Best Practices:** 

- **Configure when:** Immediate reflection of updates in forbidden access combinations is crucial for business operations and compliance requirements.
- **Avoid when:** The system is experiencing performance issues, or the risk associated with delayed detection of forbidden combinations is low.