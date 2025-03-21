**Technical Name:** DynamicSoDCreateEventForSingleUse

**Category:** SOD

**Default Value:** False

**Impact Level:** High

**Description:** This parameter controls whether the Pathlock Cloud GRC platform triggers a dynamic Segregation of Duties (SoD) event for single-use scenarios. It is designed to enhance security and compliance by evaluating user activities within a specified timeframe and identifying potential SoD conflicts based on those activities.

**Business Impact:** Enabling this feature ensures that SoD violations are dynamically detected and reported as they occur, allowing organizations to promptly address and mitigate potential risks associated with unauthorized or unintended access combinations. This proactive approach to SoD management significantly contributes to maintaining internal controls and supports compliance with regulatory requirements.

**Technical Impact when configured:** Once enabled, the system filters and assesses user actions based on defined criteria, focusing on changes made during the checked period. This targeted evaluation allows for the timely detection of SoD conflicts, ensuring that only relevant activities trigger an SoD event. As a result, organizations can efficiently allocate resources to investigate and resolve genuine risks, thereby enhancing overall security and compliance posture.

**Example Scenario:** If an organization activates the DynamicSoDCreateEventForSingleUse parameter, and a user performs an action that, combined with their existing permissions, creates a potential SoD conflict, the system will generate an event. This event could indicate that the user, while posting a sales order (an activity within their role), also attempts to approve the same order, a combination that violates company policy on SoD.

**Related Settings:** CheckDynamicSoDOnLogRecordsWithChangesOnly

**Best Practices:** Configure when implementing stringent SoD controls is critical for regulatory compliance or to enhance internal security policies. Avoid enabling it in environments where user permissions are highly dynamic and could result in an excessive number of false positives, leading to "alert fatigue" among administrators.