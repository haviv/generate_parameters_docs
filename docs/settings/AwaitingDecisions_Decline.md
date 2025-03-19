**Technical Name:** AwaitingDecisions_Decline

**Category:** Workflow

**Default Value:** "/Report/UserPerformanceAction.aspx?DecisionId={0}&Decline=True"

**Impact Level:** High

**Description:** This parameter configures the URL redirection for declining pending decisions within the Pathlock Cloud GRC platform. It is used to navigate users to the appropriate report page after they choose to decline a decision awaiting their approval or review. The `{0}` within the URL is dynamically replaced with the specific Decision ID that is being declined.

**Business Impact:** Enables efficient decision management by streamlining the process of declining awaiting decisions. It ensures that decision-makers can easily access and process declinations, which in turn helps maintain operational integrity and compliance by addressing potential risks or non-compliance issues promptly.

**Technical Impact when configured:** When configured, this parameter affects how and where users are redirected upon declining a decision. Proper configuration ensures users are guided to the correct report or dashboard, enhancing user experience and decision-making clarity within the workflow process.

**Examples Scenario:** A manager receives a notification to approve a high-risk access request. After reviewing the details and consulting the relevant compliance policies, the manager decides this request does not adhere to the organizational security standards and opts to decline it. Upon choosing the decline action, the manager is automatically redirected to a summary report detailing their decision, facilitated by the `AwaitingDecisions_Decline` configuration.

**Related Settings:** 
- AwaitingDecisions_Approve

**Best Practices:** 
- **Configure when:** Setting up decision management workflows to ensure that users have a straightforward path to view the outcome of their declined decisions. 
- **Avoid when:** The platform's decision-making process does not require redirection after declining a request, or if all decision-making is handled in an external system.