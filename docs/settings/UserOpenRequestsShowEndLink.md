**User Open Requests Show End Link**

**Technical Name:** UserOpenRequestsShowEndLink

**Category:** Workflow

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of the end link for open requests in the user's profile. When enabled, users can directly navigate to the end of their open requests list, enhancing usability and streamlining the navigation process within the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling this feature significantly improves user experience by allowing users to quickly access the most recent requests without manually scrolling through the list. This can be particularly beneficial for users with a high volume of open requests, reducing the time spent on request management and increasing overall efficiency in managing security, risk, and compliance tasks.

**Technical Impact when configured:**

When this parameter is set to true (`bool.TrueString`), the end link for open requests becomes visible and accessible to the user. Conversely, setting it to false (`bool.FalseString`) hides this link, requiring users to scroll through their open requests manually.

**Examples Scenario:**

A user with administrative privileges in the Pathlock Cloud GRC platform has numerous open requests pending approval or action. By enabling the User Open Requests Show End Link, the platform allows this user to instantly jump to the end of their request list, facilitating quick access to the most recent or last-pending requests, thus saving time and improving the workflow efficiency.

**Related Settings:** 

- EnableCustomWorkflowApprovalGroupResolving
- TransactionHistoryRecordTerminal_NumberOfUsersToDisplay

**Best Practices:** configure when user efficiency and fast navigation through a large number of open requests are desired; avoid when unnecessary to reduce interface clutter and focus users on outstanding items at the top of the list.