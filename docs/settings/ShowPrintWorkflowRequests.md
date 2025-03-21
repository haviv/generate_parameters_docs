# Show Print Workflow Requests

**Technical Name:** ShowPrintWorkflowRequests

**Category:** Workflow

**Default Value:** "Workflow Requests:<br><table>{0}</table><br>"

**Impact Level:** Medium

**Description:**

The `ShowPrintWorkflowRequests` parameter controls the display format of workflow requests within the Pathlock Cloud GRC platform. It specifies how workflow requests are visually organized and presented to the user, typically in a tabular format encapsulated within HTML tags for web-based display.

**Business Impact:**

Adjusting how workflow requests are shown can significantly impact how quickly and efficiently users can identify, understand, and action pending or in-process workflow requests. A clear, concise presentation of workflow requests enhances user experience and facilitates better monitoring and management of business processes.

**Technical Impact when configured:**

When the `ShowPrintWorkflowRequests` parameter is configured, it alters the layout and structure of workflow request displays across the Pathlock Cloud GRC platform. This modification impacts all users viewing workflow requests, making it critical to tailor the display settings to match organizational needs and user preferences for optimal readability and accessibility.

**Examples Scenario:**

A compliance manager regularly reviews in-progress workflow requests to ensure timely processing. By configuring the `ShowPrintWorkflowRequests` parameter to present the data in an organized table format, the manager can more easily identify bottlenecks or outstanding requests, leading to more immediate remedial action and ensuring compliance tasks are completed within set deadlines.

**Related Settings:**

- WorkflowReminderContainerAsTable

**Best Practices:** configure when you need a clear, structured visualization of workflow requests for review, monitoring, or reporting purposes. Avoid custom configurations that could lead to cluttered or confusing displays, hindering the users' ability to effectively manage workflows.