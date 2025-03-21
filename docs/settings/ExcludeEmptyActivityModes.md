# Exclude Empty Activity Modes

**Technical Name:** ExcludeEmptyActivityModes

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Exclude Empty Activity Modes parameter is designed to enhance the efficiency of authorization and transaction reviewing processes within the Pathlock Cloud GRC platform. Configuring this parameter ensures that activity modes and transactions devoid of significant actions or changes are excluded from review lists, streamlining the review process.

**Business Impact:**

Implementing this parameter can significantly reduce the volume of data that needs to be reviewed, allowing users to focus on more critical and impactful activities. This can lead to a more efficient audit review process, improved risk management, and a reduction in the time and resources needed for compliance activities.

**Technical Impact when configured:**

When configured, the system will filter out and exclude any activity modes or transactions that do not have associated action items or significant data changes. This results in a more focused and efficient review process by displaying only the relevant and impactful activities to the user.

**Example Scenario:**

An organization is using the Pathlock Cloud GRC platform to monitor and review user transactions and activity modes within their financial software systems. They notice that a significant amount of time is being spent reviewing empty or insignificant activity logs. By configuring the Exclude Empty Activity Modes parameter, the organization can streamline this process, allowing their compliance and audit teams to focus on reviewing transactions and activities that have a potential risk or compliance implication.

**Related Settings:** 

- MyAppovalsPortalShowLastTopRequests

**Best Practices:** 

- **Configure when:** You have a high volume of transactions and activities, and there's a need to focus on the most significant items for compliance and risk management.
- **Avoid when:** Every activity, regardless of its significance, is required to be reviewed due to strict regulatory or internal compliance standards.