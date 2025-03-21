# Authorization Review Position Change Notification Year

**Technical Name:** AuthorizationReviewPositionChangeNotificationYear

**Category:** Authorization Review

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures the year for sending notifications related to changes in authorization review positions within the Pathlock Cloud GRC platform. It is pivotal in scheduling and organizing authorization review processes efficiently.

**Business Impact:**

Configuring this parameter assists organizations in maintaining compliance with internal and external audit requirements by ensuring timely review of user access rights. It helps in reducing the risk of unauthorized access by ensuring that changes in critical positions are reviewed and authorized within the set timeframe.

**Technical Impact when configured:**

When configured, this parameter triggers the notification system of the Pathlock GRC platform to send alerts or notifications concerning position changes that require authorization review for the specified year. This ensures that all relevant personnel are informed and can take appropriate action within the designated time frame.

**Examples Scenario:**

- An organization sets the parameter to the current year to ensure that any change in positions with access to sensitive data is reviewed and authorized promptly. This is crucial for maintaining data integrity and preventing data breaches.

**Related Settings:**

- `AuthorizationReviewPageSize`: Related to pagination in the authorization review list, which could be indirectly related to how users interact with reviews triggered by position changes.

**Best Practices:** 

- **Configure when:** It is best to configure this parameter at the start of each fiscal or calendar year to align with the organization’s internal audit and compliance schedules.
  
- **Avoid when:** Avoid setting this parameter inappropriately or not updating it annually, as it may lead to missed reviews, posing security and compliance risks.