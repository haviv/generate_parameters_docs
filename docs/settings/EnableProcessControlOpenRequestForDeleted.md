# Enable Process Control Open Request For Deleted

**Technical Name:** EnableProcessControlOpenRequestForDeleted

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls the ability to open process control requests for deleted items within the Pathlock GRC platform. When enabled, it allows users to initiate workflow processes for items that have been removed, providing a mechanism for review and potential reversal of deletion actions.

**Business Impact:**

Enabling this feature can significantly impact governance, risk management, and compliance (GRC) processes by ensuring that all actions, including deletions, are subject to review and approval. It enhances accountability and transparency in managing critical business processes, especially in highly regulated environments.

**Technical Impact when configured:**

When configured, the system allows initiation of authorization requests for review on actions performed on deleted items, especially within workflows concerning system access rights, transaction activities, and SAP roles. This ensures a robust control environment where even the deletion of items can be audited and reviewed.

**Examples Scenario:**

- A user mistakenly deletes a critical role in the SAP system. With **EnableProcessControlOpenRequestForDeleted** set to True, the deletion can be subjected to a review process, wherein the deletion can be evaluated, potentially preventing unintended loss of access controls.
  
**Related Settings:**

- SendMailOnWorkflowDeclinedToCurrentApprovers

**Best Practices:** 

- Configure when:

  - Your organization requires stringent controls over deletions of items within your GRC processes.
  - You need to maintain an audit trail for all deletions, ensuring that they can be reviewed and possibly reversed if needed.

- Avoid when:

  - Your organization's workflow does not require the overhead of reviewing deletions.
  - The additional step in the workflow process could unduly delay other time-sensitive actions.