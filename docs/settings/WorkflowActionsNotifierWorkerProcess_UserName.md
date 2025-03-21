# Workflow Actions Notifier Worker Process User Name

**Technical Name:** WorkflowActionsNotifierWorkerProcess_UserName

**Category:** Workflow

**Default Value:** *Not provided in the code references*

**Impact Level:** Medium

**Description:**

This parameter is related to the Workflow Actions Notifier system within the Pathlock Cloud GRC platform. It specifically handles the identification for user accounts that are associated with the process of notifying users about workflow actions.

**Business Impact:**

Misconfiguration or misuse of this parameter could lead to failures in notifying the relevant personnel about critical workflow actions, potentially delaying response times and impacting operational efficiency and compliance.

**Technical Impact when configured:**

Proper configuration ensures that notifications related to workflow actions are correctly processed and sent out by the designated worker process, using the appropriate user credentials. This is crucial for maintaining the integrity and security of workflow action notifications.

**Examples Scenario:**

For an organization that has implemented the Pathlock Cloud GRC platform, setting this parameter with the correct user name ensures that operational teams receive timely notifications about workflow actions requiring their attention, such as approval requests or reviews. This contributes to smoother operational flows and adherence to compliance protocols.

**Related Settings:**

- WorkflowActionsNotifierWorkerProcess_OpenOn
- WorkflowActionsNotifierWorkerProcess_WaitingSince

**Best Practices:** 

- configure when: You have identified a dedicated user account for handling workflow notifications, ensuring it has the necessary permissions.
- avoid when: The user account specified doesn't exist or lacks permission to send notifications, as this will disrupt the workflow notification process.