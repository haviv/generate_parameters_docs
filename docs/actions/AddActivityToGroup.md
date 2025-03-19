# AddActivityToGroup

**Category:** Workflow

**Description:** 

This action is designed to automate the assignment of specific activities to a user group within the Pathlock Cloud platform. It takes two main inputs: an activity group name and an activity mode name. The workflow looks up the activity mode based on the given name and identifies the target group using the activity group name. If both the transaction and the group are valid, the action creates a link (SoxGroupsContent) between the transaction and the group with the specified activity mode (if provided). This process facilitates dynamic access management and operational flexibility, aligning with compliance and governance requirements.

**Parameters:**

- Basic:
  
  Name: TechnicalNameForActivityGroup  
  Description: Specifies the name of the activity group. It is used to locate the group in the database and associate it with the Target transaction.  
  Default value: N/A  
  Mandatory: yes
  
  Name: TechnicalNameForActivityMode  
  Description: Determines the mode in which the activity should be added to the group. It influences how the activity is processed and applied to the group members.
  Default value: N/A  
  Mandatory: no

**Business impact:** 

Implementing this action impacts the business by ensuring that access rights and operational permissions can be dynamically managed and adjusted to meet the evolving needs and compliance requirements of the organization. Efficiently managing activity groups helps streamline processes, mitigate risks associated with access control, and enhance the overall governance framework.

**Example of usage:** 

An administrator wants to add a financial review task to the "Financial Managers" group in "Audit Only" mode. They would configure the action with the "Financial Managers" as the activity group and "Audit Only" as the activity mode. This ensures that members of the "Financial Managers" group can perform the task under the defined constraints, aligning with compliance and audit requirements.

**Prerequisites:** 

- The user executing the action must have administrative rights to manage groups and activities.
- The specified activity group and mode must exist in the system.

**Error Handling and Troubleshooting:** 

- If the activity group name or activity mode name does not exist, the action will not perform any operations. Ensure the names are correctly specified and exist in the system.
- In case of a system exception, refer to the error log for more detailed information about the cause of the failure. Common issues may include database connectivity problems or transactional errors. In such cases, verifying the system's operational status and checking database permissions may resolve the issue.