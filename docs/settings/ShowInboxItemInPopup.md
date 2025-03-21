# Show Inbox Item In Popup

**Technical Name:** ShowInboxItemInPopup

**Category:** Workflow

**Default Value:** True

**Impact Level:** Medium

**Description:**

The `ShowInboxItemInPopup` parameter controls whether items in the Pathlock Cloud GRC platform's workflow inbox are displayed directly within a popup window. Enabling this feature improves user interaction by allowing detailed inspection of workflow items without navigating away from the inbox page.

**Business Impact:**

Enabling this feature streamlines the review process of workflow items, reducing the time and effort required for users to interact with, and respond to, workflow tasks. It enhances user experience and efficiency, especially for users who manage a high volume of workflow items.

**Technical Impact when configured:**

When enabled, workflow items are presented in a popup modal, providing users with immediate access to the content. This configuration reduces page reloads and improves the application's responsiveness, leading to a more efficient workflow management process.

**Examples Scenario:**

A compliance officer needs to review and approve a series of policy changes. With `ShowInboxItemInPopup` enabled, they can quickly click through each item in their inbox, view the details in a popup, make decisions, and perform actions without ever leaving the inbox screen. This capability significantly accelerates the review and approval process.

**Related Settings:**

- CloudAutoRunProcesessSimpleMode

**Best Practices:** configure when the workflow involves frequent and rapid review of inbox items to enhance user satisfaction and efficiency. Avoid when each workflow item requires extensive review time or if displaying items in a popup could distract from detailed analysis.