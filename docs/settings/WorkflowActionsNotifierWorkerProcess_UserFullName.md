# Workflow Actions Notifier Worker Process User Full Name

**Technical Name:** WorkflowActionsNotifierWorkerProcess_UserFullName

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter configures the display of the user's full name in workflow action notifications. It ensures that notifications are personalized and clearly identifiable by including the full name of the user associated with each workflow action.

**Business Impact:**

Including the user's full name in notifications can improve the clarity and effectiveness of communication within workflow actions. It helps in identifying the source or target of a workflow action quickly, enhancing the speed and efficiency of processing. For organizations using Pathlock's Cloud GRC platform, this personalization can improve user engagement and compliance with workflow tasks. 

**Technical Impact when configured:**

When configured, this parameter modifies notification systems within workflows to include the user's full name. This can affect all workflow-related communications, ensuring a more personalized and user-friendly experience by identifying individuals involved in workflow actions directly.

**Example Scenario:**

- **Context:** An organization uses Pathlock for managing access reviews.
- **Without the parameter configured:** Notifications sent to reviewers simply include a username or an employee number, leading to confusion, especially in large organizations.
- **With the parameter configured:** Notifications now include the full name of the employee in question, allowing reviewers to immediately identify whom the access review concerns.

**Related Settings:**

- WorkflowInstanceId
- ActionName
- UserName

**Best Practices:** 

- **Configure when:** It's crucial to enhance the clarity of workflow notifications, especially in environments with numerous users where identifying individuals by their full name can significantly improve processing time and user experience.
- **Avoid when:** There are strict privacy concerns that restrict the display of full user names in communications.